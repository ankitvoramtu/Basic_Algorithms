import numpy
a=numpy.matrix([[-20, 3, 3,5],[2,0, 3, 4],[4,6, 5, 6],[4,8,1,-1]]) #change to whatever you want, it doesn't need to be NxN
									#you can also get the matrix as an input of course
(k,l)=a.shape
iter=0
count=1
maxsubsum=0
for i in range(k):
	for i2 in range(k+1):
		if i >= i2:
			iter+=1
		else:
			for j in range(l):
				for j2 in range(l+1):
					if j >= j2:
						iter+=1
					else:
						submat=a[int(i):int(i2),int(j):int(j2)]
						print submat, submat.sum()
						count+=1
						if submat.sum()>maxsubsum:
							maxsubsum=submat.sum()
							maxsubmat=a[int(i):int(i2),int(j):int(j2)]
							print "guess I`ve found... :-)"
						else:
							print "Not this one..."
#							raw_input("Press Enter for next submatrix... ")	
print "\nResult: "
print maxsubmat
print "with sum of "+str(maxsubsum)
