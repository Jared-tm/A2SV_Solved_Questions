class FrequencyTracker:

    def __init__(self):
        self.count = {}
        self.freq = {}

    def add(self, number: int) -> None:
        old_count = self.count.get(number, 0)

        if old_count > 0:
            self.freq[old_count] -= 1

        new_count = old_count + 1
        self.count[number] = new_count
        self.freq[new_count] = self.freq.get(new_count, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number not in self.count:
            return

        old_count = self.count[number]
        self.freq[old_count] -= 1
        new_count = old_count - 1

        if new_count == 0:
            del self.count[number]
        else:
            self.count[number] = new_count
            self.freq[new_count] = self.freq.get(new_count, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq.get(frequency, 0) > 0



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
