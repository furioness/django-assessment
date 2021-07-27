FROM python:3.9

WORKDIR /app

COPY entrypoint.sh .

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Code checks
# RUN black --check --extend-exclude "migrations|staticfiles" .
# RUN flake8

ENTRYPOINT ["bash", "entrypoint.sh"]
