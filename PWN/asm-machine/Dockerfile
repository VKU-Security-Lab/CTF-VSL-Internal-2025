FROM ubuntu:latest

RUN apt-get update && apt-get install socat -y && apt-get install -y nasm && apt-get install python3 -y && apt-get install binutils -y

WORKDIR /app

COPY src/main.py .
COPY src/flag.txt /
COPY entry.sh .

RUN chmod +x entry.sh
RUN chmod 444 /flag.txt

CMD ["./entry.sh"]