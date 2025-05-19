FROM python:3.11

RUN apt-get update && apt-get install -y \
    curl \
    procps \
    ffmpeg\
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN ollama start & \
    sleep 5 && \
    ollama run llama3.2:3b && \
    kill $(pgrep ollama)

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --upgrade pip


RUN pip install --no-cache-dir -r requirements.txt
RUN pip install git+https://github.com/openai/whisper.git 
RUN pip install faiss-cpu llama-cpp-python
RUN pip install nltk


# Download the punkt_tab resource
# RUN python -m nltk.downloader punkt_tab punkt stopwords

COPY . /app/

EXPOSE 6004 
ENTRYPOINT ["/app/entrypoint.sh"]