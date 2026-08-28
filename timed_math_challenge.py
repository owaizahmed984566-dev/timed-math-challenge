import random
import time
print('Timed Math Challenge')
print('Enter Your Name :',end=' ')
name=input()
print('Do you want to challenge the math, '+str(name)+' :(yes 0r no)')
user=input()
user=user.lower()

if user=='yes':
    print('Welcome '+str(name))
    print('You have to complete the problems whithin 30 seconds')
    print('To Start Challenge Press "Enter"')
    start=input()
    print('------------------------------')

    l=["+","-","*"]

    start_time=time.time()
    
    i=1
    while i<=7:
       a=random.randint(1,10)
       b=random.randint(1,10)
       op=random.choice(l)
       
       expression_1=str(a)+str(op)+str(b)
       answer_1=eval(expression_1)
       print('# Problem ',i,': ',a,op,b,'=',end=' ')    
       inpt_1=int(input())
       while inpt_1!=answer_1:
          print('Wrong Answer')
          print('# Problem ',i,': ',a,op,b,'=',end=' ')    
          inpt=int(input())
          if inpt==answer_1:
            break
       i=i+1

    
    while i<=10:
       intgers=[2,4,6,8,10,12,14,16,18,20]
       n=random.choice(intgers)
       print('# Problem ',i,': ',n,'/ 2 =',end=' ')
       inpt_2=int(input())
       expression_2=(n/2)
       while expression_2!=inpt_2:
         print('Wrong Answer')
         print('# Problem ',i,': ',n,'/ 2 =',end=' ')
         inpt_2=int(input())
         if n==inpt_2:
            break
       i=i+1 
        
    end_time=time.time()
    
    total_time= end_time - start_time
    print('------------------------------')
    if total_time<= 30:
     print('Nice Work you have completed the challenge in '+str(total_time)+' seconds')
    else:
       print('You faild the challenge ,because you have completed the challenge in '+str(total_time)+' seconds, try again') 
    print('Thank You')
    print('Have a Good Day '+str(name))

elif user=='no':
    print('Quit The Challenge')
    print('Thank You')
    print('Have a Good Day '+str(name))

else:
   print(name,'you had not answerd')


           
        


        




    
    
    


        
    

    












