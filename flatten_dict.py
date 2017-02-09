"""
Function to flatten nested dictioary:
input: {'name': {'first': 'ksenia', 'last': 'andr'}}
output: {'name/first': 'ksenia', 'name/last': 'andr'}
"""


def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result

dic = {'name': {'first': 'ksenia', 'last': 'andr'}}
print flatten(dic)
