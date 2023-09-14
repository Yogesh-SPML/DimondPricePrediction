FROM python:3.9-slim-buster
WORKDIR /application
COPY . /application

#RUN pip install -r requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python3", "application.py"]