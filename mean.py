

def mean(a):
    '''
    MEAN calculates the arithemtic average of the entered numbers.

    Parameters
    ----------
    a : float, int 
        
    Example:
    
        a=[3.9,45,3,12,19.4]
        
    mean([3.9,45,3,12,19.4])

    Returns
    -------
    Average

    '''

    S=sum(a)
    Ave=S/len(a)
    
    return print("Average is:", Ave)