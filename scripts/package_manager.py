import urllib.request
import urllib.response

#Downloading images from the server
def download_images_from_server(path):
    url = "http://dodgethat.co.uk/"+path
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    resp = resp.read()
    file = open (path,"wb")
    file.write(resp)
    file.close()