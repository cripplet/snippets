CC=g++ -std=c++0x
CFLAGS=-c -W -Wall -Wextra -pedantic # -s -O2 -flto -march=native
LDFLAGS=
SOURCES=main.cpp node.cpp channel.cpp content.cpp utils.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=cim

all:		$(SOURCES) $(EXECUTABLE)
$(EXECUTABLE):	$(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@
.cpp.o:
	$(CC) $(CFLAGS) $< -o $@
test:		$(EXECUTABLE)
	./$(EXECUTABLE)
clean:
	rm -rf *o $(EXECUTABLE)
