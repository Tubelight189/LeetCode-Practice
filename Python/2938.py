def minimumSteps(self, s):
    """
    :type s: str
    :rtype: int
    """
    c, one = 0, 0
    for ch in s:
        if ch == '1':
            one += 1
        else:
            c += one
        print(one, c)
    return c