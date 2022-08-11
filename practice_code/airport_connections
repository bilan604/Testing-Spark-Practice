# The hardest problem on AlgoExpert as of 2020: "Airport Connections"
# https://www.youtube.com/watch?v=qz9tKlF431k&t=125s


# Given a list of unique airport names,
# a list of one way flights from an airport to another airport,
# and a starting airport;
# --------------------
# FIND the minimum number of routes that must be added so that a passenger can
# reach any other aiport from the starting airport


class Airport(object):
    def __init__(self, name):
        self.name = name
        self.connectsTo = []
        self.connectsFrom = []


def airport_connections(airports, routes, startingAirport):
    # hashmap of airports
    dd = {airport: Airport(airport) for airport in airports}
    
    # adding edges
    for route in routes:
        dd[route[0]].connectsTo.append(route[1])
        dd[route[1]].connectsFrom.append(route[0])
    
    clusterCount = sum([1 if not airport.connectsFrom else 0 for airport in dd.values()])
    
    if dd[startingAirport].connectsFrom:
        return clusterCount
    return clusterCount - 1


# ~10 minute finish