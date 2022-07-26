FROM python:3.10.5-slim-buster
WORKDIR /ServicesCommunication/EventConsumer
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /ServicesCommunication/EventConsumer
CMD ["python", "main.py"]