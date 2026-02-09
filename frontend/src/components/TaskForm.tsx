"use client";

import { useState } from "react";
import { api, CreateTaskData } from "@/lib/api";

interface TaskFormProps {
  userId: string;
  onTaskCreated: () => void;
  initialData?: { title: string; description: string; priority: string; tags: string[] };
  onCancel?: () => void;
  editMode?: boolean;
  taskId?: number;
}

export default function TaskForm({
  userId,
  onTaskCreated,
  initialData,
  onCancel,
  editMode = false,
  taskId,
}: TaskFormProps) {
  const [title, setTitle] = useState(initialData?.title || "");
  const [description, setDescription] = useState(initialData?.description || "");
  const [priority, setPriority] = useState(initialData?.priority || "medium");
  const [tagsInput, setTagsInput] = useState(initialData?.tags?.join(", ") || "");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    const trimmedTitle = title.trim();
    if (!trimmedTitle) {
      setError("Title is required");
      return;
    }
    if (trimmedTitle.length > 200) {
      setError("Title must be 200 characters or less");
      return;
    }

    const tags = tagsInput
      .split(",")
      .map((t) => t.trim())
      .filter(Boolean);

    setLoading(true);
    try {
      const data: CreateTaskData = {
        title: trimmedTitle,
        description: description.trim() || undefined,
        priority,
        tags,
      };

      if (editMode && taskId) {
        await api.updateTask(userId, taskId, data);
      } else {
        await api.createTask(userId, data);
      }

      if (!editMode) {
        setTitle("");
        setDescription("");
        setPriority("medium");
        setTagsInput("");
      }
      onTaskCreated();
      onCancel?.();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to save task");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow">
      <h2 className="text-lg font-semibold text-gray-900 mb-4">
        {editMode ? "Edit Task" : "Add New Task"}
      </h2>

      {error && (
        <div className="mb-4 bg-red-50 border border-red-200 text-red-700 px-3 py-2 rounded text-sm">
          {error}
        </div>
      )}

      <div className="space-y-4">
        <div>
          <label htmlFor="title" className="block text-sm font-medium text-gray-700">
            Title *
          </label>
          <input
            id="title"
            type="text"
            required
            maxLength={200}
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            placeholder="What needs to be done?"
          />
        </div>

        <div>
          <label htmlFor="description" className="block text-sm font-medium text-gray-700">
            Description
          </label>
          <textarea
            id="description"
            maxLength={1000}
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            rows={3}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            placeholder="Add details (optional)"
          />
        </div>

        <div className="flex gap-4">
          <div className="flex-1">
            <label htmlFor="priority" className="block text-sm font-medium text-gray-700">
              Priority
            </label>
            <select
              id="priority"
              value={priority}
              onChange={(e) => setPriority(e.target.value)}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="high">High</option>
              <option value="medium">Medium</option>
              <option value="low">Low</option>
            </select>
          </div>

          <div className="flex-1">
            <label htmlFor="tags" className="block text-sm font-medium text-gray-700">
              Tags
            </label>
            <input
              id="tags"
              type="text"
              value={tagsInput}
              onChange={(e) => setTagsInput(e.target.value)}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              placeholder="work, personal (comma-separated)"
            />
          </div>
        </div>
      </div>

      <div className="mt-4 flex gap-2">
        <button
          type="submit"
          disabled={loading}
          className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
        >
          {loading ? "Saving..." : editMode ? "Update Task" : "Add Task"}
        </button>
        {onCancel && (
          <button
            type="button"
            onClick={onCancel}
            className="px-4 py-2 bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200"
          >
            Cancel
          </button>
        )}
      </div>
    </form>
  );
}
