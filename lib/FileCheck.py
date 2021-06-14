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
        path = cwd + '/' + job[0]
        if not os.path.isfile(path): urllib.request.urlretrieve(job[1], path)