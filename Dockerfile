FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y locales && \
    sed -i '/pt_BR.UTF-8/s/^# //' /etc/locale.gen && \
    locale-gen
    
ENV LANG=pt_BR.UTF-8 \
    LANGUAGE=pt_BR:pt:en \
    LC_ALL=pt_BR.UTF-8


RUN pip install --no-cache-dir pipenv

WORKDIR /app

COPY . /app/

RUN pipenv install --deploy --system

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]