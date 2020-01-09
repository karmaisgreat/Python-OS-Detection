import platform
os = platform.system()
if 'Windows' in os:
	print('\nWindows OS Detected!\n')
elif 'Linux' in os:
	print('\nLinux OS Detected!\n')
else:
	print('\nUnknown OS Detected!\n')