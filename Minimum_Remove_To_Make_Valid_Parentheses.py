def minRemoveToMakeItValid(s: str) -> str:
    # we either have surplace of "(" or ")
    # if extra ")" skip it
    # if extra "(" we remove them at end, how?
    count = 0
    res = []
    for c in s:
        if c == '(':
            res.append(c)
            count += 1
        elif c == ")" and count > 0:
            res.append(c)
            count -= 1
        elif c != ")":
            res.append(c)

    filtered = []
    for c in res[::-1]:
        if c == '(' and count > 0:
            count -= 1
        else:
            filtered.append(c)
    return "".join(filtered[::-1])


if __name__ == '__main__':

    string = ")lee(t(co)de)("

    print(minRemoveToMakeItValid(string))



