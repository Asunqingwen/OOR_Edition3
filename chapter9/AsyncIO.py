# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 0008 15:46
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: AsyncIO.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
# @WebSite : labixiaoxin.me
import asyncio
import random


async def random_sleep(counter):
    delay = random.random() * 5
    print("{} sleeps for {:.2f} seconds".format(counter, delay))
    await asyncio.sleep(delay)
    print("{} awakens".format(counter))


async def five_sleepers():
    print("Creating five tasks")
    tasks = [asyncio.get_event_loop().create_task(random_sleep(i)) for i in range(5)]
    print("Sleeping after starting five tasks")
    await asyncio.sleep(2)
    print("Waking and waiting for five tasks")
    await asyncio.gather(*tasks)  


asyncio.get_event_loop().run_until_complete(five_sleepers())
