FROM python:alpine

LABEL maintainer="Lucien Shui"

COPY . /app

WORKDIR /app

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /app/requirements.txt

CMD ["python", "main.py"]
