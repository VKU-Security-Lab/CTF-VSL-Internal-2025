FLAGS = -fno-stack-protector -no-pie

all: libpwn

libpwn: main.c
	gcc -o $@ $^ $(FLAGS)