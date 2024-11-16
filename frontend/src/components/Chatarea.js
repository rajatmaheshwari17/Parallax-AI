import React, { useState, useRef, useEffect } from 'react';
import './ChatArea.css';

function ChatArea() {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [selectedStrategy, setSelectedStrategy] = useState('Standard');
  const [selectedModel, setSelectedModel] = useState('Chatgpt');
  const [isProcessing, setIsProcessing] = useState(false); // Track whether AI is processing
  const messageEndRef = useRef(null);

  const scrollToBottom = () => {
    messageEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    // Simulate typing effect for the initial greeting message
    const initialMessage = 'Hello! How can I assist you?';
    simulateTypingEffect(initialMessage, []);
  }, []); // Empty dependency array ensures this runs only once after the component mounts

  // Function to handle sending a message
  const sendMessage = async () => {
    if (!inputValue.trim() || isProcessing) return; // Don't send message if AI is processing

    const updatedMessages = [...messages, { text: inputValue, sender: 'user' }];
    setMessages(updatedMessages);
    setIsProcessing(true); // Set processing state to true

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

      // Start the typing effect with the AI response
      simulateTypingEffect(data.message, updatedMessages);

    } catch (error) {
      console.error('Error:', error);
      setMessages([
        ...updatedMessages,
        { text: 'Error: Unable to fetch response from AI model', sender: 'gpt' },
      ]);
    }

    setInputValue('');
    setIsProcessing(false); // Reset processing state after response is received
  };

  const simulateTypingEffect = (message, updatedMessages) => {
    let i = 0;
    const typingSpeed = 50; // Adjust the typing speed (milliseconds)
    const interval = setInterval(() => {
      if (i < message.length) {
        setMessages((prevMessages) => [
          ...updatedMessages,
          { text: message.slice(0, i + 1), sender: 'gpt' },
        ]);
        i++;
      } else {
        clearInterval(interval); // Stop typing effect when finished
      }
    }, typingSpeed);
  };

  return (
    <div className="chat-area">
      <div className="messages-container">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`message ${message.sender === 'user' ? 'user-message' : 'gpt-message'}`}
            // Use dangerouslySetInnerHTML to render HTML content
            dangerouslySetInnerHTML={{ __html: message.text }}
          />
        ))}
        <div ref={messageEndRef} />
      </div>
      <div className="chat-input-container">
        <select
          className="ai-model-selector"
          onChange={(e) => setSelectedModel(e.target.value)}
          value={selectedModel}
        >
          <option>Chatgpt</option>
          <option>Claude</option>
          <option>Gemini</option>
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
          disabled={isProcessing} // Disable input when processing
        />
        <button
          className="send-button"
          onClick={sendMessage}
          disabled={isProcessing} // Disable button when processing
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default ChatArea;
