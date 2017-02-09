from inspect import isgenerator

def min(*args, **kwargs):
    def empty_f(arg):
        return arg
    key = kwargs.get("key", empty_f)
    args = args if len(args) > 1 else args[0]
    for arg in args:
        min = arg
        break
    for arg in args:
        if key(arg) < key(min):
            min = arg
    return min

def max(*args, **kwargs):
    def empty_f(arg):
        return arg

    key = kwargs.get("key", empty_f)
    args = args if len(args) > 1 else args[0]
    max = args[0] if hasattr(args, '__getitem__') else args.next()
    for arg in args:
        if key(arg) < key(max):
            max = arg
    return max

def test(*args, **kwargs):
    args = args if len(args) > 1 else args[0]
    max = args[0] if hasattr(args, '__getitem__') else args.next()
    print max
    for i in args:
        if i > max:
            max = i
    return max

print min({1,2,3})