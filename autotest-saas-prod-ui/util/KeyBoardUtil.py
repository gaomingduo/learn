# encoding=utf-8
# @time   :2020/5/9 17:53
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :KeyBoardUtil.py
# @explain:封装模拟键盘按键类

import win32api
import win32con
import time


class KeyboardKeys(object):
    # 模拟键盘按键类
    VK_CODE = {
        'enter': 0x0D,
        'ctrl': 0x11,
        'v': 0x56,
        'esc': 0x1B
    }

    @staticmethod
    def keyDown(keyName):
        # 按下按键
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName], 0, 0, 0)
        time.sleep(1)

    @staticmethod
    def keyUp(keyName):
        # 释放按键
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)

    @staticmethod
    def oneKey(key):
        # 模拟单个按键
        KeyboardKeys.keyDown(key)
        KeyboardKeys.keyUp(key)
        time.sleep(1)

    @staticmethod
    def twoKeys(key1, key2):
        # 模拟两个组合键
        KeyboardKeys.keyDown(key1)
        KeyboardKeys.keyDown(key2)
        KeyboardKeys.keyUp(key2)
        KeyboardKeys.keyUp(key1)
