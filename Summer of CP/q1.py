def palindrome(s):
    n = len(s)
    i=0
    j=n-1

    while(i<j):
        if (s[i]!=s[j]):
            return False
        i+=1
        j-=1
    return True

def patternj(s):
    n = len(s)
    if (n==1 or n==0):
        return True
    if (palindrome(s)):
        return patternj(s[:n//2]) and patternj(s[(n+1)//2:])
    else:
        return False

for _ in range(int(input())):
    s = input()
    if(patternj(s)):
        print("yes")
    else:
        print("no")