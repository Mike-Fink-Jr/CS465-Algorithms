import sys
import big_arithmetic


def grade_school(a,b):
    ans = [i * a[0] for i in b]
    for i in range(len(ans)-1, 0, -1):
        if ans[i] > 9:
            ans[i - 1] += ans[i] / 10
            ans[i] %= 10
    if ans[0] >9:
        ans= [ans[0]/10]+ans
        ans[1]%=10
        #print ans
    return ans

def karatsuba(a, b):


    #shift =max(len(a),len(b))

    while a[0] == 0 and len(a) > 1:
        a = a[1:]
    while b[0] == 0 and len(b) > 1:
        b = b[1:]

    if a is [0] or b is [0]:
        return [0]

    if len(a)!= len(b):
        if len(a)==1:
           return grade_school(a,b)
        if len(b)==1:
            return grade_school(b,a)


        dif= abs(len(a)-len(b))
        if len(a)>len(b):
            b= [0]*dif +b
        else:
           return karatsuba(b,a)


    leng= len(a)

    if  leng == 1:
        if (a[0]*b[0])>9:
            return [  (a[0]*b[0]/10) ,  (a[0]*b[0])%10 ]
        else:
            return [a[0]*b[0]]

    #9 8 9 3 7     8 6 4 1 4
    #6 9 9 4 8     2 8 5 0 7
    a1=a[:leng/2]
    a2=a[(leng/2):]
    b1= b[:leng/2]
    b2=b[(leng/2):]
 #   print "a1/2=", a, a1, a2, "\nb1/2= ", b, b1, b2
    x= karatsuba(a[:leng/2],b[:(leng/2)])
    y= karatsuba(a[(leng/2):],b[(leng/2):])
    t1= big_arithmetic.big_add(a[:leng/2],a[(leng/2):])
    t2= big_arithmetic.big_add(b[:(leng/2)],b[(leng/2):])

    z=karatsuba(t1,t2)

    print "a1/2= ", a, a1, a2, "\nb1/2= ", b, b1, b2
    print "z presub=", z
   # print "z, pre sub= ",t1,t2,z
    z= big_arithmetic.big_sub(z*1,x*1)
    z= big_arithmetic.big_sub(z*1,y*1)

    if leng%2==1:
        leng+=1

    ans =  big_arithmetic.big_add(x+[0]*leng,z+[0]*(leng/2))
   # print "ans pre y=",ans
    ans= big_arithmetic.big_add(ans*1,y*1)
    print "x,y,z" ,x,y,z


    print ans,"\n\n"
    #print "\n"
    while ans[0] == 0 and len(ans) > 1:
        ans = ans[1:]

    return ans


 #15057748070249
# READ INPUT
numbers_a = [int(x) for x in sys.stdin.readline().split()]
numbers_b = [int(x) for x in sys.stdin.readline().split()]

answer = karatsuba(numbers_a, numbers_b)

while answer[0] == 0 and len(answer)>1:
    answer = answer[1:]
print ' '.join(str(x) for x in answer)
