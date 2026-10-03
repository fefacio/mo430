CXX = g++
CXXFLAGS = -O3

NUMDS_SRC = NuMDS/NuMDS.cpp
NUMDS_BIN = NuMDS/NuMDS

DEMDS_SRC = DemDS/DemDS.cpp
DEMDS_BIN = DemDS/DemDS

.PHONY: all clean numds demds

all: numds demds

numds: $(NUMDS_BIN)

demds: $(DEMDS_BIN)

$(NUMDS_BIN): $(NUMDS_SRC)
	$(CXX) $(CXXFLAGS) $(NUMDS_SRC) -o $(NUMDS_BIN)

$(DEMDS_BIN): $(DEMDS_SRC)
	$(CXX) -std=c++11 $(CXXFLAGS) $(DEMDS_SRC) -o $(DEMDS_BIN)

clean:
	rm -f $(NUMDS_BIN) $(DEMDS_BIN)