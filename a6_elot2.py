class ELot(Spot):
    def __init__(self, station, status):
        super().__init__()
        self.station = station
        self.status = "Available"
        self.durations = []

    def __str__(self):
        return f"{super().__str__()} | Station: {self.station.name} | Status: {self.status}"

    def update(self, new_status: str):
        self.status = new_status

    def charge(self, card: Card, ev: EV, duration: int):
        if card.credit >= ev.charge_rate * duration:
            card.credit -= ev.charge_rate * duration
            self.durations.append(duration)
            self.update("Occupied")
            return True
        else:
            return False