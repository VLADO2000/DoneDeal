#Base image to start with
FROM python:3.11-slim-bullseye 
#Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
#Prevent form writing .pyc files while importing
ENV PYTHONDONOTWRITEBYTECODE 1
#Preventing from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

#Set working directory
WORKDIR /DD_project

#Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Copy the project
COPY . . 