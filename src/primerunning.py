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
    action_run = subparser.add_parser('run', help=('outputs of the prime '
                                      'walking function at prime values'))

    action_gen_primes.add_argument('-o', '--outfile', type=argparse.FileType('w'),
                                   default=sys.stdout,
                                   help='the file to output to (default is stdout)')
    action_gen_primes.add_argument('n', type=int, help=('find primes up to '
                                   'this number'))

    action_walk.add_argument('-i', '--infile', type=type(""),
                             help=('file containing prime '
                             'numbers (default is to generate them internally)'),
                             required=True)
    action_walk.add_argument('-o', '--outfile', type=type(""),
                             help=('file to output data to'),
                             required=True)
    action_walk.add_argument('a', type=int, help='consider the residue class of a')
    action_walk.add_argument('q', type=int, help='consider residue class mod q')

    action_run.add_argument('-i', '--infile', type=type(""),
                            help=('file containing prime '
                            'numbers (default is to generate them internally)'),
                            required=True)
    action_run.add_argument('-o', '--outfile', type=type(""),
                            help=('file to output data to'),
                            required=True)
    action_run.add_argument('-b', type=int, help='consider the residue class of b')
    action_run.add_argument('-m', type=type(""),
                            help=('consider all residue classes mod q; if '
                                  'specified, the b value is ignored'))
    action_run.add_argument('q', type=int, help='consider residue class mod q')
    action_run.add_argument('-n', type=int, help='input to prime running function')

    args = parser.parse_args(argv[1:])

    if args.command == 'gen-primes':
        with args.outfile as out:
            primes = genprimes.gen_primes(args.n)
            out.write(str(args.n) + "\n")
            out.write("\n".join([str(p) for p in primes]) + "\n")
    elif args.command == 'walk':
        try:
            primeFunctions = primefunctions.PrimeFunctions(args.infile)
            ys = primeFunctions.walkingSumPrimes(args.a, args.q)
            with open(args.outfile, "w") as out:
                for i in range(len(ys)):
                    out.write(str(primeFunctions.primes[i])+"," + str(ys[i])
                              + "\n")
        except RuntimeError as e:
            print("Error: " + str(e))
            return 1
    elif args.command == 'run':
        try:
            primeFunctions = primefunctions.PrimeFunctions(args.infile)
            if args.m == "all":
                yss = primeFunctions.runningSumPrimesAll(args.q)
                with open(args.outfile, 'w') as out:
                    out.write('n value')
                    for a in range(args.q):
                        out.write(',' + str(a) + ' mod ' + str(args.q))
                    out.write('\n')
                    for i in range(len(yss[0])):
                        out.write(str(primeFunctions.primes[i]))
                        for j in range(len(yss)):
                            out.write(',' + str(yss[j][i]))
                        out.write('\n')
            elif args.m == "one":
                ys = primeFunctions.runningSumPrimes(args.b, args.q)
                out.write('n value,' + str(args.b) + ' mod ' + str(args.q) + '\n')
                with open(args.outfile, "w") as out:
                    for i in range(len(ys)):
                        out.write(str(primeFunctions.primes[i]) + ',' + str(ys[i])
                                  + '\n')
            else:
                for i in range(50):
                    with open('mod' + str(i) + '.txt', 'w') as out:
                        q = primeFunctions.primes[i]
                        for j in range(1, q):
                            n = primeFunctions.runningSum(j, q, args.n)
                            out.write(str(j) + ': ' + str(n) + '\n')
        except RuntimeError as e:
            print("Error: " + str(e))
            return 1
    else:
        return 1
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
