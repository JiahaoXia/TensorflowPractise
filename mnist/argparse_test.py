__author__ = 'XJH'
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('num', type=int, help="input int")
	parser.add_argument('str', type=str, help="input str")
	parser.add_argument('--ext', type=str, default='hello world!!!',
						help="default value")

	args = parser.parse_args()

	print(args.num)
	print(args.str)
	print(args.ext)

	args1, args2 = parser.parse_known_args()
	print(args1.num)
	print(args1.str)
	print(args1.ext)
	print(args2)

if __name__ == '__main__':
	main()