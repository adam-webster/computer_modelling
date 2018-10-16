import math as m

def mag(v):
    """
    The magnitude of the vector
    :param v: 3D vector (vx, vy, vz)
    :return: magnitude sqrt(vx**2 + vy**2 + vz**2)
    """
    return m.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def mag_sq(v):
    """
    The squared magnitude of the vector
    :param v: 3D vector (vx, vy, vz)
    :return: magnitude vx**2 + vy**2 + vz**2
    """
    return v[0]**2 + v[1]**2 + v[2]**2

def scalar_mult(v, scalar):
    """
    vector multiplied by a scalar
    :param v: 3D vector (vx, vy, vz)
    :param scalar: scalar factor
    :return: scaled vector (vx*scalar, vy*scalar, vz*scalar)
    """
    return [v[0]*scalar, v[1]*scalar, v[2]*scalar]

def scalar_div(v, scalar):
    """
    vector divided by a scalar
    :param v: 3D vector (vx, vy, vz)
    :param scalar: scalar factor
    :return: scaled vector (vx/scalar, vy/scalar, vz/scalar)
    """
    return [v[0]/scalar, v[1]/scalar, v[2]/scalar]

def sum(a, b):
    """
    Vector sum of 2 vectors
    :param a: first 3D vector (ax, ay, az)
    :param b: second 3D vector (bx, by, bz)
    :return: vector sum (ax+bx , ay+by , az+bz)
    """
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def dif(a, b):
    """
    Vector difference of 2 vectors
    :param a: first 3D vector (ax, ay, az)
    :param b: second 3D vector (bx, by, bz)
    :return: vector sum (ax-bx , ay-by , az-bz)
    """
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def cross(a, b):
    """
    Vector (cross) product of 2 vectors
    :param a: first 3D vector (ax, ay, az)
    :param b: second 3D vector (bx, by, bz)
    :return: vector product (ay*bz - az*by , az*bx - ax*bz , ax*by - ay*bx)
    """
    return [a[1]*b[2]-a[2]*b[1] , a[2]*b[0]-a[0]*b[2] , a[0]*b[1]-a[1]*b[0]]

def dot(a,b):
    """
    Scalar product of 2 vectors
    :param a: first 3D vector (ax, ay, az)
    :param b: second 3D vector (bx, by, bz)
    :return: scalar product ax*bx + ay*by + az*bz
    """
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def equal(a, b):
    """
    Tells you if 2 vectors are the same or not
    :param a: first 3D vector (ax, ay, az)
    :param b: second 3D vector (bx, by, bz)
    :return: print 'Vectors are the same' if a = b or print 'Vectors are not the same' else
    """
    if a == b:
        print('Vectors are the same')
    else:
        print('Vectors are not the same')
