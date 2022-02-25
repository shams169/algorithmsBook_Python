def bubble_sort(A):

    for i in range(0, len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
    print(A) 
            

def main():
    A = [2,4,1,6,8,5,3,7]
    bubble_sort(A)

if __name__ == "__main__":
    main()