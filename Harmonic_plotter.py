import math as m

#fileout = open("input("File name:")", "w" )

#define harmonic function

def harmonic_function(x) :
    harmonic = m.sin(x) + 1/3 * m.sin(3*x) + 1/5 * m.sin(5*x) + 1/7 * m.sin(7*x)

    return harmonic


def main() :

    x = float(input("what is x"))
    harmonic = harmonic_function(x)
    print(harmonic)

main()


""" need to now create list of x vals 0 to 2pi. instead of printing harm, write out to file. then plot. """
