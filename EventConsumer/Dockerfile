# Simple docker file for Communication-of-services program
#
# Created by Aurimas A. Nausedas on 07/24/22.
# Updated by Aurimas A. Nausedas on 07/25/22.
# Updated by Aurimas A. Nausedas on 07/26/22.

FROM python:3.10.5-slim-buster
WORKDIR /ServicesCommunication/EventConsumer
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /ServicesCommunication/EventConsumer
CMD ["python", "main.py"]
