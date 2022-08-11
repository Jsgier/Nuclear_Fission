
#purpose of this script is to provide a scratchpad for

import numpy

# Constants
N_A = 6.022E23 #Avogadro's number, mol^-1

# User Defined Functions

#dP- probability of reaction
#N - number of nuclei per unit volume
#sigma - cross section. Note - total cross section is sum of all cross sections
#dx - short distance traveled by neutron
dP = lambda N,sigma,dx : N*sigma*dx

#N- number of nuclei per unit volume
#rho - density
#N_A - Avogadro's number
#M - material atomic mass
N = lambda rho,M : N_A*rho / M

#mfp - mean free path
mfp = lambda N, sigma: 1 / (N*sigma)


def main():



if __name__ == '__main__':
    main()
