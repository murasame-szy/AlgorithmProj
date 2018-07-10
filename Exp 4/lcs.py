def lcs(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]
    flag = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]
    for i in range(len1):
        for j in range(len2):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                flag[i+1][j+1] = 'eq'
            elif dp[i][j+1] >= dp[i+1][j]:
                dp[i+1][j+1] = dp[i][j+1]
                flag[i+1][j+1] = 'up'
            else:
                dp[i+1][j+1] = dp[i+1][j]
                flag[i+1][j+1] = 'left'
    return dp, flag

def print_lcs(flag, s1, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == 'eq':
        print_lcs(flag, s1, i-1, j-1)
        print(s1[i - 1], end='')
    elif flag[i][j] == 'up':
        print_lcs(flag, s1, i-1, j)
    else:
        print_lcs(flag, s1, i, j-1)

if __name__ == '__main__':
    s1 = input("input string1:  ")
    s2 = input("input string2:  ")
    dp, flag = lcs(s1, s2)
    print('dp:')
    for i in dp:
        print(i)
    print('flag:')
    for j in flag:
        print(j)
    print('最长公共子序列长度为',dp[len(s1)][len(s2)])
    print('最长公共子序列为', end='')
    print_lcs(flag, s1, len(s1), len(s2))