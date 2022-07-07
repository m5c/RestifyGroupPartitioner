class MaxAverageDiff:

    def __init__(self, averages):
        self.min = min(averages)
        self.max = max(averages)
        self.diff = self.max - self.min

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_diff(self):
        return self.diff
