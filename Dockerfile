FROM python:3.10

ENV PYTTHONUNBUFFERED = 1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# CMD ["sh","entrypoint.sh"]
CMD ["gunicorn", "--env", "DJANGO_SETTINGS_MODULE=Dante.settings.development", "Dante.wsgi:application", "--bind", "0.0.0.0:8000"]

