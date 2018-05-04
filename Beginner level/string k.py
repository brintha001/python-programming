def play_44():
	s=input('Enter string :')
	k=int(input('Enter k :'))
	c=s[k:]
	c+=s[:k]
	print(c)
  
play_44()
