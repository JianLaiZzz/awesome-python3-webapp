import asyncio


async def consumer(n, q):
    print('consumer {}: starting'.format(n))
    while True:
        print('consumer {}: waiting for item'.format(n))
        item = await q.get()
        print('consumer {}: has item {}'.format(n, item))
        if item is None:
            # None is the signal to stop.
            q.task_done()
            break
        else:
            await asyncio.sleep(0.01 * item)
            q.task_done()
    print('consumer {}: ending'.format(n))


async def producer(q, num_workers):
    print('producer: starting')
    # Add some numbers to the queue to simulate jobs
    for i in range(num_workers * 3):
        await q.put(i)
        print('producer: added task {} to the queue'.format(i))
    # Add None entries in the queue
    # to signal the consumers to exit
    print('producer: adding stop signals to the queue')
    for i in range(num_workers):
        await q.put(None)
    print('producer: waiting for queue to empty')
    await q.join()
    print('producer: ending')


async def main(loop, num_consumers):
    # Create the queue with a fixed size so the producer
    # will block until the consumers pull some items out.
    q = asyncio.Queue(maxsize=num_consumers)

    # Scheduled the consumer tasks.
    consumers = [
        loop.create_task(consumer(i, q)) for i in range(num_consumers)
    ]

    # Schedule the producer task.
    prod = [loop.create_task(producer(q, num_consumers))]

    # Wait for all of the coroutines to finish.
    await asyncio.wait(consumers + prod)


event_loop = asyncio.get_event_loop()

try:
    event_loop.run_until_complete(main(event_loop, 2))
finally:
    event_loop.close()

n = 10
buf = []


async def producer(num):
    run_flag = True
    count = 0
    while run_flag:
        t = random.uniform(0.1, 1.2)
        await asyncio.sleep(t)  # 模拟生产时间
        p = chr(random.randint(65, 90))  # 产品是随机生成的大写的英文字母
        if len(buf) < n:
            print('生产者 {} 花费时间 {:.3f} 生成一个产品 {}'.format(num, t, p))
            buf.append(p)  # 加入缓冲区
            print('--------------', buf, '---------------')
        else:
            count += 1
        if count == 5:
            run_flag = False
    print(f'生产者 {num} 退出')


async def consumer(num):
    run_flag = True
    count = 0
    while run_flag:
        t = random.uniform(0.1, 1.2)
        await asyncio.sleep(t)  # 模拟消费时间
        if len(buf) > 0:
            print('消费者 {} 花费时间 {:.3f} 消费一个产品 {}'.format(num, t, buf[0]))
            del buf[0]  # 移出缓冲区
            print('--------------', buf, '---------------')
        else:
            count += 1
        if count == 3:
            run_flag = False
    print(f'消费者 {num} 退出')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # 创建一个事件循环，并设为当前循环
    pros = [loop.create_task(producer(i)) for i in range(3)]  # 生产者事件组
    cons = [loop.create_task(consumer(i)) for i in range(2)]  # 消费者事件组
    tasks = pros + cons
    print(tasks)  # 查看事件列表
    loop.run_until_complete(asyncio.wait(tasks))  # 把事件列表加入到循环中运行，并等待至所有事件运行结束
    print(tasks)  # 再看一次
    loop.close()
