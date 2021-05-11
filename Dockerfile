FROM ubuntu:18.04
ARG HTTP_API


RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
ARG HTTP_API
ENV HTTP_API=${HTTP_API}

WORKDIR /bot

# ENTRYPOINT ["/bin/sh", "-c", "/bin/bash"]
ENTRYPOINT [ "python3", "main.py" ]