FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip 
WORKDIR /app
# ADD requirements.txt requirements.txt
COPY requirements.txt requirements.txt
WORKDIR /app
COPY hello_world.py hello_world.py

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8888

ENTRYPOINT [ "jupyter", "lab" ]
CMD ["--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]
