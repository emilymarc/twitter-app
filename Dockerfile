FROM python:3.6

RUN rm -rfv /projetoteste/ && mkdir -p /projetoteste/
WORKDIR /projetoteste/
COPY . .
RUN pip3 install -r requirements.txt && \
    apt-get update && \
CMD python3 twitter-tests.py