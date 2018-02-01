def findTriplets(arr, n):
    found = False
    arr.sort()  # sorting elements of the array
    for i in range(0, n - 1):
        left = i + 1 # initializing left and right
        right = n - 1
        x = arr[i]
        while (left < right):
            if (x + arr[left] + arr[right] == 0):
                print([x, arr[left], arr[right]])# print elements if sum is zero
                left += 1
                right -= 1
                found = True
            elif (x + arr[left] + arr[right] < 0):# If sum of three elements is lessthan zero then increment in left
                left += 1
            else: # if sum is greater than zero than decrement in right side
                right -= 1
    if (found == False):
        print(" No Triplet Found")

a = input("Enter the list of numbers:")
arr = list(map(int,a.split()))
n = len(arr)
findTriplets(arr, n)