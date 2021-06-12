FROM python:3.9
LABEL maintainer="NaveenKumar Namachivayam"

COPY . /pythonapp
WORKDIR /pythonapp
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
