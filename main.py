# coding: utf-8

# !/usr/bin/env python
# coding: utf-8

import time

from loguru import logger
from wxbot import *

from flask import Flask, jsonify, request, current_app
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import wx
import itchat

app = Flask(__name__)


@app.route('/s', methods=['get'])
def test_calculation():
    return 'Tools Running!'


@app.route('/wx_login', methods=['get'])
def get_wx_login():
    print('')


@app.route('/wx_friend_info', methods=['get'])
def get_wx_friend_info():
    wx.get_friend_info()


@app.route('/text_reply', methods=['get'])
def send_text_reply():
    itchat.auto_login()
    wx.text_reply()


@app.route('/douyin_video/', methods=['get'])
def get_douyin_video():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def is_odd(n):
        return n % 2 == 0
    print(list(filter(is_odd(), a)))
    import uuid
    from time import sleep
    share = request.values.get("share")

    pat = '(https://v.douyin.com/.*?/)'
    pat1 = '(//www.douyin.com/.*? type)'
    txt = requests.get('https://www.douyin.com/video/7040062228699172134')
    url = re.compile(pat).findall(share)[0]
    url2 = "https://www.douyin.com/video/7040062228699172134"

    chrome_driver = r"C:\Program Files\chromedriver\chromedriver.exe"
    chrome_driver2 = r"C:\Program Files\chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver)
    driver2 = webdriver.Chrome(executable_path=chrome_driver)
    driver.get(url)
    driver2.get(url2)
    driver.refresh()
    driver2.refresh()
    time.sleep(3)
    ActionChains.context_click()
    element_close1 = driver.find_element_by_class_name('verify-bar-close--icon')
    element_close2 = driver2.find_element_by_class_name('verify-bar-close--icon')
    element_close1.click()
    element_video = driver.find_element_by_class_name('xg-video-container')
    elements = driver.find_elements_by_xpath('//video/source')
    # 2.循环遍历出每一条搜索结果的标题
    for i, t in enumerate(elements):
        print(t.text)
        print(i)
        element = driver.find_element_by_link_text(t.text)
        element.click()
        sleep(3)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3904.108 Safari/537.36'
    }

    r = requests.get(url, headers=headers, allow_redirects=False)
    # 通过分享的抖音视频地址去解析出视频重定向之后的真实地址（此地址无水印）

    playurl = r.headers['location']
    video = requests.get(url=playurl, headers=headers)
    file_name = str(uuid.uuid1)
    file = r'C:\Users\joea\Desktop\PycharmProjects\tools\video' + file_name + '.mp4'
    with open(file, 'wb')as file:
        file.write(video.content)
        file.close()
        print("===>视频下载完成！")


@app.route('/video', methods=['get'])
def get_douyin():
    share = input("请输入你要去水印的抖音短视频链接：")
    pat = '(https://v.douyin.com/.*?/)'
    url = re.compile(pat).findall(share)[0]  # 正则匹配分享链接
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3904.108 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    pat = 'playAddr: "(.*?)",'
    play = re.compile(pat).findall(r.text)[0].replace("playwm", "play")
    headers = {
        'user-agent': 'Android',
    }
    r = requests.get(play, headers=headers, allow_redirects=False)
    playurl = r.headers['location']

    # 自定义文件名保存短视频
    name = input("===>正在下载保存视频,请输入视频名称：")
    video = requests.get(url=playurl, headers=headers)
    with open(name + ".mp4", 'wb')as file:
        file.write(video.content)
        file.close()
        print("===>视频下载完成！")

    # 完事后退出程序
    input("===>press enter key to exit!")


@app.route('/api/DataCollection/SubmitCalcTask/<int:task_id>', methods=['post'])
def submit(task_id):
    time.sleep(2)
    response = requests.post(
        'http://127.0.0.1:9090/api/v1/hook/status' + '/' + str(task_id) + '/' + str(7),
        headers={"Content-Type": "application/json; charset=UTF-8"}
    )
    response = {'code': str(response.status_code), 'message': 'success'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=21427)
