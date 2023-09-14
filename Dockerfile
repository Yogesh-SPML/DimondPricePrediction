FROM python:3.9-slim-buster

COPY . /application
WORKDIR /application


#RUN pip install -r requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "application.py"]
