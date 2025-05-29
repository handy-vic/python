# Microservice for your entity-extraction functionality using FastAPI, Hosted with Docker.

1. Install the following packages:
   pip install fastapi uvicorn python-multipart spacy pandas
  python -m spacy download en_core_web_sm

3. Run Service: uvicorn main:app --reload

5. Build the Docker image: docker build -t entity-extractor .

7. Run the container: docker run -d -p 8000:8000 entity-extractor

9. Open your browser and go to: http://localhost:8000/docs
  Upload a .txt file and download a CSV of extracted entities. You can upload .txt files directly via Swagger UI there.

