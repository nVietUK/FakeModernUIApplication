import urllib.request, os

def check(requestfile, cwd):
    filename, headers = urllib.request.urlretrieve(
        requestfile, 
        filename= cwd + "/Request.file"
    )
    File = open(filename)
    run = True
    while run:
        job = File.readline().split(' ').rstrip("\n")
        path = cwd + '/' + job[0]
        if not os.path.isfile(path): urllib.request.urlretrieve(job[1], path)