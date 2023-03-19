import argparse

parser = argparse.ArgumentParser(description='my parser')
parser.add_argument('argument', type=str, help='argument')

args = parser.parse_args()
print(args.argument)

# python .\simple_example.py hello
# python .\simple_example.py "Hello, world!"
