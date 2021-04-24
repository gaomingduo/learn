# encoding=utf-8
# @time   :2020/5/9 17:52
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :ClipboardUtil.py
# @explain:封装剪辑板

import win32clipboard as w
import win32con
import time


class Clipboard(object):
    # 模拟windows设置剪贴板
    # 读取剪贴板
    @staticmethod
    def getText():
        # 打开剪贴板
        w.OpenClipboard()
        time.sleep(1)
        # 获取剪贴板中的数据
        d = w.GetClipboardData(win32con.CF_TEXT)
        # 关闭剪贴板
        w.CloseClipboard()
        time.sleep(1)
        # 返回剪贴板数据给调用者
        return d

    # 设置剪贴板内容
    @staticmethod
    def setText(aString):
        # 打开剪贴板
        w.OpenClipboard()
        time.sleep(1)
        # 清空剪贴板
        w.EmptyClipboard()
        time.sleep(1)
        # 将数据aString写入剪贴板
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
        time.sleep(1)
        # 关闭剪贴板
        w.CloseClipboard()
        time.sleep(1)
