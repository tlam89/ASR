#!/bin/bash
echo "Starting Ollama server..."
ollama serve &

# Wait for the Ollama server to start
sleep 1

# Check if the model exists
if ! ollama list | grep -q "llama3.2:3b"; then
    echo "Model llama3.2:3b not found. Pulling..."
    ollama pull llama3.2:3b
else
    echo "Model llama3.2:3b already exists. Skipping pull."
fi

echo "Starting FastAPI..."
exec uvicorn main:app --host 0.0.0.0 --port 6004 --reload
