
FROM node:18 AS builder
RUN echo "Stage 1"
EXPOSE 8000



#ENV NODE_OPTIONS=--openssl-legacy-provider
ENV NODE_VERSION=18.13.0

# Build frontend
WORKDIR /app/frontend
COPY ./frontend .

RUN yarn install
RUN yarn build # builds to ../backend/static

#COPY . ..
#RUN ../run yarn:build:js && ../run yarn:build:css

FROM python:3.10-slim

RUN echo "Stage 2"
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY backend/requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY ./backend /app

COPY --from=builder /app/backend/static /app/static


# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]


CMD ["python", "manage.py", "makemigrations", "models"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload", "--settings", "config.production"]

#RUN python manage.py runserver 0.0.0.0:8000
