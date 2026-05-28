from collections import namedtuple 

Task = namedtuple('Task',['summary','owner','id','done'])
Task.__new__.__defaults__ = (None,None,0,False) # the use of __new__.__defaults__ to create the Test Object

def test_defaults():
    """"Using no parameters should invoke the default values"""
    t1 = Task()
    t2 = Task(None,None,None,False)
    
def test_member_access():
    """Check.field functionality of namedtuple"""
    t = Task('buy milk','dip')
    assert t.summary == 'buy milk'
    assert t.owner == 'dip'
    # If I add t.id == 1 and t.done == True then the test will fail because the default values 
    # for id and done are 0 and False respectively.
    assert (t.id,t.done) == (0,False)
    