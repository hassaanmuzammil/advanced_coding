s = "abccba"

def countPalindromicSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    dp = []
    n = len(s)
    count = 0
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        dp.append(l)

    # if start == end, then substring is palindrome (length 1 substrings)
    for i in range(n):
        dp[i][i] = True

    # if start + 1 == end, then check for ends (length 2 substrings) 
    for i in range(n-1):
        sub = s[i:i+2]
        if sub[0] == sub[-1]:
            dp[i][i+1] = True
        else:
            dp[i][i+1] = False

    # for everything else, check ends and previous diagonal entry (length > 2 substrings)
    for g in range(2,n):
        for i in range(n-g):
            sub = s[i:i+g+1]
            if sub[0] == sub[-1] and dp[i+1][i+g-1] == True:
                dp[i][i+g] = True
            else:
                dp[i][i+g] = False

    return sum([l.count(True) for l in dp])
  
countPalindromicSubstring(s)

#returns 9
