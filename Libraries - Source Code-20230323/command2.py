import sys

if len(sys.argv) < 2:
	sys.exit("Too Few Arguments")
elif len(sys.argv) > 2:
	sys.exit("Too much Arguments")

print("Welcome Back, "+sys.argv[1])