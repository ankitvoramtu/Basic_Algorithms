s = raw_input('The List: ') #given list should be in ascending order
list = map(int, s.split())
sum = int(raw_input('The Sum to reach: '))

first = 0
last = len(list)-1

#This loop check the first and last elements of list to reach the sum.
#In every iteration, the first or last element of list changed, when this happens
#the previous one is no longer consideration.
while last >= 0 and first < len(list) and list[first] + list[last] != sum:
	print str(first) + " " + str(last) #to check the trials
	if list[first] + list[last] < sum: #since our sum is higher we need to shift the little one (first)
		first += 1
	elif list[first] + list[last] > sum: #since our sum is lower we need to shift the big brother (last)
		last -= 1

#guess it`s obvious why I put these conditions
if last < 0 or first == len(list): 
	print "You cannot reach " + str(sum) + " with these numbers."
elif list[first] + list[last] == sum:
	print str(list[first]) + " + " + str(list[last]) + " = " + str(sum)
