FROM python:3.10.2

RUN apt-get update

EXPOSE 8085

COPY . ./

RUN pip install -r requirements.txt

CMD uvicorn main:app --reload