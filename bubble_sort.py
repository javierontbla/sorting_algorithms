# Bubble Sort implementation with Python

class BubbleSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        for num in range(1, len(self.array)):
            for num in range(1, len(self.array)):
                if self.array[num - 1] > self.array[num]:
                    temp = self.array[num - 1]
                    self.array[num - 1] = self.array[num]
                    self.array[num] = temp

        return self.array
