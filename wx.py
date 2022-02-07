
# -*- coding: utf-8 -*-
"""
微信好友性别及位置信息
"""

#导入模块
from wxpy import Bot
import itchat
from wxbot import *

'''Q
微信机器人登录有3种模式，
(1)极简模式:robot = Bot()
(2)终端模式:robot = Bot(console_qr=True)
(3)缓存模式(可保持登录状态):robot = Bot(cache_path=True)
'''
def get_friend_info():
    # 初始化机器人，选择缓存模式（扫码）登录
    robot = Bot(cache_path=True)

    # 获取好友信息
    robot.chats()
    # robot.mps()#获取微信公众号信息

    # 获取好友的统计信息
    Friends = robot.friends()
    print(Friends.stats_text())


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    itchat.send('Hello, filehelper', toUserName='filehelper')
    return msg.text
