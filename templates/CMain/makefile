CC=gcc
CC_FLAGS=-Werror -o
SRC=main.c
LNK=
BIN=main
ARGS=

all: compile run

compile: $(SRC)
	$(CC) $(CC_FLAGS) $(BIN) $(SRC)

run:
	./$(BIN)

clean:
	rm $(BIN)

.PHONY: clean

