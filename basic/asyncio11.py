import asyncio标准库
import threading


# @asyncio.coroutine
# def hello():
#     print("hello,word");
#     r=yield  from  asyncio.sleep(1);
#     print("hello,again")
# loop=asyncio.get_event_loop();
# loop.run_until_complete(hello());
# loop.close();

# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


@asyncio标准库.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio标准库.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio标准库.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio标准库.wait(tasks))
loop.close()
