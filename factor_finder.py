num = 100
# fraction_list.sort(reverse=False)	
for factor1 in range(1, 2023):
	if num%factor1 == 0:
		for factor2 in range(1,factor1):
			if factor1%factor2 == 0:
				p,k,m = num//factor1,factor2,factor1//factor2
				x,y = p*k*(k+m),p*m*(k+m)
				if x <= 2023 and y <= 2023:	
						print(x,y)