from sys import path
import sys
from lib import WindowsBox
import urllib.request, os, sys

def DirCreate(cwd, path):
    run = os.path.join(cwd, path.split('/')[0])
    try: os.mkdir(run)
    except: pass
    if path != path.replace(path.split('/')[0]+'/', ''):
        DirCreate(run, path.replace(path.split('/')[0]+'/', ''))
    return None
def resource(requestfile, cwd):
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
        file = job[0].split('/')[len(job[0].split('/'))- 1]
        path = job[0].replace('/'+file, '')
        DirCreate(cwd, path)
        if not os.path.isfile(cwd+'/'+path+'/'+file): urllib.request.urlretrieve(job[1], filename= path+'/'+file)
def existent(path):
    if os.path.isfile(path):
        return path
    else:
        WindowsBox.error(path+" not found", 'File Error')
        return ''