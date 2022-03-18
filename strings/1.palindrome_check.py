def isPalindrome(string):
    p1 = 0
    p2 = len(string) - 1
    while p1 <= p2:
        if string[p1] == string[p2]:
            p1 += 1
            p2 -= 1
        else:
            return False
    return True


print(isPalindrome("abcdcba"))
