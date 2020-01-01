# def consumer():
#     r = "";
#     while True:
#         n = yield r;
#         # 发现这是两句废代码
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = "299k";
#
#
# def produce(c):
#     c.send(None);
#     n = 0;
#     while n < 5:
#         n = n + 1;
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n);
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close();
#
#
# c = consumer();
# produce(c)
from asyncio标准库 import coroutines


def consumer():
    r = "";
    while True:
        m = yield r;
        if not m:
            return;
        print("消费了%s" % m);
        r = "200k";


def produce(c):
    num = 0;
    next(c);
    while num < 5:
        num = num + 1;
        print("生产了%s" % num);
        x = c.send(num);
        print("消费返回值%s" % x);
    c.close();
    print("生产完毕")


c = consumer();
produce(c)