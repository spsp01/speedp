

def createimg(imagebase,type,filename):
    imgdata = base64.urlsafe_b64decode(imagebase)
    with open('img/tmp/'+type+'/'+filename+'.jpg', 'wb') as f:
        f.write(imgdata)