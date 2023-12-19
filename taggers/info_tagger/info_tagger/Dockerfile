# # 
# FROM 192.168.110.45:5000/python:customized

# # 
# WORKDIR /code

# RUN apt-get update

# COPY ./requirements.txt /code/requirements.txt

# # 
# RUN pip install  -r /code/requirements.txt


FROM ner_tagger:latest

# 
COPY ./ /code/


# 
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "2468"]
#CMD ["python","api/main.py"]
CMD ["python","startup.py"]