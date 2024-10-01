FROM python:3.11.9

ENV PYTHONBUFFERED=1

ENV PORT 8000

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
#CMD gunicorn edmanager.wsgi:application --bind 0.0.0.0:"${PORT}"

EXPOSE ${PORT}