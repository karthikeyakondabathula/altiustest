#Solution based on in-place insertion of new elements into the window and deletition
#of elements with reference to original array order to optimally update the window
#while keeping it sorted for finding median easily.

#Bisect module provides methods to efficiently search, insert elements into a sorted array 
import bisect

#Input for Value of Window Size
k = int(input())
#Input Array
a = list(map(int, input().split()))
#Len of Input array
n = len(a)

#Error handling
if k==0:
    print("Please enter a valid window size")
elif n==0:
    print("Please enter a valid Input Array")

#to store the output
ans = []



#Initial Case - Manual Handling
frame = a[:k]
frame.sort()
mid = k//2

ans.append(frame[mid])


#Main Logic to insert new element into frame via binary insertion method using
#insort method by bisect and removal of outgoing element with reference to original
#array for an optimal insertion and deletion of elements into the window
for i in range(k, n):
    frame.remove(a[i-k])
    bisect.insort(frame,a[i])
    ans.append(frame[mid])

#Print Output
print(ans)


# Sample Input:
# 3
# 1 3 -1 -3 5 3 6 7
# Sample Output:
# [1, -1, -1, 3, 5, 6]

