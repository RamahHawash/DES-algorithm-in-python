
print("enter the key")
i=0
key=[]
while i<10:
      user_x = input("")
      x = int(user_x) 
      key.append(x)
      i+=1 
print("key :")     
print(key)
k1=[]
k1.append(key[2])
k1.append(key[4])
k1.append(key[1])
k1.append(key[6])
k1.append(key[3])
k1.append(key[9])
k1.append(key[0])
k1.append(key[8])
k1.append(key[7])
k1.append(key[5])
print("key after 1st per : ")
print(k1)
k1l=[]
k1l.append(k1[1])
k1l.append(k1[2])
k1l.append(k1[3])
k1l.append(k1[4])
k1l.append(k1[0])
k1r=[]
k1r.append(k1[6])
k1r.append(k1[7])
k1r.append(k1[8])
k1r.append(k1[9])
k1r.append(k1[5])
k11=[]
k1[0]=k1l[0]
k1[1]=k1l[1]
k1[2]=k1l[2]
k1[3]=k1l[3]
k1[4]=k1l[4]
k1[5]=k1r[0]
k1[6]=k1r[1]
k1[7]=k1r[2]
k1[8]=k1r[3]
k1[9]=k1r[4]
print("key after shft by 1:")
print(k1)
k11.append(k1[5])
k11.append(k1[2])
k11.append(k1[6])
k11.append(k1[3])
k11.append(k1[7])
k11.append(k1[4])
k11.append(k1[9])
k11.append(k1[8])
print("k1 :")
print(k11)
k1[0]=k1l[2]
k1[1]=k1l[3]
k1[2]=k1l[4]
k1[3]=k1l[0]
k1[4]=k1l[1]
k1[5]=k1r[2]
k1[6]=k1r[3]
k1[7]=k1r[4]
k1[8]=k1r[0]
k1[9]=k1r[1]
print("key after shft by 2:")
print(k1)
k22=[]

k22.append(k1[5])
k22.append(k1[2])
k22.append(k1[6])
k22.append(k1[3])
k22.append(k1[7])
k22.append(k1[4])
k22.append(k1[9])
k22.append(k1[8])
print("k2 :")
print(k22)
# end of k1 k2

print("enter 1 if you want encryption and 2 if you want decryption :")

user_x2 = input("")
x2 = int(user_x2) 
if x2 ==1 :
    print("encryption :")
    print("enter the plain text:")
    plain=[]
    j=0
    while j<8:
      user_x3 = input("")
      x3 = int(user_x3) 
      plain.append(x3)
      j+=1
    print ("plain:") 
    print(plain)
    plain1=[]
    plain1.append(plain[1])
    plain1.append(plain[5])
    plain1.append(plain[2])
    plain1.append(plain[0])
    plain1.append(plain[3])
    plain1.append(plain[7])
    plain1.append(plain[4])
    plain1.append(plain[6])
    print("plain after 1st per :")
    print(plain1)
    plainl=[]
    plainl.append(plain1[0])
    plainl.append(plain1[1])
    plainl.append(plain1[2])
    plainl.append(plain1[3])
    
    plainr=[]
    plainr.append(plain1[4])
    plainr.append(plain1[5])
    plainr.append(plain1[6])
    plainr.append(plain1[7])
    print("plain right side")
    print(plainr)
    print("plain left side")
    print(plainl)
    plainr1=[]
    plainr1.append(plainr[3])
    plainr1.append(plainr[0])
    plainr1.append(plainr[1])
    plainr1.append(plainr[2])
    plainr1.append(plainr[1])
    plainr1.append(plainr[2])
    plainr1.append(plainr[3])
    plainr1.append(plainr[0])
    print("plain right side after per + exp")
    print(plainr1)
    xor=[]
    if plainr1[0]==k11[0]:
       xor.append(0)
    else :
       xor.append(1)
    if plainr1[1]==k11[1]:
       xor.append(0)
    else :
       xor.append(1) 
    if plainr1[2]==k11[2]:
       xor.append(0)
    else :
       xor.append(1)
    if plainr1[3]==k11[3]:
       xor.append(0)
    else :
       xor.append(1)
    if plainr1[4]==k11[4]:
       xor.append(0)
    else :
       xor.append(1)
    if plainr1[5]==k11[5]:
       xor.append(0)
    else :
       xor.append(1)
    if plainr1[6]==k11[6]:
       xor.append(0)
    else :
       xor.append(1)
    if plainr1[7]==k11[7]:
       xor.append(0)
    else :
       xor.append(1)
    print("the result of xor:")
    print(xor)
    s0=[
       [1,0,3,2],
       [3,2,1,0],
       [0,2,1,3],
       [3,1,3,2],
       ]
    s1=[
       [0,1,2,3],
       [2,0,1,3],
       [3,0,1,0],
       [2,1,0,3],
       ]
    s0r=0
    s0c=0
    s1r=0
    s1c=0
   
    if xor[0]==1 and xor[3]==1:
       s0r=3
    if xor[0]==1 and xor[3]==0:
       s0r=2

    if xor[0]==0 and xor[3]==0:
       s0r=0

    if xor[0]==0 and xor[3]==1:
       s0r=1

    if xor[1]==1 and xor[2]==1:
       s0c=3

    if xor[1]==1 and xor[2]==0:
       s0c=2

    if xor[1]==0 and xor[2]==0:
       s0c=0

    if xor[1]==0 and xor[2]==1:
       s0c=1

    if xor[4]==1 and xor[7]==1:
       s1r=3

    if xor[4]==1 and xor[7]==0:
       s1r=2

    if xor[4]==0 and xor[7]==0:
       s1r=0

    if xor[4]==0 and xor[7]==1:
       s1r=1

    if xor[5]==1 and xor[6]==1:
       s1c=3

    if xor[5]==1 and xor[6]==0:
       
       s1c=2

    if xor[5]==0 and xor[6]==0:
       s1c=0

    if xor[5]==0 and xor[6]==1:
       s1c=1

    
    s02=0
    s12=0
    s02=s0[s0r] [s0c]
    s12=s1[s1r] [s1c]
    print("s0 ")
    print(s02)
    print("s1 ")
    print(s12) 
    b1 = bin(s02)[2:].zfill(2)
    b2 = bin(s12)[2:].zfill(2)
    
    digits = [int(digit) for digit in str(b1)]
    digits2 = [int(digit) for digit in str(b2)]
    
    s = digits + digits2
    print("s0+s1")
    print(s)
    s1=[]
    s1.append(s[1])
    s1.append(s[3])
    s1.append(s[2])
    s1.append(s[0])
    print("after per")
    print(s1)
    xor2=[]
    if(plainl[0]==s1[0]):
       xor2.append(0)
    else :
       xor2.append(1)
    if(plainl[1]==s1[1]):
       xor2.append(0)
    else :
       xor2.append(1)
    if(plainl[2]==s1[2]):
       xor2.append(0)
    else :
       xor2.append(1)
    if(plainl[3]==s1[3]):
       xor2.append(0)
    else :
       xor2.append(1)
    print("left side xor s")
    print(xor2)
    print("output of first stage:")
    
    stage1=plainr+xor2
    print("the first stage")
    print(stage1)
    ###3###
   
    plainl2=[]
    plainl2.append(stage1[0])
    plainl2.append(stage1[1])
    plainl2.append(stage1[2])
    plainl2.append(stage1[3])
    
    plainr2=[]
    plainr2.append(stage1[4])
    plainr2.append(stage1[5])
    plainr2.append(stage1[6])
    plainr2.append(stage1[7])
    print("plain 2 right side")
    print(plainr2)
    print("plain 2 left side")
    print(plainl2)
    plainr12=[]
    plainr12.append(plainr2[3])
    plainr12.append(plainr2[0])
    plainr12.append(plainr2[1])
    plainr12.append(plainr2[2])
    plainr12.append(plainr2[1])
    plainr12.append(plainr2[2])
    plainr12.append(plainr2[3])
    plainr12.append(plainr2[0])
    print("plain right side after per + exp")
    print(plainr12)
    xor22=[]
    if plainr12[0]==k22[0]:
       xor22.append(0)
    else :
       xor22.append(1)
    if plainr12[1]==k22[1]:
       xor22.append(0)
    else :
       xor22.append(1) 
    if plainr12[2]==k22[2]:
       xor22.append(0)
    else :
       xor22.append(1)
    if plainr12[3]==k22[3]:
       xor22.append(0)
    else :
       xor22.append(1)
    if plainr12[4]==k22[4]:
       xor22.append(0)
    else :
       xor22.append(1)
    if plainr12[5]==k22[5]:
       xor22.append(0)
    else :
       xor22.append(1)
    if plainr12[6]==k22[6]:
       xor22.append(0)
    else :
       xor22.append(1)
    if plainr12[7]==k22[7]:
       xor22.append(0)
    else :
       xor22.append(1)
    print("the result of xor:")
    print(xor22)
    s00=[
       [1,0,3,2],
       [3,2,1,0],
       [0,2,1,3],
       [3,1,3,2],
       ]
    s11=[
       [0,1,2,3],
       [2,0,1,3],
       [3,0,1,0],
       [2,1,0,3],
       ]
    s00r=0
    s00c=0
    s11r=0
    s11c=0
   
    if xor22[0]==1 and xor22[3]==1:
       s00r=3
    if xor22[0]==1 and xor22[3]==0:
       s00r=2

    if xor22[0]==0 and xor22[3]==0:
       s00r=0

    if xor22[0]==0 and xor22[3]==1:
       s001r=1

    if xor22[1]==1 and xor22[2]==1:
       s00c=3

    if xor22[1]==1 and xor22[2]==0:
       s00c=2

    if xor22[1]==0 and xor22[2]==0:
       s00c=0

    if xor22[1]==0 and xor22[2]==1:
       s00c=1

    if xor22[4]==1 and xor22[7]==1:
       s11r=3

    if xor22[4]==1 and xor22[7]==0:
       s11r=2

    if xor22[4]==0 and xor22[7]==0:
       s11r=0

    if xor22[4]==0 and xor22[7]==1:
       s11r=1

    if xor22[5]==1 and xor22[6]==1:
       s11c=3

    if xor22[5]==1 and xor22[6]==0:
       
       s11c=2

    if xor22[5]==0 and xor22[6]==0:
       s11c=0

    if xor22[5]==0 and xor22[6]==1:
       s11c=1

    
    s002=0
    s112=0
    s002=s00[s00r] [s00c]
    s112=s11[s11r] [s11c]
  
    b11 = bin(s002)[2:].zfill(2)
    b22 = bin(s112)[2:].zfill(2)
  
    ###
    digitss = [int(digit) for digit in str(b11)]
    digitss2 = [int(digit) for digit in str(b22)]
    
    ss = digitss + digitss2
    print("s0+s1")
    print(ss)
    
    s11=[]
    s11.append(ss[1])
    s11.append(ss[3])
    s11.append(ss[2])
    s11.append(ss[0])
    print(s11)
    xor222=[]
    if(plainl2[0]==s11[0]):
       xor222.append(0)
    else :
       xor222.append(1)
    if(plainl2[1]==s11[1]):
       xor222.append(0)
    else :
       xor222.append(1)
    if(plainl2[2]==s11[2]):
       xor222.append(0)
    else :
       xor222.append(1)
    if(plainl2[3]==s11[3]):
       xor222.append(0)
    else :
       xor222.append(1)
    print("lefr side xor s")
    print(xor222)
    stage11=xor222+plainr2
    stage2=[]
    stage2.append(stage11[3])
    stage2.append(stage11[0])
    stage2.append(stage11[2])
    stage2.append(stage11[4])
    stage2.append(stage11[6])
    stage2.append(stage11[1])
    stage2.append(stage11[7])
    stage2.append(stage11[5])
    print("the cipher text")
    print(stage2)
    #end of encyrption
    
else :
     print("decryption :")
     print("enter the cirher text:")
     plain=[]
     j=0
     while j<8:
       user_x3 = input("")
       x3 = int(user_x3) 
       plain.append(x3)
       j+=1
     print ("cipher:") 
     print(plain)
     plain1=[]
     plain1.append(plain[1])
     plain1.append(plain[5])
     plain1.append(plain[2])
     plain1.append(plain[0])
     plain1.append(plain[3])
     plain1.append(plain[7])
     plain1.append(plain[4])
     plain1.append(plain[6])
     print("plain after 1st per :")
     print(plain1)
     plainl=[]
     plainl.append(plain1[0])
     plainl.append(plain1[1])
     plainl.append(plain1[2])
     plainl.append(plain1[3])
    
     plainr=[]
     plainr.append(plain1[4])
     plainr.append(plain1[5])
     plainr.append(plain1[6])
     plainr.append(plain1[7])
     print("cipher right side")
     print(plainr)
     print("cipher left side")
     print(plainl)
     plainr1=[]
     plainr1.append(plainr[3])
     plainr1.append(plainr[0])
     plainr1.append(plainr[1])
     plainr1.append(plainr[2])
     plainr1.append(plainr[1])
     plainr1.append(plainr[2])
     plainr1.append(plainr[3])
     plainr1.append(plainr[0])
     print("cipher right side after per + exp")
     print(plainr1)
     xor=[]
     if plainr1[0]==k22[0]:
        xor.append(0)
     else :
        xor.append(1)
     if plainr1[1]==k22[1]:
        xor.append(0)
     else :
        xor.append(1) 
     if plainr1[2]==k22[2]:
        xor.append(0)
     else :
        xor.append(1)
     if plainr1[3]==k22[3]:
        xor.append(0)
     else :
        xor.append(1)
     if plainr1[4]==k22[4]:
       xor.append(0)
     else :
        xor.append(1)
     if plainr1[5]==k22[5]:
        xor.append(0)
     else :
        xor.append(1)
     if plainr1[6]==k22[6]:
        xor.append(0)
     else :
        xor.append(1)
     if plainr1[7]==k22[7]:
        xor.append(0)
     else :
        xor.append(1)
     print("the result of xor:")
     print(xor)
     s0=[
       [1,0,3,2],
       [3,2,1,0],
       [0,2,1,3],
       [3,1,3,2],
       ]
     s1=[
       [0,1,2,3],
       [2,0,1,3],
       [3,0,1,0],
       [2,1,0,3],
       ]
     s0r=0
     s0c=0
     s1r=0
     s1c=0
   
     if xor[0]==1 and xor[3]==1:
        s0r=3
     if xor[0]==1 and xor[3]==0:
        s0r=2

     if xor[0]==0 and xor[3]==0:
        s0r=0

     if xor[0]==0 and xor[3]==1:
        s0r=1

     if xor[1]==1 and xor[2]==1:
        s0c=3

     if xor[1]==1 and xor[2]==0:
        s0c=2

     if xor[1]==0 and xor[2]==0:
        s0c=0

     if xor[1]==0 and xor[2]==1:
        s0c=1

     if xor[4]==1 and xor[7]==1:
        s1r=3
        print(s1r)

     if xor[4]==1 and xor[7]==0:
        s1r=2

     if xor[4]==0 and xor[7]==0:
        s1r=0

     if xor[4]==0 and xor[7]==1:
        s1r=1

     if xor[5]==1 and xor[6]==1:
        s1c=3

     if xor[5]==1 and xor[6]==0:
       
        s1c=2

     if xor[5]==0 and xor[6]==0:
        s1c=0

     if xor[5]==0 and xor[6]==1:
        s1c=1

    
     s02=0
     s12=0
     s02=s0[s0r] [s0c]
     s12=s1[s1r] [s1c]
      
     b1 = bin(s02)[2:].zfill(2)
     b2 = bin(s12)[2:].zfill(2)
  
     digits = [int(digit) for digit in str(b1)]
     digits2 = [int(digit) for digit in str(b2)]
   
     s = digits + digits2
     print("s0+s1")
     print(s)
     s1=[]
     s1.append(s[1])
     s1.append(s[3])
     s1.append(s[2])
     s1.append(s[0])
     print(s1)
     xor2=[]
     if(plainl[0]==s1[0]):
        xor2.append(0)
     else :
        xor2.append(1)
     if(plainl[1]==s1[1]):
       xor2.append(0)
     else :
        xor2.append(1)
     if(plainl[2]==s1[2]):
        xor2.append(0)
     else :
        xor2.append(1)
     if(plainl[3]==s1[3]):
        xor2.append(0)
     else :
        xor2.append(1)
     print("lefr side xor s")
     print(xor2)
     print("output of first stage:")
     stage1=plainr+xor2
     print(stage1)
    ###3###
     plainl2=[]
     plainl2.append(stage1[0])
     plainl2.append(stage1[1])
     plainl2.append(stage1[2])
     plainl2.append(stage1[3])
    
     plainr2=[]
     plainr2.append(stage1[4])
     plainr2.append(stage1[5])
     plainr2.append(stage1[6])
     plainr2.append(stage1[7])
     print("cipher 2 right side")
     print(plainr2)
     print("cipher 2 left side")
     print(plainl2)
     plainr12=[]
     plainr12.append(plainr2[3])
     plainr12.append(plainr2[0])
     plainr12.append(plainr2[1])
     plainr12.append(plainr2[2])
     plainr12.append(plainr2[1])
     plainr12.append(plainr2[2])
     plainr12.append(plainr2[3])
     plainr12.append(plainr2[0])
     print("cipher right side after per + exp")
     print(plainr12)
     xor22=[]
     if plainr12[0]==k11[0]:
        xor22.append(0)
     else :
        xor22.append(1)
     if plainr12[1]==k11[1]:
        xor22.append(0)
     else :
        xor22.append(1) 
     if plainr12[2]==k11[2]:
        xor22.append(0)
     else :
        xor22.append(1)
     if plainr12[3]==k11[3]:
        xor22.append(0)
     else :
        xor22.append(1)
     if plainr12[4]==k11[4]:
        xor22.append(0)
     else :
        xor22.append(1)
     if plainr12[5]==k11[5]:
        xor22.append(0)
     else :
        xor22.append(1)
     if plainr12[6]==k11[6]:
        xor22.append(0)
     else :
        xor22.append(1)
     if plainr12[7]==k11[7]:
        xor22.append(0)
     else :
        xor22.append(1)
     print("the result of xor:")
     print(xor22)
     s00=[
       [1,0,3,2],
       [3,2,1,0],
       [0,2,1,3],
       [3,1,3,2],
       ]
     s11=[
       [0,1,2,3],
       [2,0,1,3],
       [3,0,1,0],
       [2,1,0,3],
       ]
     s00r=0
     s00c=0
     s11r=0
     s11c=0
   
     if xor22[0]==1 and xor22[3]==1:
        s00r=3
     if xor22[0]==1 and xor22[3]==0:
        s00r=2

     if xor22[0]==0 and xor22[3]==0:
        s00r=0

     if xor22[0]==0 and xor22[3]==1:
        s001r=1

     if xor22[1]==1 and xor22[2]==1:
        s00c=3
 
     if xor22[1]==1 and xor22[2]==0:
        s00c=2

     if xor22[1]==0 and xor22[2]==0:
        s00c=0

     if xor22[1]==0 and xor22[2]==1:
        s00c=1

     if xor22[4]==1 and xor22[7]==1:
        s11r=3

     if xor22[4]==1 and xor22[7]==0:
        s11r=2

     if xor22[4]==0 and xor22[7]==0:
        s11r=0

     if xor22[4]==0 and xor22[7]==1:
        s11r=1

     if xor22[5]==1 and xor22[6]==1:
        s11c=3

     if xor22[5]==1 and xor22[6]==0:
        
        s11c=2

     if xor22[5]==0 and xor22[6]==0:
        s11c=0

     if xor22[5]==0 and xor22[6]==1:
        s11c=1

    
     s002=0
     s112=0
     s002=s00[s00r] [s00c]
     s112=s11[s11r] [s11c]
     
     b11 = bin(s002)[2:].zfill(2)
     b22 = bin(s112)[2:].zfill(2)
   
    ###
     digitss = [int(digit) for digit in str(b11)]
     digitss2 = [int(digit) for digit in str(b22)]
    
     ss = digitss + digitss2
     print("s0+s1")
     print(ss)
    
     s11=[]
     s11.append(ss[1])
     s11.append(ss[3])
     s11.append(ss[2])
     s11.append(ss[0])
     print(s11)
     xor222=[]
     if(plainl2[0]==s11[0]):
        xor222.append(0)
     else :
        xor222.append(1)
     if(plainl2[1]==s11[1]):
        xor222.append(0)
     else :
        xor222.append(1)
     if(plainl2[2]==s11[2]):
        xor222.append(0)
     else :
        xor222.append(1)
     if(plainl2[3]==s11[3]):
         xor222.append(0)
     else :
        xor222.append(1)
     print("lefr side xor s")
     print(xor222)
     stage11=xor222+plainr2
     stage2=[]
     stage2.append(stage11[3])
     stage2.append(stage11[0])
     stage2.append(stage11[2])
     stage2.append(stage11[4])
     stage2.append(stage11[6])
     stage2.append(stage11[1])
     stage2.append(stage11[7])
     stage2.append(stage11[5])
     print("the plain text")
     print(stage2)
   