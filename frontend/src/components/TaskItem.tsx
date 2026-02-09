"use client";

import { useState } from "react";
import { api, Task } from "@/lib/api";
import TaskForm from "./TaskForm";

const priorityColors: Record<string, string> = {
  high: "bg-red-100 text-red-800",
  medium: "bg-yellow-100 text-yellow-800",
  low: "bg-green-100 text-green-800",
};

interface TaskItemProps {
  task: Task;
  userId: string;
  onTaskUpdated: () => void;
  onTaskDeleted: () => void;
}

export default function TaskItem({ task, userId, onTaskUpdated, onTaskDeleted }: TaskItemProps) {
  const [editing, setEditing] = useState(false);
  const [confirmDelete, setConfirmDelete] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleToggleComplete = async () => {
    setLoading(true);
    try {
      await api.toggleComplete(userId, task.id);
      onTaskUpdated();
    } catch {
      // Error handled by parent
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async () => {
    setLoading(true);
    try {
      await api.deleteTask(userId, task.id);
      onTaskDeleted();
    } catch {
      // Error handled by parent
    } finally {
      setLoading(false);
      setConfirmDelete(false);
    }
  };

  if (editing) {
    return (
      <TaskForm
        userId={userId}
        editMode
        taskId={task.id}
        initialData={{
          title: task.title,
          description: task.description || "",
          priority: task.priority,
          tags: task.tags,
        }}
        onTaskCreated={onTaskUpdated}
        onCancel={() => setEditing(false)}
      />
    );
  }

  return (
    <div className={`bg-white p-4 rounded-lg shadow flex items-start gap-3 ${task.completed ? "opacity-60" : ""}`}>
      <button
        onClick={handleToggleComplete}
        disabled={loading}
        className={`mt-0.5 w-5 h-5 rounded border-2 flex-shrink-0 flex items-center justify-center ${
          task.completed
            ? "bg-blue-600 border-blue-600 text-white"
            : "border-gray-300 hover:border-blue-400"
        }`}
        aria-label={task.completed ? "Mark incomplete" : "Mark complete"}
      >
        {task.completed && (
          <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
          </svg>
        )}
      </button>

      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2 flex-wrap">
          <h3 className={`font-medium text-gray-900 ${task.completed ? "line-through" : ""}`}>
            {task.title}
          </h3>
          <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${priorityColors[task.priority] || priorityColors.medium}`}>
            {task.priority}
          </span>
        </div>

        {task.description && (
          <p className="mt-1 text-sm text-gray-600">{task.description}</p>
        )}

        <div className="mt-2 flex items-center gap-2 flex-wrap">
          {task.tags.map((tag) => (
            <span key={tag} className="px-2 py-0.5 bg-gray-100 text-gray-600 rounded text-xs">
              {tag}
            </span>
          ))}
          <span className="text-xs text-gray-400">
            {new Date(task.created_at).toLocaleDateString()}
          </span>
        </div>
      </div>

      <div className="flex gap-1 flex-shrink-0">
        <button
          onClick={() => setEditing(true)}
          className="px-2 py-1 text-xs text-gray-600 hover:text-blue-600 hover:bg-blue-50 rounded"
        >
          Edit
        </button>

        {confirmDelete ? (
          <div className="flex gap-1">
            <button
              onClick={handleDelete}
              disabled={loading}
              className="px-2 py-1 text-xs text-white bg-red-600 hover:bg-red-700 rounded disabled:opacity-50"
            >
              Confirm
            </button>
            <button
              onClick={() => setConfirmDelete(false)}
              className="px-2 py-1 text-xs text-gray-600 hover:bg-gray-100 rounded"
            >
              Cancel
            </button>
          </div>
        ) : (
          <button
            onClick={() => setConfirmDelete(true)}
            className="px-2 py-1 text-xs text-gray-600 hover:text-red-600 hover:bg-red-50 rounded"
          >
            Delete
          </button>
        )}
      </div>
    </div>
  );
}
