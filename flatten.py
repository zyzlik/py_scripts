def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if v and isinstance(v, dict):
                stack.append((path + (k,), v))
            elif not v:
                result["/".join((path + (k,)))] = ''
            else:
                result["/".join((path + (k,)))] = v
    print(result)
    return result

flatten({"empty": {}})
