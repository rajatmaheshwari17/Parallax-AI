import React, { useState } from 'react';
import '@fortawesome/fontawesome-free/css/all.min.css';
import Sidebar from './components/Sidebar';
import ChatArea from './components/Chatarea';
import './App.css';

function App() {
  const [isSidebarVisible, setIsSidebarVisible] = useState(true);

  const toggleSidebar = () => {
    setIsSidebarVisible(!isSidebarVisible);
  };

  return (
    <div className="app-container">
      <button className="toggle-sidebar-button" onClick={toggleSidebar}>
        <i className={`fas ${isSidebarVisible ? 'fa-bars' : 'fa-times'}`}></i> {/* Toggle between icons */}
      </button>

      {isSidebarVisible && <Sidebar />} {/* Show Sidebar if visible */}
      <ChatArea />
    </div>
  );
}
export default App;