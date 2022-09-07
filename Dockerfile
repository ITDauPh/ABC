FROM python:3.10
COPY . /APP 
WORKDIR /APP
RUN pip install -r requirements.txt
CMD python project/manage.py runserver 0.0.0.0:8000