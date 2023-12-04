afile=open("/Users/nikhiljosephmartin/Desktop/data.txt",'r')
data=(afile.read())
print(data)
lines=data.split()
wd1=input('Element to be seareched in file:')
count=0
for i in lines:
    if(i==wd1):
        count+=1
print("Occurence of string",wd1,"in the textfile is:",count)


