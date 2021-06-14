import win32con, win32ui

def error(message, title):
    win32ui.MessageBox(
        message, 
        title, 
        win32con.MB_ICONERROR
    )
def info(message, title):
    win32ui.MessageBox(
        message, 
        title,
        win32con.MB_ICONINFORMATION
    )