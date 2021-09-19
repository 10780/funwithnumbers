#this program doesn't really do anything, it's just fun to watch the numbers go
def count(n):
	i = n
	stop = False
	if i > 0:
		print(i)
		while i > 0 and stop == False:
			i -= 1
			print(i)
			if i == 0:
				while i < n and stop == False:
					i += 1
					print(i)
					if i == n:
						stop = True
	elif i <= 0:
		print(i)
		while i < 0 and stop == False:
			i += 1
			print(i)
			if i == 0:
				while i > n and stop == False:
					i -= 1
					print(i)
					if i == n:
						stop = True
