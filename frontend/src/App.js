import React, { useState, useEffect } from 'react';
import '@fortawesome/fontawesome-free/css/all.min.css';
import Sidebar from './components/Sidebar';
import ChatArea from './components/Chatarea';
import './App.css';
import logo from './logo.png'; // Import your logo

function App() {
  const [isSidebarVisible, setIsSidebarVisible] = useState(true);
  const [showSplash, setShowSplash] = useState(true); // State to control splash screen visibility

  useEffect(() => {
    // Hide the splash screen after 3 seconds and show the chat area
    const timer = setTimeout(() => {
      setShowSplash(false);
    }, 3000); // 3 seconds duration for splash screen
    return () => clearTimeout(timer); // Clean up the timer when the component unmounts
  }, []);

  const toggleSidebar = () => {
    setIsSidebarVisible(!isSidebarVisible);
  };

  return (
    <div className="app-container">
      {/* Splash Screen */}
      {showSplash && (
        <div className="splash-screen">
          <img src={logo} alt="Parallax AI Logo" className="logo" />
        </div>
      )}

      {/* Chat Area */}
      {!showSplash && (
        <>
          <button className="toggle-sidebar-button" onClick={toggleSidebar}>
            <i className={`fas ${isSidebarVisible ? 'fa-bars' : 'fa-times'}`}></i> {/* Toggle between icons */}
          </button>

          {isSidebarVisible && <Sidebar />} {/* Show Sidebar if visible */}
          <ChatArea />
        </>
      )}
    </div>
  );
}

export default App;
