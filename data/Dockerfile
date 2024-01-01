# 
FROM python:slim-buster
# FROM data_access
# 
WORKDIR /code

RUN apt-get update
#
COPY ./requirements.txt /code/requirements.txt
# 
RUN pip install  -r /code/requirements.txt

COPY ./ /code/

CMD ["python","views/main.py"]