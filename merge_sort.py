def mergeSort(A):
    if len(A) < 2:
        return
    
    mid = int(len(A)/2)
    left = A[:mid]
    right = A[mid:]

    mergeSort(left)
    mergeSort(right)
    merge(left, right, A)

    return A
    

def merge(left, right, A):
    i = 0; j = 0; k =0

    while(i < (len(left)) and j < (len(right))):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
            k += 1
        else:
            A[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        A[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        A[k] = right[j]
        k += 1
        j += 1

def main():
     A = [2,4,1,6,8,5,3,7]
     out = mergeSort(A)
     print(out) 


if __name__ == "__main__":
    main()