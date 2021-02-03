FROM python:alpine

LABEL maintainer="Lucien Shui"

COPY requirements.txt /app/requirements.txt
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /app/requirements.txt
WORKDIR /app

CMD ["python", "main.py"]
