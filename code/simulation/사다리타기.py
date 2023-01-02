def sol(n:int, ladder:list):
    ans = [chr(ord('A')+i) for i in range(n)]

    for hori in ladder:
        for s in hori:
            ans[s-1], ans[s] = ans[s], ans[s-1]

    return ans;
    

# ladder =[[1, 3], [2, 4], [1, 4]] n=5
# ladder = [[1,3,5], [1,3,6], [2,4]] n = 7
# ladder =[[1, 5], [2, 4, 7], [1, 5, 7], [2, 5, 7]] n=8
ladder = [[1, 5, 8, 10], [2, 4, 7], [1, 5, 7, 9, 11], [2, 5, 7, 10], [3, 6, 8, 11]] 
n=12
ans = sol(n, ladder)
print(ans)