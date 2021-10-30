import sys
# Dictionary to create multiple buttons
values = {"1.click photo" : "1",
         "2.capture video" : "2",
         "3.upload photo" : "3",
         "4.upload video" : "4",
         }

def option():
	n = int(input())
	if(0<n<5): print(n)
	else: 
		print("wrong input")
		m = str(input("try again or exit:(y/n)"))
		if(m =='y'or'Y'): option()
		# if(m=='n'or'N'): sys.exit()
		else: quit()
#program is starting from here 
print("select option:\n**********************")

for i in values:
	print(i)
option()
