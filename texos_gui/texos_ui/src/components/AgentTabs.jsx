import React from "react";

// ✅ Define the agents
const agents = [
  { id: "tex", label: "🧠 Tex" },
  { id: "vortex", label: "🛠️ Vortex" },
  { id: "aeondelta", label: "👶 AeonDelta" },
];

// ✅ Component
export default function AgentTabs({ currentAgent, onSelect }) {
  return (
    <div className="w-1/3 p-4 bg-gray-900 text-white flex flex-col space-y-2">
      <h2 className="text-lg font-bold text-purple-400 mb-2">Agents Online</h2>
      {agents.map(agent => (
        <button
          key={agent.id}
          onClick={() => onSelect(agent.id)}
          className={`p-2 rounded border ${
            currentAgent === agent.id
              ? "bg-purple-700 border-purple-400"
              : "bg-gray-800 hover:bg-gray-700 border-gray-600"
          } text-left`}
        >
          {agent.label}
        </button>
      ))}
    </div>
  );
}