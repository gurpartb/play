
CC = g++

test: play
	./play

play: play.o
	$(CC) -o play play.o

play.o: play.cpp
	$(CC) -c play.cpp

test2: dynamic
	./dynamic

dynamic: dynamic.o
	$(CC) -o dynamic  dynamic.o

dynamic.o: dynamic.cpp
	$(CC) -c dynamic.cpp

testprintmatrix: printmatrix
	cat printmatrix.txt | ./printmatrix

printmatrix: printmatrix.o
	$(CC) -o printmatrix printmatrix.o

printmatrix.o: printmatrix.cpp
	$(CC) -c printmatrix.cpp
