FROM python:3.8

RUN pip install fastapi

RUN pip install uvicorn

RUN pip install pymongo

EXPOSE 27017

COPY ./APP /app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "27017" ]