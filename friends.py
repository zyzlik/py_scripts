"""
We have class Friend, it can have some friends, it can add friend.
We have to write method to check if the suggested friend in the connection net
of the object.
If suggested friend is a friend of the object or a friend of friend of the object etc,
the should return True for this method. Otherwise, False.
Example:
f1 = Friend('abc')
f2 = Friend('thj')
f3 = Friend('bnm')
f4 = Friend('bng')
f5 = Friend('bnu')
f1.add_friend(f2)
f1.add_friend(f3)
f3.add_friend(f4)
f2.is_connection(f3) is True
f2.is_connection(f4) is True
f2.is_connection(f5) is False
"""


class Friend(object):

    def __init__(self, email):
        self.email = email
        self.friends = set()

    def add_friend(self, friend):
        self.friends.add(friend)

    def get_friends(self):
        return self.friends

    def is_connection(self, friend):
        net = set()
        changed_size = True
        net.update(self.get_friends())
        while changed_size:
            len_net = len(net)
            tmp_net = set()
            for f in net:
                tmp_net.update(f.get_friends())
            net.update(tmp_net)
            if len_net == len(net):
                changed_size = False
        return friend in net

f1 = Friend('abc')
f2 = Friend('thj')
f3 = Friend('bnm')
f4 = Friend('ttt')
f5 = Friend('ksu')
f6 = Friend('lonely')

f1.add_friend(f2)
f2.add_friend(f3)
f3.add_friend(f4)
f4.add_friend(f5)
print f1.is_connection(f6)
