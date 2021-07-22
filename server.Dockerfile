FROM python:3.9

WORKDIR /app

COPY entrypoint.sh .

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]
