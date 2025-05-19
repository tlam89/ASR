import ollama
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, File, UploadFile, Form, Query       
from fastapi import HTTPException, Request                    
from fastapi.staticfiles import StaticFiles          

from fastapi.middleware.cors import CORSMiddleware   

from pydantic import BaseModel
from typing import List
from src.utils import create_prompt, initialize_a_logger
# from elasticsearch import Elasticsearch # type: ignore

import whisper


logger = initialize_a_logger()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# try:
#     es = Elasticsearch("http://192.168.1.26:9200")
#     logger.debug(f"initial ES8 in server2: {es.ping()}")
# except:
#     logger.debug(f"initial ES8 in server2: None")


class PromptRequest(BaseModel):
    model: str = "llama3.2:3b"
    prompt: str

class SpeechRequest(BaseModel):
    model: str = "base.en"
    audiofile: str

async def generate_response(model: str = "llama3.2:3b", prompt: str = "") -> str:
    try:
        stream = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            stream=True
        )

        response_text = ""

        for chunk in stream:
            response_text += chunk['message']['content']

        return response_text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {e}")

@app.post("/generate")
async def generate_text(request: PromptRequest):
    model = request.model
    prompt = request.prompt
    response = await generate_response(model, str(prompt))

    return {"text": response}

import tempfile
import shutil
model = whisper.load_model("base")
@app.post("/asr/transcribe")
async def asr_whisper(file: UploadFile = File(...)):

    # Save to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        with open(temp_audio.name, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        temp_audio_path = temp_audio.name
    # Run transcription
    result = model.transcribe(temp_audio_path)
    
    return {"transcription": result["text"]}

if __name__ == "__main__":
    import uvicorn # type: ignore

    uvicorn.run(app, host='0.0.0.0', port='6004', debug=True)