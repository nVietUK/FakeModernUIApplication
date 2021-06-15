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
def download(file, cwd, path, link):
    DirCreate(cwd, path)
    if not os.path.isfile(cwd+'/'+path+'/'+file): urllib.request.urlretrieve(link, filename= path+'/'+file)
    return cwd+'/'+path+'/'+file
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
        download(file, cwd, path, job[1])
def existent(path, cwd, resource):
    if os.path.isfile(path):
        return path
    else:
        WindowsBox.error(path+" not found", 'File Error')
        return download(
            resource.split(' ')[0].split('/')[len(resource.split(' ')[0].split('/'))- 1], 
            cwd, 
            resource.split(' ')[0].replace('/'+resource.split(' ')[0].split('/')[len(resource.split(' ')[0].split('/'))- 1], ''), 
            resource.split(' ')[1]
        )