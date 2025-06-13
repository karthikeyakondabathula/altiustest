#Input for Value of Window Size
k = int(input())
#Input Array
a = list(map(int, input().split()))
#Len of Input array
n = len(a)

#to store the output
ans = []

#Initial Case - Manual Handling using .copy() to avoid reference issues
frame = a[:k]
x = frame.copy()
x.sort()
mid = k//2

ans.append(x[mid])


#Main Logic
for i in range(1, n-k+1):
    frame.pop(0)
    frame.append(a[i+k-1])
    x = frame.copy()
    x.sort()
    ans.append(x[mid])

#Print Output
print(ans)


