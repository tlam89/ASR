import React, { useState, KeyboardEvent, ChangeEvent, useEffect } from 'react';
import { AudioManager } from "./AudioManager";

interface Message {
  sender: string;
  text: string | null;
}

interface ChatInterfaceProps {
  initialMessages?: Message[];
}

const ChatInterface: React.FC<ChatInterfaceProps> = ({ initialMessages = [] }) => {
  const [messages, setMessages] = useState<Message[]>(initialMessages);
  const [input, setInput] = useState<string>('');
  const [whisperResponse, setWhisperResponse] = useState<string | null>("")
  // const [llmResponse, setLlmResponse] = useState<string | null>("")

  const handleSend = () => {
    if (input.trim() === '') return;

    const newMessage: Message = { sender: 'User', text: input };
    if (input) {
      setMessages(prev => [...prev, newMessage]);
      sendMessage(input);
    };
    setInput('');
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setInput(e.target.value);
  };

  

  const sendMessage = async (text: string) => {
      try {
          const response = await fetch('http://localhost:6004/generate', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({
              model: "llama3.2:3b",
              prompt: text,
          }),
          });

          if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
          }

          const data = await response.json();
          // setLlmResponse();
          setTimeout(() => {
            const botMessage: Message = { sender: 'Bot', text: `${data.text}` };
            setMessages(prev => [...prev, botMessage]);
          }, 500);
          
      } catch (error) {
          console.error('Error sending audio to FastAPI:', error);
      }
    };

  useEffect(() => {
      if (whisperResponse) {
        const newMessage: Message = { sender: 'User', text: whisperResponse };
        setMessages(prev => [...prev, newMessage]);
        sendMessage(whisperResponse);
        setWhisperResponse("");
      };
  }, [whisperResponse]);

  return (
    <div className="flex flex-col h-full max-h-screen bg-gray-800 text-gray-300 p-4 rounded shadow-md">
      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto bg-gray-900 rounded p-4 mb-4">
        {messages && 
          messages.map((msg, index) => (
            <div
              key={index}
              className={`mb-2 ${msg.sender === 'User' ? 'text-blue-400' : 'text-green-400'}`}
            >
              <span className="font-semibold">{msg.sender}:</span> {msg.text}
            </div>
          ))
        }
        
      </div>

      {/* Input Area */}
      <div className="flex space-x-2">
        
        <AudioManager whisperListener= {setWhisperResponse} />
        
        <input
          type="text"
          className="flex-1 px-3 py-2 rounded bg-gray-700 text-white placeholder-gray-400 focus:outline-none"
          placeholder="Type a message..."
          value={input}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
        />
        <button
          onClick={handleSend}
          className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded text-white font-semibold"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatInterface;
