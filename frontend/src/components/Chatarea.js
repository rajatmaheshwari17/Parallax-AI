import React from 'react';
import './ChatArea.css';

function ChatArea() {
  return (
    <div className="chat-area">
      <div className="chat-input-container">
        {/* Dropdowns next to the input box */}
        <select className="ai-model-selector">
          <option>OpenAI</option>
        </select>
        <select className="strategy-selector">
          <option>Pro-SLM</option>
          <option>Chain of Thought</option>
          <option>RAG</option>
        </select>
        <input type="text" placeholder="What can I help you with?" className="input-box" />
        <button className="send-button">➤</button>
      </div>
    </div>
  );
}
export default ChatArea;
