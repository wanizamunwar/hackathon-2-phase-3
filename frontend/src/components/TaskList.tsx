"use client";

import { Task } from "@/lib/api";
import TaskItem from "./TaskItem";

interface TaskListProps {
  tasks: Task[];
  userId: string;
  onTaskUpdated: () => void;
  onTaskDeleted: () => void;
}

export default function TaskList({ tasks, userId, onTaskUpdated, onTaskDeleted }: TaskListProps) {
  if (tasks.length === 0) {
    return (
      <div className="text-center py-12 bg-white rounded-lg shadow">
        <p className="text-gray-500 text-lg">No tasks yet</p>
        <p className="text-gray-400 text-sm mt-1">Create your first task above to get started!</p>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      <h2 className="text-lg font-semibold text-gray-900">
        Your Tasks ({tasks.length})
      </h2>
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          task={task}
          userId={userId}
          onTaskUpdated={onTaskUpdated}
          onTaskDeleted={onTaskDeleted}
        />
      ))}
    </div>
  );
}
