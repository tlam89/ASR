import ChatInterface from "./ChatInterface";

const RightSidebar: React.FC = () => {
  
    return (
      <section className="col-[3/4] row-[1/3] bg-gray-800 border-l border-black/10 p-4 flex flex-col">
        <h2 className="text-white text-lg font-semibold mb-4">Chat</h2>
        <div className="flex-1 bg-gray-900 rounded p-2 overflow-y-auto text-gray-300">
          <ChatInterface />
        </div>
      </section>
    );
  };

export default RightSidebar;