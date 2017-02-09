"""
Given the list of prices for shares: iterable
iterable[0] = price for the first day
iterable[1] = price for the second day
etc.
We should find the most profitable way when to buy and to sell
for example, [100, 120, 150, 135, 99] - better to buy by price of 100
and to sell when then price is 150. So, we got 50 as benefit
The function returns max benefit
"""

l = [260, 255, 245, 240, 235]


def max_benefit(iterable):
    min_price = iterable[0]
    max_price = iterable[1]
    max_benefit = max_price - min_price
    for i in range(len(iterable) - 1):
        min_price = iterable[i]
        max_price = max(iterable[i + 1:])
        benefit = max_price - min_price
        if benefit > max_benefit:
            max_benefit = benefit
    if max_benefit > 0:
        return max_benefit
    return -1

print max_benefit(l)
