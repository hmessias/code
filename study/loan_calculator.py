#! /usr/bin/env python3
""" this calculates how much you pay on a loan """
LOAN = input("tell how much you want to loan: ")
RATE = input("tell what is the interest rate, in %: ")
NUMBER = input("in how many times you want to pay: ")
L = int(LOAN)
N = int(NUMBER)
R1 = int(RATE)
I = R1/100
M = 0
M1 = 0
M2 = 0
M1 = L*N*(I*(1+I))
M2 = ((1+I)*N-1)
M = M1/M2
print(M)
