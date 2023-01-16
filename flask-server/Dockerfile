FROM python:3

WORKDIR /usr/src/server

COPY requirements.txt /usr/src/server

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "/usr/src/server/server.py" ]