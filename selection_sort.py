# Selection Sort implementation with Python

class SelectionSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        for i in range(len(self.array)):
            min_indx = i
            min_current = self.array[i]
            for j in range(i + 1, len(self.array)):
                # updated index everytime smaller value appears
                if self.array[j] < self.array[min_indx]:
                    min_indx = j

            # swap values until second loop is done
            # in order to swap only the smallest value
            # in that way, array doesn't wrongly updated
            self.array[i] = self.array[min_indx]
            self.array[min_indx] = min_current

        return self.array


selection = SelectionSort([2, 5, 1, 4, 8, 10, 3, 6, 8])
print(selection.sort())
