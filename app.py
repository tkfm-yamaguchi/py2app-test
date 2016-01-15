#!/usr/bin/python

# icon.py

import wx

def main():
    app = wx.App()

    frame = wx.Frame(None, title='Icon', pos=(350,300))
    frame.SetIcon(wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO))
    frame.Center()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
