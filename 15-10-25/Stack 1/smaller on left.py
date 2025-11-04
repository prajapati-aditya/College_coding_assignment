def Smallestonleft(arr, n):
    stack = []
    res = []

    for num in arr:
        while stack and stack[-1] >= num:
            stack.pop()

        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])

        stack.append(num)

    return res

n = 5
arr = [2, 3, 4, 5, 1]

print(Smallestonleft(arr,n))