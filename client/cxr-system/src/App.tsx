import "./css/App.css";
import LeftSideBar from "./components/LeftSidebar";
import MiddleContainer from "./components/MiddleContainer";
import RightSidebar from "./components/RightSidebar";
function App() {

  return (   
    <div className="flex justify-center bg-black min-h-screen">

      <main className="relative w-[100vw] h-[100vh] bg-gray-700 shadow-[0_4px_4px_rgba(0,0,0,0.08)] grid grid-cols-[1fr_4fr_2fr] grid-rows-[59px_1fr] overflow-hidden"> 
        <LeftSideBar/>
        <MiddleContainer/>
        <RightSidebar/>        
      </main>
    </div>

  )
}

export default App
