import React, { useState } from "react";
import ChatPane from "./components/ChatPane";
import AgentTabs from "./components/AgentTabs";

export default function App() {
  const [currentAgent, setCurrentAgent] = useState("tex");

  return (
    <div className="h-screen w-screen flex flex-col bg-gradient-to-br from-black via-gray-900 to-gray-800">
      <div className="text-2xl font-bold p-4 text-purple-400 tracking-wide">
        🧠 TexOS Genesis Interface
      </div>
      <div className="flex flex-1 overflow-hidden">
        <ChatPane currentAgent={currentAgent} />
        <AgentTabs currentAgent={currentAgent} onSelect={setCurrentAgent} />
      </div>
    </div>
  );
}