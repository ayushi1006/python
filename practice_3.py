# program 1) WAP to create a list of 50 prime no.
prime=[]
for i in range(1,400):
    if len(prime)<50:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            prime.append(i)
print("Length of prime no's list:",len(prime))
print(prime)

# program 2) WAP to create list of name and then remove names that contain 'a' or 'o' char.
name=[]
updated_list=[]
for i in range(1,6):
    input_name=input()
    name.append(input_name) 
print("Names:",name)
for i in name:
    if 'a' in i:
        updated_list.append(i)
    elif 'o' in i:
        updated_list.append(i)
    else:
        pass
print("updated_list:",updated_list)

# program 3) WAP to create a nested list using user input, the length of list depend upon the user.
inner_list=[]
outer_list_limit=int(input())
inner_list_limit=int(input())
for i in range(1,outer_list_limit):
    outer_list=[]
    for i in range(1,inner_list_limit):
        data=int(input())
        inner_list.append(data)
    outer_list.append(inner_list)
print("Nested list:",outer_list)

# progrram 4) WAP to print all armstrong numbers till 100000.
armstrong=[]
for i in range(1,100001):
    original_num=i
    s=0
    while(i>0):
        r=i%10
        s=s+r*r*r
        i=i//10
    if original_num==s:
        armstrong.append(original_num)
print("armstrong list:",armstrong)

#program 5) WAP to generate a list of cricketers entered by user only if the first letter of the name is capital, the size will depend upon user.
names=[]
length=int(input("Enter size of list"))
for i in range(1,length+1):
    a=input()
    if a[0].isupper():
        names.append(a)
    else:
        pass
print(names) 