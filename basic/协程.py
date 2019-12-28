def consumer():
    r = "";
    while True:
        n = yield r;
        # 发现这是两句废代码
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = "299k";


def produce(c):
    c.send(None);
    n = 0;
    while n < 5:
        n = n + 1;
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n);
        print('[PRODUCER] Consumer return: %s' % r)
    c.close();


c = consumer();
produce(c)
