tests = ["aaabbbc","aabbbacd"]

def collapse(level):
    stack = []
    for l in level:
        if not stack:
            stack.append([l,1])
        else:
            [lastLetter, count] = stack.pop()
            if count
