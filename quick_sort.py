# Quick Sort implementation with Python

class QuickSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        def partition(arr, low, high):
            pivot = arr[high]  # last element from arr
            i = low - 1  # indx of smaller element

            for j in range(low, high):
                if arr[j] <= pivot:  # if current is smaller than pivot
                    i = i + 1
                    # swap values only if conditional is True
                    temp_in = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp_in

            # swap values ALWAYS
            temp_out = arr[high]
            arr[high] = arr[i + 1]
            arr[i + 1] = temp_out

            return i + 1

        def quick(arr, low, high):
            if (len(arr) == 1):
                return arr

            elif (low < high):
                p_indx = partition(arr, low, high)  # gets new pivot index

                # recursive
                quick(arr, low, p_indx - 1)
                quick(arr, p_indx + 1, high)

            print(arr)
            return arr

        quick(self.array, 0, len(self.array) - 1)
