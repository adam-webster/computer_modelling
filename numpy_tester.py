import math
import random
import numpy as np

'''
    This program randomly creates vectors, tells you what the vectors are

    then shows how simple vector calculations work. The random vectors produced are non integer to ensure the program works for all possible inputs.

    It also tests the following identities using numpy and show if they hold true or not:

    v1 x v2 = - v2 x v1

    v1 ×(v2 + v3) = (v1 x v2) + (v1 × v3)

    v1 ×(v2 × v3) = (v1 · v3)v2 − (v1 · v2)v3
'''


def identity_1(v1, v2):

    #v1 x v2 = - v2 x v1

    vLHS = np.cross(v1, v2) #lhs
    v4 = np.cross(v2, v1)
    vRHS = v4*-1 #rhs

    if np.all(vLHS) == np.all(vRHS) :
        print('v1 x v2 = - v2 x v1')
    else:
        print('v1 x v2 does not equal - v2 x v1')


def identity_2(v1, v2, v3):

    #v1 ×(v2 + v3) = (v1 × v2) + (v1 × v3)

    v4 = v2 + v3
    vLHS = np.cross(v1, v4) #lhs of identity
    v5 = np.cross(v1,v2)
    v6 = np.cross(v1, v3)
    vRHS = v5 + v6 #rhs of identity

    if np.all(vLHS) == np.all(vRHS) :
        print('v1 ×(v2 + v3) = (v1 x v2) + (v1 × v3)')
    else:
        print('v1 ×(v2 + v3) does not equal (v1 × v2) + (v1 × v3)')


def identity_3(v1, v2, v3):

    #v1 ×(v2 × v3) = (v1 · v3)v2 − (v1 · v2)v3

    v4 = np.cross(v2, v3)
    vLHS = np.cross(v1, v4) #lhs of identity
    s5 = np.inner(v1, v3)
    s6 = np.inner(v1, v2)
    s6 = -s6
    v5 = v2 * s5
    v6 = v3 * s6
    vRHS = v5 + v6 #rhs of identity

    if np.all(vLHS) == np.all(vRHS):
        print('v1 ×(v2 × v3) = (v1 · v3)v2 − (v1 · v2)v3')
    else:
        print('v1 ×(v2 × v3) does not equal (v1 · v3)v2 − (v1 · v2)v3')


# Main method:

def main():

    # Create two random vectors

    v1 = np.array([random.random(), random.random(), random.random()])
    v2 = np.array([random.random(), random.random(), random.random()])
    v3 = np.array([random.random(), random.random(), random.random()])


    #line break in output screen, clearer to read

    print()


    # Print out the vectors to terminal window

    print("v1 = ", v1)
    print("v2 = ", v2)
    print("v3 = ", v3)


    #line break in output screen, clearer to read

    print()

    #print basic vector manipulations

    #vector sum, scalar product and vector (cross) product

    print("v1 + v2 =", v1 + v2)
    print('v1 · v2 =', np.inner(v1, v2))
    print('v1 x v2 =', np.cross(v1, v2))

    #line break in output screen, clearer to read

    print()


    #testing if the vector identites hold

    identity_1(v1, v2)
    identity_2(v1, v2, v3)
    identity_3(v1, v2, v3)


# Execute main method

main()
