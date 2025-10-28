class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {}
        self.journey_data = {}     

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = (stationName, t)
    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStn, startTime = self.check_in_data.pop(id)
        route = (startStn, stationName)
        totalTime, count = self.journey_data.get(route, (0, 0))
        self.journey_data[route] = (totalTime + t - startTime, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, count = self.journey_data[(startStation, endStation)]
        return totalTime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)