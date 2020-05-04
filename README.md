# Pylenstra

Implementation of Lenstra elliptic curve factorization method [link](https://en.wikipedia.org/wiki/Lenstra_elliptic_curve_factorization) [pub](http://wstein.org/edu/124/lenstra/lenstra.pdf).
This is a small part of my master thesis, which i would like to share.
Maybe someone will find this implementation useful to gain some knowledge about Elliptic Curves.

## Specification:

You will need this packages and libraries:
 * [Open MPI](https://www.open-mpi.org/)
 * [mpi4py](http://mpi4py.readthedocs.io/en/stable/)
 * [gmpy2](https://gmpy2.readthedocs.io/en/latest/index.html)
 
Installation on **ArchLinux**:
```
pacman -S openmpi #(archlinux)

pip install gmpy2 mpi4py
```

Installation on **Debian-based (tested on Ubuntu 18.04 LTS)**:
```
sudo apt install mpc libmpc-dev
pip3 install gmpy2 mpi4py
```

## Example of usage:

To run the app, please execute ``src/main.py``, with using this options:

* -h --help - print help 
* -n --number - Number we want to factor (attack ;) )

Examples:

```
➜  src: python src/main.py -n 829348951
Number  829348951  was factored with time  0.001033782958984375  ms, and the factor is a: 7919
We find a solution, so kill all MPI processes
--------------------------------------------------------------------------
MPI_ABORT was invoked on rank 0 in communicator MPI_COMM_WORLD 
with errorcode 1.

NOTE: invoking MPI_ABORT causes Open MPI to kill all MPI processes.
You may or may not see output from other processes, depending on
exactly when Open MPI kills them.
--------------------------------------------------------------------------
```

With using Open MPI: 

```
➜  src: mpirun -np 4 python src/main.py -n 829348951
Number  829348951  was factored with time  0.011167049407958984  ms, and the factor is a: 7919
We find a solution, so kill all MPI processes
--------------------------------------------------------------------------
MPI_ABORT was invoked on rank 2 in communicator MPI_COMM_WORLD 
with errorcode 1.

NOTE: invoking MPI_ABORT causes Open MPI to kill all MPI processes.
You may or may not see output from other processes, depending on
exactly when Open MPI kills them.
--------------------------------------------------------------------------
```
