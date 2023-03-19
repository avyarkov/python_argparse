import argparse


def combine(args):
    words = args.words
    if args.use_camel:
        return ''.join(map(lambda w: w.capitalize(), words))
    if args.use_snake:
        return '_'.join(map(lambda w: w.lower(), words))
    if args.use_const:
        return '_'.join(map(lambda w: w.upper(), words))
    if args.use_dash:
        return '-'.join(words)

    delimiter = '' if args.merge else args.delimiter
    if args.capitalize:
        words = map(lambda w: w.capitalize(), words)
    if args.uppercase:
        words = map(lambda w: w.upper(), words)
    return delimiter.join(words)


def main():
    parser = argparse.ArgumentParser(
        description='console command to combine words')

    parser.add_argument('words', type=str, nargs='*', help='words to combine')

    parser.add_argument('--camel', action='store_true', dest='use_camel',
                        help='use CamelCase')
    parser.add_argument('--snake', action='store_true', dest='use_snake',
                        help='use snake_case')
    parser.add_argument('--const', action='store_true', dest='use_const',
                        help='use CONST_CASE')
    parser.add_argument('--dash', action='store_true', dest='use_dash',
                        help='use dash-case')

    parser.add_argument('-m', '--merge', action='store_true',
                        help='merge words without a delimiter')
    parser.add_argument('-d', '--delimiter', type=str, default='_',
                        help='delimiter to use when combining')
    parser.add_argument('-c', '--capitalize', action='store_true',
                        help='Capitalize All Words')
    parser.add_argument('-u', '--uppercase', action='store_true',
                        help='UPPERCASE ALL WORDS')

    result = combine(parser.parse_args())
    print(result)


if __name__ == '__main__':
    main()
