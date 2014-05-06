import urllib.request

url = 'http://ned.ipac.caltech.edu/cgi-bin/objsearch?search_type=Obj_id&objid=4757810&objname=1&img_stamp=YES&hconst=73.0&omegam=0.27&omegav=0.73&corr_z=1'
book = urllib.request.urlopen(url)
lines = book.readlines()
book.close()

index = 0
for line in lines:
    if 'm-M' in line:
        print(index,line)
    index+=1

