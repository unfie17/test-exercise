FROM python:3.10.6-alpine3.16
COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]