import time
clock="clock"
title="title"
wm="nothing"
counter=0
percentage="0%"
time_left="0 minutes"
temperature="0"

dark_blue="2222bb"
blue="5555ff"
dark_green="006600"
green="22bb22"
orange="FFA500"
dark_orange="B17200"
black="000000"
white="FFFFFF"
gray="888888"
red="ff5555"
dark_red="880000"

while 1 :
	try:
		string = input(" ")
		words=string.split()
	except:
		pass
	elements=string.split(":")
	if len(elements)>5 :
	#	print(elements[0])
		temp = list(elements[0])
	#	print(temp)
		temp.pop(0)
		elements[0] = "".join(temp)
		wm=""
		counter=1
		for i in elements :
			if i[0]=="m" :
				if counter > 2:
					wm=wm+"%{F#"+white+"}%{B#"+black+"} --- "
				wm=wm+"%{F#"+black+"}"
			elif i[0]=="M" :
				if counter > 2:
					wm=wm+"%{F#"+white+"}%{B#"+black+"} --- "
				wm=wm+"%{F#"+white+"}"
			elif i[0]=="o" :
				wm=wm+"%{B#"+dark_blue+"} "+str(counter)+" "
				counter+=1
			elif i[0]=="O" :
				wm=wm+"%{B#"+blue+"} "+str(counter)+" "
				counter+=1
			elif i[0]=="F" :
				wm=wm+"%{B#"+green+"} "+str(counter)+" "
				counter+=1
			elif i[0]=="f" :
				wm=wm+"%{B#"+dark_green+"} "+str(counter)+" "
				counter+=1
			else :
				pass

	elif len(words) == 0 :
		title = ""
	elif (words[0]=="CPU:") :
		temperature = words[1]
	elif (words[0]=="edge:") :
		temperature = words[1]
	elif (words[0]=="time") :
		time_left= words[-2]+" "+words[-1]
	elif (words[0] == "percentage:") :
		percentage = words[-1]
	elif (words[0]=="Clock:") :
		words.pop(0)
		clock=" ".join(words)
	else :
		title = string[:75]
	#print("%{l}%{F#FFFFFF}%{B#"+black+"}"+percentage+"  |  "+time_left+" | "+temperature+"%{c}"+clock+"    "+wm+"%{r}%{F#"+white+"}%{B#"+black+"}"+title)
	print("%{l}%{F#FFFFFF}%{B#"+black+"}"+temperature+"%{c}%{F#FFFFFF}%{B#"+black+"}"+clock+"    "+wm+"%{r}%{F#"+white+"}%{B#"+black+"}"+title)
