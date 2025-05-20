import React, { useState } from "react";

export default function ChatPane({ messages, input, setInput, sendMessage, currentAgent }) {
  return (
    <div className="w-2/3 p-4 flex flex-col bg-black text-white">
      <div className="flex-1 overflow-y-auto space-y-2 p-2 bg-gray-900 rounded">
        {messages.map((msg, i) => (
          <div key={i} className={`p-2 rounded ${msg.from === "you" ? "bg-purple-700" : "bg-gray-700"}`}>
            <strong>{msg.from}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <div className="mt-4 flex">
        <input
          className="flex-1 p-2 rounded bg-gray-800 text-white border border-gray-600"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === "Enter" && sendMessage()}
          placeholder={`Talk to ${currentAgent}...`}
        />
        <button onClick={sendMessage} className="ml-2 px-4 py-2 bg-purple-600 rounded hover:bg-purple-500">
          Send
        </button>
      </div>
    </div>
  );
}
