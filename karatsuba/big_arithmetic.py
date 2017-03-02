import sys

def big_arithmetic(a, b, op):
    if str(op) is "+":
       return big_add(a,b)
    elif str(op) is "-":
       return  big_sub(a,b)
    else:
        return -1



def big_sub(a,b):
    #print "sub\na,b= ",a,b
    if a is b:
        return[0]

    a_shift=0
    b_shift=0
    b_len = len(b)
    while a[0]==0 and len(a) > 1 :
        a=a[1:]
        a_shift+=1

    while b[0] == 0 and b_len>1 :
        b=b[1:]
        b_shift+=1
        b_len-=1


    b_len=len(b)
    len_dif= len(a) - b_len
    ans=a

    for num in range(0,b_len):
        ans[num+len_dif]-=b[num]
        temp=len_dif+num
        while ans[temp]<0:
            ans[temp]+=10
            temp-=1
            ans[temp] -= 1
    #if ans[0]==0:
        #ans=ans[1:]
    #if len(ans) == b_len + b_shift and len(ans) == len(a) + a_shift:
    #    return ans

    #elif b_len + b_shift > len(a) + a_shift:
     #   ans = [0] * (len(ans) - b_len + b_shift) + ans

    #else:
    #    ans = [0] * (len(ans) - len(a) + a_shift) + ans


    return ans


def big_add(a,b):
  #  print "add\na,b=",a,b
    a_shift=0
    b_shift=0
    b_len = len(b) # b length will always be <= a length


    carry = False


    while a[0]==0 and len(a) > 1 :
        a=a[1:]
        a_shift+=1

    while b[0] == 0 and b_len>1 :
        b=b[1:]
        b_shift+=1
        b_len-=1

    ans = a
    len_dif = len(a) - b_len
  #  print "length difference=",len_dif
    if len_dif < 0:
        ans= big_add(b,a)

    else:
        for num in range(b_len-1,-1,-1):
            ans[num+len_dif] += b[num]
            if carry:
                ans[num+len_dif] += 1
                carry = False
            if ans[num+len_dif] > 9:
                ans[num+len_dif] -= 10
                carry = True

        while carry:
            if len_dif == 0:
                ans= [1] + ans
                carry=False
            else:
                ans[len_dif-1]+=1
                if ans[len_dif-1]<10:
                    carry= False
                else:
                    ans[len_dif-1]-=10
                    len_dif-=1
   # print ans

#    if len(ans) == b_len+b_shift and len(ans)== len(a)+a_shift:
#        return ans

#    elif b_len+b_shift > len(a)+a_shift:
#        ans = [0]* (len(ans)-b_len+b_shift) + ans

#    else:
#        ans = [0] * (len(ans) - len(a) + a_shift) + ans



    return ans










#READ INPUT
#numbers_a = [int(x) for x in sys.stdin.readline().split()]
#numbers_b = [int(x) for x in sys.stdin.readline().split()]
#operation = (sys.stdin.readline())[0]

#result = big_arithmetic(numbers_a, numbers_b, operation)
#while result[0] == 0 and len(result)>1:
#    result= result[1:]
#print ' '.join(str(x) for x in result)