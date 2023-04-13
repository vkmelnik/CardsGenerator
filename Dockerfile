FROM python:3.8-slim-buster

COPY . .

WORKDIR /src

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=main.py

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
