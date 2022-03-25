
def sigma(a):
    '''
    SIGMA function calculates the summation from number 1 to a

    Parameters
    ----------
    a : int
        DESCRIPTION.

    Returns
    -------
    The summation from 1 to a

    '''
    z=0
    for i in range(1,a+1):
        
        z=z+i
        
        print("The summation from 1 to "+str(a)+" is: ",z)
        
