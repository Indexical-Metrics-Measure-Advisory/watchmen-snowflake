FROM python:3.9.6-slim-buster

WORKDIR /app
ADD . .
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8001
CMD ["uvicorn","watchmen.main:app","--host", "0.0.0.0", "--port", "80"]






