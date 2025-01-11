FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y socat libc6 gcc gdb && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /chall

COPY ./src/entry.sh /entry.sh
COPY ./src/chall .
COPY ./src/flag.txt .

RUN sed -i 's/\r//' /entry.sh

RUN chmod 444 flag.txt && \
    chmod +x /entry.sh && \
    chmod +x /chall/chall

CMD ["/bin/sh", "/entry.sh"]
