import React, { useState, useRef } from 'react';
import './ChatArea.css';

function ChatArea() {
  const [messages, setMessages] = useState([
    { text: 'Hello! How can I assist you?', sender: 'gpt' },
  ]);
  const [inputValue, setInputValue] = useState('');
  const [selectedStrategy, setSelectedStrategy] = useState('None');
  const messageEndRef = useRef(null);

  const scrollToBottom = () => {
    messageEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  // Function to handle sending a message
  const sendMessage = async () => {
    if (!inputValue.trim()) return; // Do nothing if the input is empty

    // Add the user's message to the chat
    const updatedMessages = [...messages, { text: inputValue, sender: 'user' }];
    setMessages(updatedMessages);

    try {
      // Ensure that the selected strategy is 'Standard' if nothing else is selected
      const strategyToSend = selectedStrategy === 'None' ? 'Standard' : selectedStrategy;

      // Send the user's message and selected strategy to the backend
      const response = await fetch('http://127.0.0.1:5001/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: inputValue,
          strategy: strategyToSend, // Send the correct strategy
        }),
      });

      const data = await response.json();
      setMessages([...updatedMessages, { text: data.message, sender: 'gpt' }]);
    } catch (error) {
      console.error('Error:', error);
      setMessages([...updatedMessages, { text: 'Error: Unable to fetch response from GPT', sender: 'gpt' }]);
    }

    // Clear the input field
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
        <select className="ai-model-selector">
          <option>OpenAI</option>
        </select>
        <div className="strategy-selector-container">
          <select
            className="strategy-selector"
            id="strategy"
            value={selectedStrategy}
            onChange={(e) => setSelectedStrategy(e.target.value)}
          >
            <option>Standard</option>
            <option>Pro-SLM</option>
            <option>Chain of Thought</option>
            <option value="RAG">RAG</option>
          </select>
        </div>
        <input
          className="input-box"
          placeholder="What can I help you with?"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={(e) => { if (e.key === 'Enter') sendMessage(); }}
        />
        <button className="send-button" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

export default ChatArea;
