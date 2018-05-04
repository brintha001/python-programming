def play_40():
	n=int(input())
	b=0
	for i in range(n+1):
		for j in range(n+1):
			d=(i*1)+(j*2)
			if d==n:
				b+=1
	print(b)
play_40()
