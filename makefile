BIN := flannMatcher

all: $(BIN).cpp
	g++ $(BIN).cpp -o $(BIN) `pkg-config --cflags --libs opencv`

clean:
	rm -rf $(BIN) tags

remove:
	rm -rf source/
	rm -rf targets/
