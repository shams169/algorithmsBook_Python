def insertion_sort(A):
    for i in range(1, len(A)):
        val = A[i]
        hole = i

        while i > 0:
            if A[i-1] > val:
                A[i-1], A[i] = A[i], A[i-1]
                hole = hole -1
            i = i-1
        A[hole] = val
    print(A)


def recursive_insertion_sort(A, n):

    if n <= 1:
        return
    recursive_insertion_sort(A, n-1)
    val = A[n-1]
    hole = n-1
    i = n-1
    while i > 0:
        if A[i-1] > val:
            A[i-1], A[i] = A[i], A[i-1]
            hole = hole -1
        i = i-1
    A[hole] = val

    print(A)


def main():
    A = [2,4,1,6,8,5,3,7]
    #out = insertion_sort(A)
    out = recursive_insertion_sort(A, len(A))

if __name__ == "__main__":
    main()