
import pytest

@pytest.fixture(scope="session") # each fixture has a default scope
def preSetWork():
    print("This is the pre work for the session")
    