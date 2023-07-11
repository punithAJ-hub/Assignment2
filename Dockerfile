FROM python:3.8-slim-buster

WORKDIR /app

COPY app.py app.py

RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install flask
RUN pip install numpy

EXPOSE 5000

CMD ["python3", "-m", "flask","run","--host=0.0.0.0", "--port=5000"]