from imports import *


# terminal clearing function for cleaner output
def clear():
	# windows
	if os.name == 'nt':
		os.system('cls')
	# mac/linux
	else:
		os.system('clear')
