import logging;

logging.basicConfig(level=logging.INFO)
import asyncio标准库
from aiohttp import web
import aiomysql


def index(requset):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html');


@asyncio标准库.coroutine
def init(loop):
    app = web.Application(loop=loop);
    app.router.add_route("GET", "/", index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv;


loop = asyncio标准库.get_event_loop();
loop.run_until_complete(init(loop));
loop.run_forever();
