import courier

KNOWNVALUES = ( (1, 1, 1),
                (1, 1.2, 2),
                (0.5, 1, 1),
                (0.5, 0.8, 1.0),
                (0.5, 0.3, 0.5),
                (0.3, 0.3, 0.5),
                (0.9, 1.3, 1.5),
                (0, 0, 0.5),
                )

def test_rounding():
    for w_break, in_num, ret_num in KNOWNVALUES:
        r = courier.roundup(in_num, w_break)
        assert r == ret_num

def test_volumetrics():
    v = courier.Volumetric(30,20,1,1)  # Length, Bredth, Height, actual weight)
    assert v.dims == '30.0 x 20.0 x 1.0' 
    assert v.mass == 1
    assert v.volumetric == 0.1
    assert v.int_chargable == 1  
    assert v.dom_chargable == 1  
    v = courier.Volumetric(50,50,50,1)  # Length, Bredth, Height, actual weight)
    assert v.dims == '50.0 x 50.0 x 50.0' 
    assert v.mass == 1
    assert v.volumetric == 25
    assert v.int_chargable == 25  
    assert v.dom_chargable == 25 
    v = courier.Volumetric(30,20,1,0.3)  # Length, Bredth, Height, actual weight)
    assert v.dims == '30.0 x 20.0 x 1.0' 
    assert v.mass == 0.3
    assert v.volumetric == 0.1
    assert v.int_chargable == 0.5  
    assert v.dom_chargable == 1
