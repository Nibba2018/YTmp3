import os
import sys


try:
        while True:
                l=[]
                ch=int(input('''Enter Your choice:
1.Auto download with url.txt file
2.Manual download via pasting links
3.Quit
:'''))
                if ch==1:
                        f=open("url.txt",'r')
                        while True:
                                line=f.readline()
                                if not line:
                                        break
                                else:
                                        l.append(line)
                        f.close()


                elif ch==2:
                        n=int(input("Enter the no. of song/s u want to download:"))

                        for i in range(0,n):
                                print("Enter {} Song URL:".format(i+1))
                                b=input()
                                l.append(b)
                else:
                        break

                for i in range(0,len(l)):
                        print("{} Song/s left to download".format(len(l)-i))
                        s="youtube-dl.exe --extract-audio --audio-format mp3 -o './YTsongs/%(title)s.%(ext)s' " + l[i]
                        os.system(s)

                print("----------------Done!!------------------------")
                del l
        
except:
        print(sys.exc_info())
        os.system("youtube-dl.exe -U")
input("Press Enter to Quit Program.....")
