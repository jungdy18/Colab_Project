#-*-coding:utf-8  
#한글 입력을 위한 정의

import win32gui 
import win32ui
#윈도우 핸들을 찾기 위한 라이브러리
#pip install pypiwin32
#anconda환경이라면 conda install -c anaconda pywin32
from PIL import Image
#이미지저장을 위한 라이브러리
#pip install pillow

from ctypes import windll
#윈도우 dll사용을 위한 라이브러리

hwndname ='Windows Media Player'
hwnd = win32gui.FindWindow(None, hwndname)
if hwnd >=1:
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer('RGB',(bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    
if result ==1: 
    #성공적으로 윈도우 값을 가져왔다면
    im.save("test.png")
    #이미지저장