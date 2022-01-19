FROM python:3.8-bullseye
#make a directory for application

WORKDIR /src

#install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copy source code
COPY /src .

#run the application
CMD ["python", "app.py"]