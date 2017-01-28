#!/usr/bin/env python
import argparse
import genprimes


def main(argv):
    parser = argparse.ArgumentParser(description='Prime running function')
    subparser = parser.add_subparsers(dest='command')

    action_primes_help = 'generates a list of primes up to the given input'
    action_gen_primes = subparser.add_parser('gen-primes',
                                             help=action_primes_help)
    action_walk = subparser.add_parser('walk')
    action_run = subparser.add_parser('run')

    action_gen_primes.add_argument('--out', type=argparse.FileType('w'),
                                   default=sys.stdout)
    action_gen_primes.add_argument('n', type=int, help='find primes up to this\
            number')
    action_walk.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args(argv[1:])

    if args.command == 'gen-primes':
        with args.out as outfile:
            primes = genprimes.gen_primes(args.n)
            outfile.write("\n".join([str(p) for p in primes]))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
