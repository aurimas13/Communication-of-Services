FROM python:3.10.5-slim-buster
WORKDIR /ServicesCommunication/EventPropagator
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /ServicesCommunication/EventPropagator
CMD ["python", "propagate.py"]