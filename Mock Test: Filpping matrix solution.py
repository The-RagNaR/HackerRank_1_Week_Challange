q = int(input())
while q > 0:
    q -= 1
    
    n = int(input())
    A = []
    for i in range(2 * n):
        A += [list(map(int, input().split()))]
    
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += max(A[i][j], A[2 * n - 1 - i][j], A[i][2 * n - 1 - j], A[2 * n - 1 - i][2 * n - 1 - j])
    # here create an 2x2 array and get a maximun value from it and repeat for all possible 2x2 array that can be formed from the given input array
    print(ans)