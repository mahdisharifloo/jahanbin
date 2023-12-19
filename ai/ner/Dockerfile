
FROM huggingface/transformers-gpu:latest

WORKDIR /code

RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list

RUN   apt-get update


COPY ./requirements.txt /code/requirements.txt

RUN pip install  -r /code/requirements.txt

COPY ./ /code/

CMD ["python3","api/main.py"]
