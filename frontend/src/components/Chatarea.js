import React, { useState } from 'react';
import './ChatArea.css';

function ChatArea() {
  const [messages, setMessages] = useState([
    { text: 'Hello! How can I assist you?', sender: 'gpt' },
  ]);
  const [inputValue, setInputValue] = useState('');

  // Function to handle sending a message
  const sendMessage = async () => {
    if (!inputValue.trim()) return; // Do nothing if the input is empty

    // Add the user's message to the chat
    const updatedMessages = [...messages, { text: inputValue, sender: 'user' }];
    setMessages(updatedMessages);

    try {
      // Send the user's message to the backend
      const response = await fetch('http://127.0.0.1:5001/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: inputValue }),
      });
      const data = await response.json();

      // Add the assistant's response to the chat
      setMessages([...updatedMessages, { text: data.message, sender: 'gpt' }]);
    } catch (error) {
      console.error('Error:', error);
      setMessages([...updatedMessages, { text: 'Error: Unable to fetch response from GPT', sender: 'gpt' }]);
    }

    // Clear the input field
    setInputValue('');
  };

  // Function to handle Enter key press
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
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
      </div>
      <div className="chat-input-container">
      <select className="ai-model-selector">
          <option>OpenAI</option>
        </select>
        <select className="strategy-selector">
          <option>Pro-SLM</option>
          <option>Chain of Thought</option>
          <option>RAG</option>
        </select>
        <input
          className="input-box"
          placeholder="What can I help you with?"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={handleKeyDown} // Add onKeyDown event listener
        />
        <button className="send-button" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

export default ChatArea;
