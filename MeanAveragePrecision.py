#see "Metrics_Explained.docx" for explanation in Turkish
import csv
import sys
import time
start=time.time()
#K=int(sys.argv[1]) #as argument
K_list=[2,3,5] #as variable
K_dict={}

for K in K_list:
	print "\n###### Test for K "+str(K)+" ######"
	i=0
	TotalAveragePrecision=0
	in_file_2 = open("predicted.csv","rb")
	predicted = csv.reader(in_file_2)
	for row in predicted:
		if i==0: #pass header
			pass
		else: 
			user=row[0]
			print "\nuser " + user
			user_post_list=[]
			in_file_1 = open("actual.csv","rb")
			actual = csv.reader(in_file_1)
			precision_score=0
			AveragePrecision=0
			for line in actual:		
				if line[0]==user:
					user_post_list.append(line[1])
			R = len(user_post_list)
			print "R " + str(R)
			print "K " + str(K)
			print "min(R,K) " + str(min(R,K))
			for j in range(K):
				
				#precision
				precision="User_Precision@"+str(j+1)
				if row[j+1] in user_post_list:				
					precision_score+=float(1)
				
				#recall
				recall="Ch_Recall@"+str(j+1)
				if row[j+1] in user_post_list:	
					recall_score=float(1)/min(R,K)
				else:
					recall_score=float(0)	
				
				AveragePrecision+=((precision_score/(j+1))*recall_score)
				print precision + " "+ str(precision_score/(j+1))
				print recall + " "+ str(recall_score)
			print "AveragePrecision@"+str(K)+" " + str(AveragePrecision)
			TotalAveragePrecision+=AveragePrecision
			#print user
			#print user_post_list
		i+=1	
	print "\nTotal User " + str(i-1)
	print "MeanAveragePrecision@"+str(K)+" "+str(TotalAveragePrecision/(i-1))
	newkey= "MeanAveragePrecision@"+str(K)
	K_dict[newkey] = TotalAveragePrecision/(i-1)
print "\n###### Final Output ######"
#print K_dict
for keys, values in K_dict.items():
	print keys, values

print "Done in "+str(time.time()-start)+" seconds."
	
#exit()



		


