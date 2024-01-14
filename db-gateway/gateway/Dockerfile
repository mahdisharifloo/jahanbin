# 
FROM python:slim-buster

# RUN apt-get update
# 
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install  -r /code/requirements.txt

COPY ./ /code/

CMD ["python","api/main.py"]