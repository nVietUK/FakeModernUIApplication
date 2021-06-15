from lib import WindowsBox
import urllib.request, os

def check(requestfile, cwd):
    try:
        filename, headers = urllib.request.urlretrieve(
            requestfile, 
            filename= cwd + "/Request.file"
        )
    except:
        WindowsBox.error('No internet connection', 'File Download Error')
    File = open(filename, 'r')
    run = True
    while run:
        job = File.readline().split(' ')
        if job[0] == '': return
        path = cwd + '\\' + job[0].rstrip("\n")
        os.path.join()
        if not os.path.isfile(path): filename, headers = urllib.request.urlretrieve(job[1], filename= path)