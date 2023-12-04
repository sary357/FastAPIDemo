FROM alpine:3.18.5

RUN apk add --update --no-cache python3 py3-pip libffi-dev openssl-dev curl && ln -sf python3 /usr/bin/python && python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools 

WORKDIR /opt

COPY conf /opt/conf
COPY main.py /opt/main.py
COPY start.sh /opt/start.sh
COPY requirements.txt /opt/requirements.txt

RUN pip install -r requirements.txt && mkdir -p /opt/log 
RUN addgroup docker && adduser -S recsysteam -G docker && chown recsysteam:docker -R /opt/* 
USER recsysteam

CMD ["sh", "start.sh"]