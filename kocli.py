from os import get_terminal_size, system

hline= "─"
vline= "│"
cp1=   "┌"
cp2=   "┐"
cp3=   "└"
cp4=   "┘"
whitespace = " "

def window(name: str,h: int, w: int, xpos: int, ypos: int):
    out = [name, h, w, xpos, ypos]
    lw=w
    lh=h
    lname=name
    if len(name) > lw-2:
        lname=lname[:lw-3]+"┅"
    out.append(cp1+lname+hline*(lw-len(name)-2)+cp2)
    lh-=2
    for x in range(lh):
        out.append(vline+whitespace*(lw-2)+vline)
    out.append(cp3+hline*(lw-2)+cp4)
    return out

    ##list output should be formated as follows:
    ##list[0] - name
    ##list[1] - height
    ##list[2] - width
    ##list[3] - window x position
    ##list[4] - window y position

    ##list[5 to 4+height] - window text 4 unicodes :D

def windowmod(lis: list, value: int, newcontent: str, fullacc: bool = False):
    lh=lis[1]
    lw=lis[2]
    out=lis
    lname=lis[0]
    if value == 0 and fullacc == False:
          
        if len(newcontent) > lw-2:
            lname=newcontent[:lw-3]+"┅"
        else:
            lname=newcontent
        out[5] = cp1+lname+hline*(lw-len(lname)-2)+cp2
        out[0] = newcontent
    elif value==0 and fullacc == True:
        out[0]=newcontent
        out[5]=newcontent
    
    elif value==1:
        newcontent=int(newcontent)
        if lh<newcontent:
            diff=newcontent-lh
            out.pop(4+lh)
            for x in range(diff):
                out.append(vline+whitespace*(lw-2)+vline)
            out.append(cp3+hline*(lw-2)+cp4)
            out[1]=newcontent
        if lh>newcontent:
            diff=lh-newcontent
            for x in range(diff):
                out.pop(lh-x)
            if len(lname) > lw-2:
                oos=lname[:lw-3]+"┅"
            else:
                oos=lname
            out[5] = cp1+oos+hline*(lw-len(oos)-2)+cp2
            
            out[1]=newcontent


    elif value==2:
        newcontent=int(newcontent)
        if lw<newcontent:
            diff=newcontent-lw
            for x in range(lh):
                out[5+x]=str(out[5+x])[:lw-1]
            

            if len(lname) > newcontent-2:
                oos=lname[:newcontent-3]+"┅"
            else:
                oos=lname
            out[5] = cp1+oos+hline*(newcontent-len(oos)-2)+cp2

            for x in range(lh-2):
                out[6+x]=str(out[6+x])+whitespace*diff+vline
            out[4+lh]=str(out[4+lh])+hline*diff+cp4

            out[2] = int(newcontent)


        if lw>newcontent:
            diff=lw-newcontent
            for x in range(lh-2):
                out[6+x]=str(out[6+x])[:lw-(diff+1)]+vline
            out[4+lh]=str(out[4+lh])[:lw-(diff+1)]+cp4

            if len(lname) > newcontent-2:
                oos=lname[:newcontent-3]+"┅"
            else:
                oos=lname
            out[5] = cp1+oos+hline*(newcontent-len(oos)-2)+cp2
            out[2] = int(newcontent)

    elif value==3 or value==4:
        out[value]=int(newcontent)
    
    elif fullacc==True:
        out[value]=newcontent
    elif fullacc==False:
        if value==5 or value==4+lh:
            pass
        else:
            if len(newcontent) > lw:
                newcontent=str(newcontent)[:lw-5]+"..."
            else:
                pass
            out[value]=vline+str(newcontent)[:lw-2]+whitespace*(lw-len(newcontent)-2)+vline
        
    
    return out


##def screenreset():
  ##out=[]
    ##widt=get_terminal_size().columns-10
    ##heigt=get_terminal_size().lines-5
    ##for x in range(heigt):
        ##out.append(hline*widt)
    ##return out
##def screencalc(screen: list, ins: list):



##temporary function - remove l8r
def windowout(inp: list):
      lh=inp[1]
      for x in range(lh):
           print(inp[5+x])



system("cls")
print("enter settings for window xoxoxoxoxo")
a=str(input(print("Enter window name: ")))
b=int(input(print("Enter window height: ")))
c=int(input(print("Enter window width: ")))
x=window(a, b, c, 0, 0)
while True:
    system("cls")
    windowout(x)
    ##print(x)
    vaa=input("Enter value to modify: ")
    nw=input("Enter new value: ")
    windowmod(x, int(vaa), nw)
