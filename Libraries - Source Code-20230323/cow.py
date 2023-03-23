import cowsay
import sys

if len(sys.argv) == 2:
	cowsay.turkey("hello, " + sys.argv[1])
	