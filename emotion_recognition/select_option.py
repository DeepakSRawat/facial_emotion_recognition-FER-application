from capture_video import cap_v
from click_photo import clk_phto
#list to create multiple buttons
values = ["1.click photo",
         "2.capture video",
         "3.upload photo",
         "4.upload video",
         ]

def option():
	n = int(input())
	if(0<n<5): 
		print(n)
		if(n==1):clk_phto()
		if(n==2):cap_v()
		

	else:
	    print("wrong input") 
	    
#program is starting from here 
print("select option:\n**********************")

#print values from list 
for i in values:
	print(i)
# calling option:
option()