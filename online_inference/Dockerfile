FROM python:3.8-slim

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY configs/ ./configs/
COPY models/ ./models/
COPY src/ ./src/

COPY app.py ./app.py

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
