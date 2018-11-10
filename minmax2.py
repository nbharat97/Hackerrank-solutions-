#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
#Then print the respective minimum and maximum values as a single line of two space-separated long integers.

a = []
n = 5
sum = []
for i in range(0,n):
    a.append(int(input()))
    sum.append(int(0))


def miniMaxSum(arr):
    for i in range(0,n):
        for j in range(0,n):

            if (i!=j):
                sum[i] = sum[i] + arr[j]
    mini = min(sum)

    maxi = max(sum)

    print(mini,maxi)


miniMaxSum(a)
