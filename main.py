# YOUR CODE HERE

def summation (lst1,lst2,oper):
    lst1=[]
    lst2=[]
    cal_list=[]
    n=int(input())
    for i in range(n):
        a=int(input())
        lst1.append(a)
    for i in range(n):
        b=int(input())
        lst2.append(b)
    for i in range(n):
        c=lst1[i]+lst2[i]
        cal_list.append(c)
    print (cal_list)
    update_list= oper(cal_list)
    return update_list
def find_min_max (update_list):
    
    find_min=min(update_list)
    find_max=max(update_list)

    return find_min,find_max
lst1=[]
lst2=[]

print(summation(lst1,lst2,find_min_max))
