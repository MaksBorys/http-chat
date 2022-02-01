FROM python:latest

COPY app.py 

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python", "app.py" ]