import pytest
from common.yaml_util import read_yaml
from common.request_util import RequestUtils

req = RequestUtils()
file_path = 'data/config.yaml'
configs = read_yaml(file_path)

@pytest.fixture(scope='session',autouse=False)
def uuid():
    url = configs['base_url'] + '/api/captchaImage'
    res = req.request_api(method='get', url=url)
    uuid = res.json()['uuid']
    return uuid

@pytest.fixture(scope='session',autouse=False)
def token(uuid):
    url = configs['base_url'] + '/api/login'
    headers = {'Content-Type':'application/json'}
    data = {'username': configs['username'],
            'password': configs['password'],
            'code': configs['code'],
            'uuid': uuid}
    res = req.request_api(method='post', url=url, headers=headers, json=data)
    token = res.json()['token']
    return token