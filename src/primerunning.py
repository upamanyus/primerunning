#!/usr/bin/env python
import argparse
import genprimes

def main(argv):
    parser = argparse.ArgumentParser(description='Prime running function')

    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument('-w', '--walking', action='store_true',
                              help='generate output for the prime walking function')
    action_group.add_argument('-r', '--running', action='store_true',
                              help='generate output for the prime running function')
    action_group.add_argument('-p', '--gen-primes', action='store', dest='num_primes', type=int,
                              help='output a list of prime numbers up to NUM_PRIMES')
    args = parser.parse_args(argv[1:])

    if args.walking:
        print("Not yet implemented!")
    elif args.running:
        print("Not yet implemented!")
    elif args.num_primes:
        print(genprimes.gen_primes(int(args.num_primes)))
    else:
        return 1
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
