import React, { useState, useRef } from 'react';
import './ChatArea.css';

function ChatArea() {
  const [messages, setMessages] = useState([
    { text: 'Hello! How can I assist you?', sender: 'gpt' },
  ]);
  const [inputValue, setInputValue] = useState('');
  const [selectedStrategy, setSelectedStrategy] = useState('Standard');
  const [selectedModel, setSelectedModel] = useState('Chatgpt');
  const messageEndRef = useRef(null);

  const scrollToBottom = () => {
    messageEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  // Function to handle sending a message
  const sendMessage = async () => {
    if (!inputValue.trim()) return;

    const updatedMessages = [...messages, { text: inputValue, sender: 'user' }];
    setMessages(updatedMessages);

    try {
      const response = await fetch('http://127.0.0.1:5001/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: inputValue,
          ai_model: selectedModel,
          strategy: selectedStrategy,
        }),
      });

      const data = await response.json();
      setMessages([...updatedMessages, { text: data.message, sender: 'gpt' }]);
    } catch (error) {
      console.error('Error:', error);
      setMessages([
        ...updatedMessages,
        { text: 'Error: Unable to fetch response from AI model', sender: 'gpt' },
      ]);
    }

    setInputValue('');
  };

  return (
    <div className="chat-area">
      <div className="messages-container">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${message.sender === 'user' ? 'user-message' : 'gpt-message'}`}
          >
            {message.text}
          </div>
        ))}
        <div ref={messageEndRef} />
      </div>
      <div className="chat-input-container">
        <select className="ai-model-selector" onChange={(e) => setSelectedModel(e.target.value)} value={selectedModel}>
          <option>Chatgpt</option>
          <option>Claude</option>
        </select>

        <select
          className="strategy-selector"
          value={selectedStrategy}
          onChange={(e) => setSelectedStrategy(e.target.value)}
        >
          <option>Standard</option>
          <option>Pro-SLM</option>
          <option>Chain of Thought</option>
          <option value="RAG">RAG</option>
        </select>

        <input
          className="input-box"
          placeholder="What can I help you with?"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter') sendMessage();
          }}
        />
        <button className="send-button" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

export default ChatArea;
