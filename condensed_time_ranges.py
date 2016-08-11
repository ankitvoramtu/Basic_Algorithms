import time

'''
#This part is just for to create a huge random tuple to test how fast the algorithm is
import random
e=2
rlist=random.sample(range(e,1000), 500) #by changing variables tuple size can vary
mytuple=[(1,2)]
#print mytuple
for i in range(len(rlist)):
	t1=rlist[i]-e
	t2=rlist[i]+e
	mytuple=mytuple+[(t1,t2)]
'''

#Meeting schedules
mytuple = [(0, 1), (3, 5),(14,16) ,(13,20) ,(4, 8), (10, 12), (9, 10),(7, 9),(1, 10),
	(1,5),(2,9),(15,19),(18,20),(21,23),(10,12),(9,10),(3,9),(1,2),(2,3),(5,6)]

startd = time.time()
def condense_meeting_times(mytuple):
	dog=1
	while dog==1:
		combtup=[]
		for i in  range(len(mytuple)):
			ss=0
			ee=0
			start=mytuple[i][0]
			end=mytuple[i][1]
			startnew=mytuple[i][0]
			endnew=mytuple[i][1]
			if (start,end) not in combtup:
				combtup.append((start,end))
			for j in range(len(mytuple)):
				del_ind=combtup.index((startnew,endnew))
				combtup=combtup[0:del_ind]+combtup[del_ind+1:len(combtup)]
				if (startnew>mytuple[j][0]) and (startnew<=mytuple[j][1]):
					startnew=mytuple[j][0] 
					ss=1
				if (endnew>=mytuple[j][0]) and (endnew<mytuple[j][1]):
					endnew=mytuple[j][1]
					ee=1
				if (startnew,endnew) not in combtup:
					combtup.append((startnew,endnew))
		if mytuple==combtup:
			break
		else:
			mytuple=combtup[:]		
	return combtup	
print condense_meeting_times(mytuple)
timed=time.time()-startd
print "Done in " + str(timed)
