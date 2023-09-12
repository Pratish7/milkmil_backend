FROM python:3.10

COPY . /app/
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

RUN pip install -r requirements/base.txt
RUN pip install -r requirements/local.txt
RUN pip install -r requirements/production.txt

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]