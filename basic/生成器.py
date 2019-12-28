#
# 生成器第一种
g = (x * x for x in range(6))
for x in g:
    print(x)


def odd():
    print("zhw")
    m = yield 1;
    print(m)
    print("xiaozlzi")
    yield 2;
    print("hehhe")
    yield 3;


for x in odd():
    print(x)
