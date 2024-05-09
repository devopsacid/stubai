FROM python:3.10-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y curl libgl1-mesa-dev libglib2.0-0 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
COPY /src ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "streamlit", "run", "ui.py", "--server.port", "8080" ]