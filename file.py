
print('Data Processing')
number_of_words = 0
afile=open("/Users/nikhiljosephmartin/Desktop/data.txt",'r')
data=(afile.read())
print(data)
lines=data.split()
number_of_words += len(lines)
print('Number of words',number_of_words)
mylist=['nausea','vomiting','infection','health','The']
print("my list is",mylist)
for i in mylist:
    count=0
    for test in lines:
        if(i==test):
            count+=1
    print("Occurence of the string",i,"is:",count)





