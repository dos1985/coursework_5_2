FROM python:3.10-slim

WORKDIR /CODE
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["sh","entrypoint.sh"]
