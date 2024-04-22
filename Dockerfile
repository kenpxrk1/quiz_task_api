FROM python:3.10 

RUN mkdir /quiz-api

WORKDIR /quiz-api

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

COPY requirments.txt .

RUN pip install --no-cache-dir --upgrade -r requirments.txt

COPY . .

RUN chmod a+x docker/*.sh
