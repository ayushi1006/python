#Program 1) print numbers which are divisible by 7 and multiple of 5, b/w range 1500 and 2700.
print("Numbers which are divisible by 7 and multiple of 5: \n")
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i,end=' ')
print("\n")

#Program 2) count no. of even and odd no's from a series
start=int(input("Enter start range"))
end=int(input("Enter end range"))
count_even=0
count_odd=0
for i in range(start,end+1):
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("Even no. count:",count_even)
print("Odd no. count:",count_odd)

#Program 3) Fibonacci series b/w 0 to 50
a=0
b=1
print(a, b,end=" ")
for i in range(2,50):
    c=a+b
    a=b
    b=c
    if c<50:
        print(c,end=" ")
print("\n")

#Program 4) Reverse word
word=input("Enter a word")
reverse_word=word[::-1]
print(reverse_word)