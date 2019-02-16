from tkinter import *
import urllib.request

finallist=[]
templ=[]

window =Tk()
btn=Button(window,text="EXECUTE",fg='blue')
btn.place(x=80,y=100)
window.title('POLICE SOS')
window.mainloop()
while True:
 cdone= urllib.request.urlopen('https://sosburla.herokuapp.com/polsos')
 xdone=str(cdone.read())
 print(xdone)
 if(xdone!=""):
    xdone=xdone.split(':')
    xdone.pop()
    for x in xdone:
        templ+=[x.split(" ")]
    finallist+=templ
    templ=[]


        
