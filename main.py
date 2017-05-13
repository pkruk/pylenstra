#! /usr/bin/python

import argparse

from gmpy2 import mpz
from mpi4py import MPI
from time import time
from lenstra import Lenstra
from sys import exit

parser = argparse.ArgumentParser(description="Do you want to factor something?")
parser.add_argument('-n', '--number', help='number which will be attacked by ECM', required=True)
parser.add_argument('-s', '--silent', help="non-verbose output", required=False, action='store_true')
args = parser.parse_args()

start = time() # init timer
comm = MPI.COMM_WORLD

sol = Lenstra(mpz(args.number)).factor()
if sol is not None:
    if args.silent:
        print(sol)
    else:
        print('Number ', args.number, ' was factored with time ', time() - start, ' ms, and the factor is a:', sol)
        print('We find a solution, so kill all MPI processes')
    MPI.COMM_WORLD.Abort(1)
    exit(0)


