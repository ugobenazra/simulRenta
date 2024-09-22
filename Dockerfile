# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

#COPY src/SimulRenta.py src/utils.py /app/
#COPY pyproject.toml poetry.lock /app/
COPY . .

RUN pip install poetry
RUN poetry install

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["poetry", "run", "streamlit", "run", "src/SimulRenta.py", "--server.port=8501", "--server.address=0.0.0.0"]
