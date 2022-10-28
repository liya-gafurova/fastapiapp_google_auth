FROM python:3.10

RUN pip install --upgrade pip
RUN mkdir app/

COPY fastapi_requirements.txt /app/

WORKDIR /app/

RUN pip install -r fastapi_requirements.txt

COPY . /app/

EXPOSE 8000

RUN ["chmod", "+x", "entrypoint.sh"]

CMD uvicorn main:app --host 0.0.0.0 --port 8000