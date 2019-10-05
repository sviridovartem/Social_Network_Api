FROM python:3.6

RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi

COPY ./friendship /opt/friendship
COPY ./group /opt/group
COPY ./news /opt/news
COPY ./Social_Network_Api /opt/Social_Network_Api
COPY ./subscription /opt/subscription
COPY ./news /opt/news
COPY ./news /opt/Social_Network_Api

RUN pip3 install -r /opt/Social_Network_Api/requirements.txt

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

EXPOSE 8000

CMD ["uwsgi", "--ini", "/opt/app/uwsgi.ini"]