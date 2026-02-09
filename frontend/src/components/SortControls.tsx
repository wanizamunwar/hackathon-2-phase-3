"use client";

interface SortControlsProps {
  sortBy: string;
  onSortByChange: (value: string) => void;
  sortOrder: string;
  onSortOrderChange: (value: string) => void;
}

export default function SortControls({
  sortBy,
  onSortByChange,
  sortOrder,
  onSortOrderChange,
}: SortControlsProps) {
  return (
    <div className="flex items-center gap-2">
      <span className="text-sm text-gray-600">Sort by:</span>
      <select
        value={sortBy}
        onChange={(e) => onSortByChange(e.target.value)}
        className="px-2 py-1 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
      >
        <option value="created_at">Date Created</option>
        <option value="priority">Priority</option>
        <option value="title">Title</option>
      </select>

      <button
        onClick={() => onSortOrderChange(sortOrder === "asc" ? "desc" : "asc")}
        className="px-2 py-1 border border-gray-300 rounded-md text-sm hover:bg-gray-50"
        title={sortOrder === "asc" ? "Ascending" : "Descending"}
      >
        {sortOrder === "asc" ? "\u2191 Asc" : "\u2193 Desc"}
      </button>
    </div>
  );
}
