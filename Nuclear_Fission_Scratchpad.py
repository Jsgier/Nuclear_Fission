
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

#Breit-Wigner formula
#sigma_a - absorption cross section, which approximates cross section of
#compound nucleus
#E_n - kinetic engergy of incident neutron
#E_o - neutron energy at resonance
#v - velocity of incident neutron
#C - constant specific to resonance
#gamma - width for the resonance level (kind of like quality facotor in RF)
sigma_a = lambda C,v,E_n, E_o, gamma: (C/v) / ((E_n -E_o)**2 + (gamma**2/4))

def main():



if __name__ == '__main__':
    main()
