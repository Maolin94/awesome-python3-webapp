import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

#定义一个请求处理函数，此函数需为协程，从而支持并发访问
async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

#建立服务器应用，持续监听本地9090端口的http请求，对首页“/”进行响应
def init():
    #创建一个应用实例
    app = web.Application()
    #将请求处理函数与对应的http请求对应，添加到路径中
    app.add_routes([web.get('/', index)])
    logging.info('server started at http://127.0.0.1:9090...')
    #启动web应用服务端
    web.run_app(app, host='127.0.0.1', port=9090)

if __name__=="__main__":
    init()    
