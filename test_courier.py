import unittest
import courier

class NumericTest(unittest.TestCase):

    def testOK(self):
        good_values = [1, 2.909, 0, 123,456,789.0, '12345']
        for num in good_values:
            self.assertTrue(courier.is_numeric(num))

    def testNotOK(self):
        bad_values = ['c', '2.9o9']
        for num in bad_values:
            self.assertFalse(courier.is_numeric(num))

class RoundUpTest(unittest.TestCase):
    knownValues = ( (1, 1, 1),
                    (1, 1.2, 2),
                    (0.5, 1, 1),
                    (0.5, 0.8, 1.0),
                    (0.5, 0.3, 0.5),
                    (0.3, 0.3, 0.5),
                    (0.9, 1.3, 1.5),
                    (0, 0, 0.5),
                    )

    def testKnown(self):
        for w_break, in_num, ret_num in self.knownValues:
            self.assertEqual(courier.roundup(in_num, w_break), ret_num)
                    
class VolumetricTest(unittest.TestCase):
    # First tuple: (len, width, height, weight)         -- input
    # Second tuple: ('dim_string', act_mass, vol_mass, int_charge, dom_charge) 
    #        --returned
    # Super tuple: ( first_tuple, second_tuple)

    knownValues = ( 
                    ( (30, 20,1, 1), 
                      ('30.0 x 20.0 x 1.0', 1, 0.1, 1, 1) 
                    ),
                    ( (50, 50, 50, 1),  
                      ('50.0 x 50.0 x 50.0', 1, 25, 25, 25)
                    ),
                    ( (30, 20,1, 0.3), 
                      ('30.0 x 20.0 x 1.0', 0.3, 0.1, 0.5, 1) 
                    ),
                   )

    def testKnown(self):
        for tup1, tup2 in self.knownValues:
            length = tup1[0]
            breadth = tup1[1]
            height = tup1[2]
            weight = tup1[3]
            dim_string = tup2[0]
            act_mass = tup2[1]
            vol_mass = tup2[2]
            int_charge = tup2[3]
            dom_charge = tup2[4]
            v = courier.Volumetric(length, breadth, height, weight)
            self.assertEqual(v.dims, dim_string)
            self.assertEqual(v.mass, act_mass)
            self.assertEqual(v.volumetric, vol_mass)
            self.assertEqual(v.int_chargable, int_charge)
            self.assertEqual(v.dom_chargable, dom_charge)

if __name__ == "__main__":
    unittest.main()



