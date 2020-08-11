#Regretation program that sum all digit from a file.
import re
fh=open("1.txt")

sum1=0

a=re.findall('[0-9]+',fh.read())	
	
			
#print(a1)
print("\n\n",a)
for b in a:
		sum1=sum1+int(b)	
	
	
print(sum1)


