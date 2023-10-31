FROM python:3.10-slim

COPY requirements.txt ./requirements.txt
COPY main.py ./main.py

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ARG WORKSPACE

RUN echo "WORKSPACE=$WORKSPACE" >> config.env

EXPOSE 80

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--env-file", "config.env"]