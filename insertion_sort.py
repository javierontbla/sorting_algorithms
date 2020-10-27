# Insertion Sort implementation with Python

class InsertionSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        i = 0
        while i < len(self.array):
            j = i
            while j > 0 and self.array[j - 1] > self.array[j]:
                temp = self.array[j - 1]
                self.array[j - 1] = self.array[j]
                self.array[j] = temp
                j = j - 1
            i = i + 1

        return self.array
