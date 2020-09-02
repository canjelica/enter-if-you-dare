def staircase(n):
	i = 1
	while i != n:
		level = n-i
		print((" " * level) + ("#" * (n-level)))
		i += 1



   
    # n=4
    # 3 spaces 1 #
    # 2 spaces 2 #
    # 1 space 3 #
    # 0 spaces 4 #

    #need a loop to print out n lines
    #for every line, n-1 spaces and then n - (n-1)
    #next line n-2 spaces, then n - (n-2)
    #n-3, n - (n-3)
    # n#
    #need a loop to print out n lines
    #for every line, n-1 spaces and then n - (n-1)
    #next line n-2 spaces, then n - (n-2)
    #n-3, n - (n-3)
    # n#
