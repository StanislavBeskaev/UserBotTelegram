FROM python:3.9.16-slim

COPY . /user_bot
COPY requirements.txt /user_bot
COPY main.py /user_bot

WORKDIR /user_bot

RUN pip install -r requirements.txt

CMD ["python", "main.py"]