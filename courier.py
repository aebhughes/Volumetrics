'''
A collection of common solutions to Logistics systems 
'''


def is_numeric(var):
    """ 
    A standard numeric test. Returns 'True' if numeric or 'False' otherwise.  
    """
    if type(var) == str:
         var = var.replace(',','')   # remove commas
    try:
        float(var)
        return True
    except ValueError:
        return False

def roundup(num, wb=1.0):
    """ 
    Rounds up a given mass in Kg's float value, (num) to the next 
    weight-break value (wb).  Weight break values should be either 0.5 
    for international courier, 1.0 for Domestic courier.  
    """
    if num % 1 == 0:
        if num > 0:
            return num
        else:
            return 0.5
    else: 
        if wb % 1 > 0:   # Weight-break can only be 1.0 or 0.5
            wb = 0.5
        else:
            wb = 1.0
        if wb == 1 or num % 1 >= 0.5:
            return int(num) + 1
        else:
            return int(num) + wb

class Volumetric:
    """ 
    Volumetric calculation : (length X breadth x height) / 5000.
    Arguments;
        length = in cm's
        breadth = width in cm's
        height  = in cm's
        mass    = weight in Kg's

    Valid numeric input is assumed
    """
    def __init__(self, l, b, h, mass):
        l, b, h = self._clean_parms(l, b, h)
        self.dims = '{0:.1f} x {1:.1f} x {2:.1f}'.format(l, b, h)
        self.mass = float(mass)
        self.volumetric = round(((l * b * h) / 5000.0), 1)
        self.dom_chargable = self._calc_chargable(self.volumetric, self.mass, 
                                                 1.0) 
        self.int_chargable = self._calc_chargable(self.volumetric, self.mass,
                                                 0.5) 
        
    def _clean_parms(self, l, b, h):
        '''
        normalise the input to rational values
        '''
        v = dict(l=l, b=b, h=h)
        for x in v.keys():
            if v[x] < 1:
                v[x] = 1.0
            else:
                v[x] = float(v[x])
        return v['l'], v['b'], v['h']

    def _calc_chargable(self, vols, mass, wb):
        '''
        choose the greater of volumetric weight vs. actual weight 
        '''
        mass = roundup(float(mass), float(wb))
        if vols < mass:
            return mass
        else:
            return roundup(vols, wb)

