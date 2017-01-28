#!/usr/bin/env python
import primefunctions
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

    action_gen_primes.add_argument('-o', '--outfile', type=argparse.FileType('w'),
                                   default=sys.stdout,
                                   help='the file to output to (default is stdout)')
    action_gen_primes.add_argument('n', type=int, help=('find primes up to '
                                   'this number'))
    action_walk.add_argument('-i', '--infile', type=type(""),
                             default=sys.stdin, help=('file containing prime '
                             'numbers (default is to generate them internally)'))
    action_walk.add_argument('a', type=int, help='consider the residue class of a')
    action_walk.add_argument('q', type=int, help='consider residue class mod q')
    action_walk.add_argument('n', type=int, help='the input of the walking function')
    args = parser.parse_args(argv[1:])

    if args.command == 'gen-primes':
        with args.outfile as out:
            primes = genprimes.gen_primes(args.n)
            out.write(str(args.n) + "\n")
            out.write("\n".join([str(p) for p in primes]) + "\n")
    if args.command == 'walk':
        try:
            primeFunctions = primefunctions.PrimeFunctions(args.infile)
            print(primeFunctions.walkingSum(args.a, args.q, args.n))
        except RuntimeError as e:
            print("Error: " + str(e))
    else:

        return 1
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
