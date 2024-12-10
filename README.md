

# Parallax-AI

Parallax-AI is an advanced AI-powered conversational application that integrates multiple AI models and conversational strategies to provide users with dynamic, real-time responses. The project supports popular models like **ChatGPT**, **Claude**, and **Gemini**, and incorporates advanced strategies such as **Pro-SLM**, **RAG**, and **Chain of Thought** to enhance the user experience. Parallax-AI's unique real-time typing effect mimics human conversation, making the interactions more engaging and natural.



## Features

-   **Multi-Model Integration**: Choose between **ChatGPT**, **Claude**, and **Gemini** for varied conversational styles.
-   **Customizable Strategies**: Switch between **Standard**, **Pro-SLM**, **RAG**, and **Chain of Thought** strategies for optimized responses.
-   **Real-Time Typing Effect**: AI responses are displayed with a dynamic typing effect, mimicking real-time typing for a more immersive experience.
-   **Interactive User Interface**: Built with **React** for a smooth and responsive UI that enables easy model and strategy selection.
-   **Real-Time Conversations**: Messages are delivered and processed in real-time to create a more natural interaction flow.
-   **Seamless Backend Integration**: Backend powered by **Flask**, connecting the front-end to various AI APIs to generate responses based on the user's input.


## Technologies Used

-   **Frontend**:
    
    -   **React**: Used to build the user interface.
    -   **JavaScript (ES6+)**: For handling dynamic user interactions.
    -   **CSS**: For styling the application and ensuring a responsive layout.
-   **Backend**:
    
    -   **Flask**: A lightweight Python web framework for managing API requests and serving AI models.
    -   **OpenAI GPT-3.5**, **Claude** by Anthropic, and **Google Gemini** APIs: For AI-powered conversation generation.
    -   **Python**: For backend logic and interaction with AI models and external APIs.


## Setup and Installation

### Prerequisites

-   **Node.js** and **npm** installed for the frontend.
-   **Python** and **pip** installed for the backend.
-   **API Keys** for OpenAI, Anthropic (Claude), and Google Gemini.



### 1. Clone the Repository

To get started with the project, clone this repository to your local machine:

```bash
git clone git@github.com:rajatmaheshwari17/Parallax-AI.git
cd Parallax-AI
```



### 2. Install Frontend Dependencies

Navigate to the `frontend` directory and install the required dependencies using **npm**:

```bash
cd frontend
npm install
```



### 3. Install Backend Dependencies

Navigate to the `backend` directory and install the required dependencies using **pip**:

```bash
cd backend
pip install -r requirements.txt
```



### 4. Configure API Keys

You need to configure API keys for the AI models (OpenAI, Anthropic, Google Gemini). Create a `.env` file in the **backend** folder and add the following:

```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
```

Replace `your_openai_api_key`, `your_anthropic_api_key`, and `your_google_api_key` with your actual API keys.


## Running the Application

### 1. Start the Backend Server

Navigate to the **backend** folder and run the following command to start the Flask server:

```bash
python3 -m backend.models.model
```

This will start the server on `http://127.0.0.1:5001`, where it will handle AI model requests.

### 2. Start the Frontend Server

In the **frontend** folder, run the following command to start the React development server:

```bash
npm start
```

This will open the frontend on `http://localhost:3001`.

## Usage

-   **Model Selection**: Select between **ChatGPT**, **Claude**, or **Gemini** to switch between different conversational styles.
-   **Strategy Selection**: Choose between **Standard**, **Pro-SLM**, **RAG**, and **Chain of Thought** strategies to optimize the AI's response generation.
-   **Real-Time Typing Effect**: Responses are dynamically typed out, providing a realistic conversational experience.

### Example Flow:

1.  The user types a message in the input box.
2.  Once sent, the AI’s response is generated with a typing effect simulating real-time communication.
3.  Users can interact by changing the model and strategy.


## API Endpoints

The backend server exposes the following **POST** endpoint:

### **POST /chat**

-   **Description**: Sends a message to the selected AI model and returns the generated response.
-   **Request Body**:
    
    ```json
    {
      "message": "User's message here",
      "ai_model": "Chatgpt" | "Claude" | "Gemini",
      "strategy": "Standard" | "Pro-SLM" | "Chain of Thought" | "RAG"
    }
    ```
    
-   **Response**:
    
    ```json
    {
      "message": "AI's generated response here"
    }
    ```


#
_This README is a part of the Parallax-AI Project by Rajat Maheshwari._
