# Microservice for your entity-extraction functionality using FastAPI, which is a modern, fast (high-performance) web framework for building APIs.TXT TO CSV Microservice

1. Install the following packages
pip install fastapi uvicorn python-multipart spacy pandas
python -m spacy download en_core_web_sm

2. Run Service
uvicorn main:app --reload

Access the docs at: http://127.0.0.1:8000/docs
You can upload .txt files directly via Swagger UI there.
