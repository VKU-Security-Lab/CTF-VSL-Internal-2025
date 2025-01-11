FROM ubuntu:latest

RUN apt-get update && apt-get install socat libc6 -y && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /chall

COPY src/libpwn .
COPY src/flag.txt .
COPY entry.sh /entry.sh

RUN sed -i 's/\r//' /entry.sh

RUN chmod +x libpwn
RUN chmod 444 flag.txt
RUN chmod +x /entry.sh

CMD ["/entry.sh"]