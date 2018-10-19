import math

import random

import vector

'''
    this program randomly creates vectors, tells you what the vectors are
    then shows how simple vector calculations work. it also tests the following
    identities and show if they hold true or not:
    v1 x v2 = - v2 x v1
    v1 ×(v2 + v3) = (v1 x v2) + (v1 × v3)
    v1 ×(v2 × v3) = (v1 · v3)v2 − (v1 · v2)v3

'''



def identity_1(v1, v2):

    #v1 x v2 = - v2 x v1

    if vector.cross(v1, v2)[0]+vector.cross(v2, v1)[0]==0 and vector.cross(v1, v2)[1]+vector.cross(v2, v1)[1]==0 and vector.cross(v1, v2)[2]+vector.cross(v2, v1)[2]==0:

        print('v1 x v2 = - v2 x v1')

    else:

        print('v1 x v2 does not equal - v2 x v1')


def identity_2(v1, v2, v3):

    #v1 ×(v2 + v3) = (v1 × v2) + (v1 × v3)

    v4 = vector.sum(v2, v3)
    v4 = vector.cross(v1, v4) #lhs
    v5 = vector.cross(v1,v2)
    v6 = vector.cross(v1, v3)
    v7 = vector.sum(v5, v6) #rhs

    if v4[0]==v7[0] and v4[1]==v7[1] and v4[2]==v7[2]:
        print('v1 ×(v2 + v3) = (v1 x v2) + (v1 × v3)')
    else:
        print('v1 ×(v2 + v3) does not equal (v1 × v2) + (v1 × v3)')


def identity_3(v1, v2, v3):

    #v1 ×(v2 × v3) = (v1 · v3)v2 − (v1 · v2)v3

    v4 = vector.cross(v2, v3)
    v4 = vector.cross(v1, v4) #lhs
    s5 = vector.dot(v1, v3)
    s6 = vector.dot(v1, v2)
    s6 = -s6
    v5 = vector.scalar_mult(v2, s5)
    v6 = vector.scalar_mult(v3, s6)
    v7 = vector.sum(v5, v6) #rhs

    if v4[0]==v7[0] and v4[1]==v7[1] and v4[2]==v7[2]:
        print('v1 ×(v2 × v3) = (v1 · v3)v2 − (v1 · v2)v3')
    else:
        print('v1 ×(v2 × v3) does not equal (v1 · v3)v2 − (v1 · v2)v3')



# Main method:

def main():

    # Create two random vectors

    v1 = [random.random(), random.random(), random.random()]

    v2 = [random.random(), random.random(), random.random()]

    v3 = [random.random(), random.random(), random.random()]


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

    print("v1 + v2 =", vector.sum(v1, v2))

    print('v1 · v2 =', vector.dot(v1, v2))

    print('v1 x v2 =', vector.cross(v1, v2))

    #line break in output screen, clearer to read
    print()


    #testing if the vector identites hold

    identity_1(v1, v2)
    identity_2(v1, v2, v3)
    identity_3(v1, v2, v3)



# Execute main method

main()
