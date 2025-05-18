import React, { useState } from "react";
import { useTranscriber } from "../hooks/useTranscriber";
import Transcript from "./Transcript";
import { AudioManager } from "./AudioManager";

const RightSidebar: React.FC = () => {
  const transcriber = useTranscriber();
  const [whisperResponse, setWhisperResponse] = useState<string>("")
    return (
      <section className="col-[3/4] row-[1/3] bg-gray-800 border-l border-black/10 p-4 flex flex-col">
        <h2 className="text-white text-lg font-semibold mb-4">Chat</h2>
        <div className="flex-1 bg-gray-900 rounded p-2 overflow-y-auto text-gray-300">
          <p className="mb-2">User 1: {whisperResponse}!</p>
          <p className="mb-2">User 2: Hi there!</p>
        </div>
        <div className='container flex flex-col justify-center items-center'>
          <AudioManager transcriber={transcriber} whisperListener= {setWhisperResponse} />
          <Transcript transcribedData={transcriber.output} />
        </div>
      </section>
    );
  };

export default RightSidebar;