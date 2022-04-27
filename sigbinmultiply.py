#binary-multiplication
print("Enter 1 for binary and 0 for decimal input")
#to check if the input is in decimal form  or binary form
x=int(input())
if(x==1):
    #enter the binary equivalent of multiplicand and multiplier
    a=input()
    q=input()
else:
    #enter the decimal equivalent of multiplicand and multiplier
    a=format(int(input()),"b")
    q=format(int(input()),"b")
#Initialzing the flag value to distinguish the diff cases in  multiplication
flag=-1
if(int(a,2)<0 and  int(q,2)<0):
    flag=0
elif(int(a,2)>0 and  int(q,2)>0):
    flag=1
else:
    flag=2
#since the multiplicand muliplier must have equal number of digits adding 0's using zfill() method
if len(a)<len(q):
    a=a.zfill(len(q))
else:
     q=q.zfill(len(a))
#initializing the sc count to length of the multiplicand
sc=len(a)
#initializing the value of E to zero
E="0"
#storing the q value in Q for calculation purpose
Q=q
print("Multiplicand",a)
print("Multiplier",q)
#initalizing the A register to zero
A=""
for i in range(0,len(a)):
      A+='0'
print("A:",A,"Q:",q)
#the main logic of the program
#IF qn=1 we add multiplicand to A and perform SHL EAQ
#ELSE we just perform SHL EAQ 
#slicing method in python is used to peform SHIFT LEFT operations
while(sc!=0):
    print("SC:",sc)
    sc=sc-1
    if(Q[-1]=="1"):
          print("Since Qn=1 we add Multiplicand",a," AND A ",A)
          result = ''
          carry = 0
          for i in range(len(a)-1, -1, -1):
              r = carry
              if A[i]=='1':
                  r+=1
              else:
                  r+=0
              if a[i]=='1':
                  r+=1
              else:
                  r+=0
              if r%2==1:
                   result = '1' + result
              else:
                   result = '0' + result
              if r<2:
                   carry = 0
              else:
                   carry = 1
          print("carry:",carry," store the value in E")
          E=str(carry)
          A=str(result)
          print("After adding perform Shift Right EAQ")
          st=" "
          string=E+A+Q
          for i in range(0,len(string)-1):
              if(i==0):
                  st+=E
                  E="0"
              else:
                  st+=string[i]
          A=st[1:(len(a)+1)]
          Q=st[len(a)+1:len(st)]
          print("After performing  Shift Right  ","E=", E ,"  A=",A,"  Q=",Q)
          print("-"*75)
    else:
            print("Since Qn=0 we perform only Shift Right ","E=", E ,"  A=",A,"  Q=",Q)
            string=E+A+Q
            st=" "
            for i in range(0,len(string)-1):
                 if(i==0):
                    st+=E
                    E="0"    
                 else:
                    st+=string[i]
            A=st[1:(len(a)+1)]
            Q=st[len(a)+1:len(st)]
            print("After performing  Shift Right  ","E=", E ,"  A=",A,"  Q=",Q)
            print("-"*75) 
#storing the answer in the Answer variable which is the concatenation of A+Q
Answer=A+Q
#case1: if any one of the multiplicand or multiplier is negative we simply take the 2's complement of the answer
#other cases just print the answer
if flag==2:
   #logic to find 2's complement of the given binary number
   n=len(Answer)
   print("n: ",n)
   i =n-1
   while(i >= 0):
       if (Answer[i] =="1"):
            break
       i+=-1
   dup=Answer[0:i]
   first_half=""
   for k in dup:
       if k=="1":
           first_half+="0"
       else:
           first_half+="1"
   final_answer=first_half+Answer[i:n]
   print("final answer stored in AQ register ::",final_answer);       
else:
   print("final answer stored in AQ register ::",Answer)
               
          


        

