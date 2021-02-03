FROM python:alpine

LABEL maintainer="Lucien Shui"

COPY . /app

WORKDIR /app

RUN pip -i https://mirrors.aliyun.com/pypi/simple/ install -r /app/requirements.txt

CMD ["python", "main.py"]
