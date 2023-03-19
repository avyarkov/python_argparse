import argparse

parser = argparse.ArgumentParser(
    description="multiple arguments parser")

parser.add_argument('positional', type=str, nargs='*')
parser.add_argument('-o', '--optional', type=str, nargs='*')
parser.add_argument('-c', '--collect', type=str, action='append')

args = parser.parse_args()

print(args.positional)
print(args.optional)
print(args.collect)

# python .\multiple_arguments.py aa bb cc -o qq ww ee -c xx -c yy -c zz
