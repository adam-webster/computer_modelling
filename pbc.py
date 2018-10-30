import math
import numpy as np


def image_in_cube(x,y,z,l, cube, input_vector) :

    #set initial image vector to go into while loop
    image_vector = input_vector

    #while loop to ensure final result is indeed in the box of size l
    while np.linalg.norm(image_vector) > np.linalg.norm(cube):

        if x <= l :
            x = x
        else:
            x = x - l

        if y <= l :
            y = y
        else:
            y = y - l

        if z <= l :
            z = z
            break #needed to avoid infinite loop
        else:
            z = z - l

    image_vector = np.array([x, y, z])
    return image_vector



def closest_image(x,y,z,l, cube, input_vector):
    image_vector = image_in_cube(x,y,z,l, cube, input_vector)
    print(np.mod(image_vector, cube))




def main() :

    #prompt for input position and box size

    x = 5#float(input('x coordinate: '))
    y = 5#float(input('y coordiante: '))
    z = 5#float(input('z coordinate: '))
    l = 2#float(input('box size: '))

    #make this a vector using numpy array
    input_vector = np.array([x, y, z])

    #create cube of size l
    cube = np.array([l,l,l])


#    image_in_cube(x,y,z,l, cube, input_vector)
    image_vector = image_in_cube(x,y,z,l, cube, input_vector)
    print(image_vector) #print result once all iterations of loop are finished
    closest_image(x,y,z,l, cube, input_vector)


main()
