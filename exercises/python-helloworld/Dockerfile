FROM python:3.9
LABEL maintainer="NaveenKumar Namachivayam"

COPY . /pythonapp
WORKDIR /pythonapp
RUN pip install -r exercises/python-helloworld/requirements.txt

CMD [ "python", "app.py" ]
