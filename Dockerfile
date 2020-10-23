FROM python:3
WORKDIR /Users/Agustin/Documents/Cloud 
RUN pip install psycopg2
RUN pip install kaggle
RUN pip install pandas
Run pip install SQLAlchemy
COPY ./kaggle.json /root/.kaggle/kaggle.json
RUN kaggle datasets download -d rtatman/lego-database
RUN apt install unzip
RUN unzip lego-database.zip
COPY ./csvetl.py /Users/Agustin/Documents/Cloud
CMD ["python3","csvetl.py"]
