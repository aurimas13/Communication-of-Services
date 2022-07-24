# Simple docker file for Communication-of-services program
#
# Created by Aurimas A. Nausedas on 07/23/22.

FROM python:3.10.5-slim-buster
FROM continuumio/miniconda3
WORKDIR /ServicesCommunication
RUN conda install -c conda-forge python-dotenv
RUN conda install -c conda-forge marshmallow
RUN conda install -c anaconda flask
COPY . .
CMD ["python", "propagate.py"]
#CMD ["0"]