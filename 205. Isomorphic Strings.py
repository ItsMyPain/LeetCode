def pupa():
    s = 'badc'
    t = 'baba'
    a = {}
    for i in range(len(s)):
        if s[i] in a:
            if t[i] != a[s[i]]:
                return False
        elif t[i] in a.values():
            return False
        else:
            a[s[i]] = t[i]
    return True


def pupa2():
    s = 'title'
    t = 'title'
    print(map(s.index, s) is map(t.index, t))

pupa2()