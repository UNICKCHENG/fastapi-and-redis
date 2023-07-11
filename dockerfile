FROM python:3.10-slim

WORKDIR /app

COPY app ./app
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]