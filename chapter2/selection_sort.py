# Inplace selection sort 
def selectionSort(A):
    for i in range(len(A)):
        min_index =  i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j

        A[i], A[min_index] = A[min_index], A[i]
    print(A)

def main():
    A = [7, 4, 3, 5, 2, 1, 6]
    selectionSort(A)

if __name__ == "__main__":
    main()
