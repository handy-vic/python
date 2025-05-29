# Microservice for your entity-extraction functionality using FastAPI, which is a modern, fast (high-performance) web framework for building APIs.TXT TO CSV Microservice

1. Install the following packages
pip install fastapi uvicorn python-multipart spacy pandas
python -m spacy download en_core_web_sm

2. Run Service
uvicorn main:app --reload

3. Build the Docker image
docker build -t entity-extractor .

4. Run the container
docker run -d -p 8000:8000 entity-extractor

5. Test it
Open your browser and go to: http://localhost:8000/docs
Upload a .txt file and download a CSV of extracted entities. You can upload .txt files directly via Swagger UI there.

