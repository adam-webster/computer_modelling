import math
import random
import vector

# Main method:
def main():
    # Create two random vectors

    v1 = [1,2,3] #[random.random(), random.random(), random.random()]
    v2 = [2,2,3]#[random.random(), random.random(), random.random()]
    v3 = [1,2,3]#[random.random(), random.random(), random.random()]
    # Print out the vectors to terminal window
    print("v1 = ", v1)
    print("v2 = ", v2)
    print("v3 = ", v3)

    #print basic vector manipulations
    #vector sum, scalar product and vector (cross) product
    print("v1 + v2 =", vector.sum(v1, v2))
    print('v1 . v2 =', vector.dot(v1, v2))
    print('v1 x v2 =', vector.cross(v1, v2))


    #testing if the vector identites hold
    #identity 1
    if vector.cross(v1, v2)[0]+vector.cross(v2, v1)[0]==0 and vector.cross(v1, v2)[1]+vector.cross(v2, v1)[1]==0 and vector.cross(v1, v2)[2]+vector.cross(v2, v1)[2]==0:
        print('v1 x v2 = - v2 x v1')
    else:
        print('v1 x v2 does not equal - v2 x v1')

    #identity 2
    if 



"""
    # Test unary functions from complex.py:
    # conjugation, modulus (squared), scaling
    print("conj(c2) = ", cplx.conj(c2))
    print("|c2|^2 = ", cplx.norm_sq(c2))
    print("|c2|   = ", cplx.norm(c2))
    print("3*c2   = ", cplx.scale(c2,3.0))

    # Test binary functions from complex.py:
    # addition, subtraction, multiplication, division

    print("c1+c2 = ", cplx.add(c1,c2))
    print("c1-c2 = ", cplx.sub(c1,c2))
    print("c1*c2 = ", cplx.mul(c1,c2))
    print("c1/c2 = ", cplx.div(c1,c2))
"""
# Execute main method
main()
