import time
fraction_list = [2,3,6]
fraction_list.sort(reverse=True)
print(fraction_list)
xlist = []
ylist = []
reps = 0
count = 0	
while True:
	reps += 1
	fraction = fraction_list[count]
	for factor1 in range(1, max(fraction_list)+1):
		if fraction%factor1 == 0:
			for factor2 in range(1,factor1):
				if factor1%factor2 == 0:
					p,k,m = fraction//factor1,factor2,factor1//factor2
					x = p*k*(k+m)
					y = p*m*(k+m)
					if x<=2023:
						if y<=2023:
							if x in xlist or y in ylist:
								pass
							else:
								xlist.append(x)
								ylist.append(y)
	for index, (bx, by) in enumerate(zip(xlist, ylist)):
		if (bx in fraction_list) or (by in fraction_list) or (bx==by):
			pass
		else:
			fraction_list.append(bx)
			fraction_list.append(by)
			fraction_list.remove(fraction)
			fraction_list.sort(reverse=True)
			print(fraction_list)
			xlist,ylist = [],[]
			break
		fraction = fraction_list[count]
	#time.sleep(0.5)
	if fraction >= 1200:
		count+=1
	if reps % 300 == 0:
		count+=1
	if count == len(fraction_list):
		break
fraction_list.sort(reverse=True)
print(fraction_list)
print(f"{len(fraction_list)} fractions found in {reps} reps!")					