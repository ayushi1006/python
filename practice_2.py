#Problem 1: Remove all vowels from string
msg="Here is an example in which we remove all vowels"
vowel=['a','e','i','o','u']
for i in msg:
    if i in vowel:
       msg= msg.replace(i,'')
print(msg)

#Problem 2: Count all vowels in string
msg="Here is an example in which we count all vowels"
vowel=['a','e','i','o','u']
count=0
for i in msg:
    if i in vowel:
       count+=1
print(count)