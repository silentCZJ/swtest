import pytest

def read_yaml():
    return ['a','b','c']

@pytest.fixture(scope='function',autouse=False,params=read_yaml())
def connect_mysql(request):
    print('connect')
    yield request.param
    print('disconnect')

