# Simple docker file for Communication-of-services program
#
# Created by Aurimas A. Nausedas on 07/23/22.

FROM python:3.8.10-slim
RUN pip install typing
RUN pip install python-math
WORKDIR /calculator/calculatorpackage
COPY . .
CMD ["python", "./calculator/calculator.py"]