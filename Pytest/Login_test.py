import pytest

@pytest.mark.regression
def testlogin():
    print("Login successfull")

@pytest.mark.skip
def testlogoff():
    print("Logoff successfull")

@pytest.mark.sanity
def testcalculation():
    assert 2+2 == 4


@pytest.mark.xfail
def testcalculation1():
    assert 2+2 == 5