class DigitalCounter:

    def __init__(self, start=0, end=100, current=None):
        if start < end:
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start

        if current is None or current < start or current > end:
            self.current = self.start
        else:
            self.current = current

    def increase(self):
        if self.current < self.end:
            self.current += 1
        else:
            self.current = self.start

    def get_current_value(self):
        return self.current


if __name__ == "__main__":

    d = DigitalCounter(current=70)
    d.increase()
    print(d.get_current_value())

