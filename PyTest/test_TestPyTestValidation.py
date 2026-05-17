import pytest

@pytest.fixture(scope="module") # each fixture has a default scope
#scope = function means it will run before every test function    
#scope = module means it will run once
# scope = class means it will run once per class
#scope=session means it will run once per session
def preWork():
    print("Browser instance setup")
    return "pass"


@pytest.fixture(scope="function")
def postWork():
    print("This is the post Work Check")
    yield  # This `yeild` keyword is used to separate the setup and teardown code in a fixture.
    #The code before `yield` is executed before the test,
    # and the code after `yield` is executed after the test. 
    # When pytest see there is `yeild` it will pause the execution of the fixture and run the test
    # once the test is done it will resume the execution of the fixture and run the code after 
    # `yield`.
    print("tear down validation")
    
def test_initialCheck(preWork,postWork):
    print("This is the first test")
    #assert preWork == "None" # This will fail as preWork is returning "pass"
    assert preWork == "pass" # This will pass as preWork is returning "pass"
    
@pytest.mark.skip(reason="This test is skipped because it is not ready yet") # This will skip 
#the test and the reason will be printed in the test report
def test_SecondCheck(preWork,postWork):
    print("This is Second Test")