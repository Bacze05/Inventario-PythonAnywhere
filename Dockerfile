FROM python:3.10

ENV PYTTHONUNBUFFERED = 1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["sh","entrypoint.sh"]


