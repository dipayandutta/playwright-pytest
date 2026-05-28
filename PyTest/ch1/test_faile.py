def test_fail():
    assert (1,2,3) == (3,2,1)
    
    
'''
This test case will fail because the two tuples (1,2,3) and (3,2,1) are not equal. 
The assertion will raise an AssertionError, indicating that the test has failed.

The best part of the PyTest OutPut is that it provides exact line or index of the error 

 AssertionError: assert (1, 2, 3) == (3, 2, 1)
E
E         At index 0 diff: 1 != 3 <---------- index 0 is different 
'''
