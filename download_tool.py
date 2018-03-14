import urllib.request
from urllib.error import HTTPError
import os
i=1
k=1
currdir=os.getcwd()
print(currdir)
while i<301:
        os.makedirs(currdir+"/"+str(i))
        os.chdir(currdir+"/"+str(i))
        try:     
            while k<43:
                if k<10 and i<10:
                    img = urllib.request.urlopen("http://img1.unicomics.com/comics/hellblazer/hellblazer-00"+str(i)+"//0"+str(k)+".jpg").read()
                    out = open(str(i)+"-"+str(k)+".jpg", "wb")
                    out.write(img)
                    out.close
                elif k>=10 and i<10:
                    img = urllib.request.urlopen("http://img1.unicomics.com/comics/hellblazer/hellblazer-00"+str(i)+"//"+str(k)+".jpg").read()
                    out = open(str(i)+"-"+str(k)+".jpg", "wb")
                    out.write(img)
                    out.close
                elif k<10 and i<100: 
                    img = urllib.request.urlopen("http://img1.unicomics.com/comics/hellblazer/hellblazer-0"+str(i)+"//0"+str(k)+".jpg").read()
                    out = open(str(i)+"-"+str(k)+".jpg", "wb")
                    out.write(img)
                    out.close
                elif k>=10 and i<100:
                    img = urllib.request.urlopen("http://img1.unicomics.com/comics/hellblazer/hellblazer-0"+str(i)+"//"+str(k)+".jpg").read()
                    out = open(str(i)+"-"+str(k)+".jpg", "wb")
                    out.write(img)
                    out.close
                elif k<10 and i>=100:
                    img = urllib.request.urlopen("http://img1.unicomics.com/comics/hellblazer/hellblazer-"+str(i)+"//0"+str(k)+".jpg").read()
                    out = open(str(i)+"-"+str(k)+".jpg", "wb")
                    out.write(img)
                    out.close
                elif k>=10 and i>=100:
                    img = urllib.request.urlopen("http://img1.unicomics.com/comics/hellblazer/hellblazer-"+str(i)+"//"+str(k)+".jpg").read()
                    out = open(str(i)+"-"+str(k)+".jpg", "wb")
                    out.write(img)
                    out.close
                k=k+1
                print ("k="+str(k))
            k=1        
            i=i+1
            print ("i="+str(i))
        except HTTPError as e:
            if e.code == 404:
                k=1
                i=i+1
