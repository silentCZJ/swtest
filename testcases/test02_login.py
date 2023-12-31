import pytest
from common.yaml_util import read_yaml
from common.request_util import RequestUtils

req = RequestUtils()
file_path = './data/config.yaml'
configs = read_yaml(file_path)

@pytest.mark.demo
def test_token(uuid):
    url = configs['base_url'] + '/api/login'
    headers = {'Content-Type':'application/json'}
    data = {'username': configs['username'],
            'password': configs['password'],
            'code': configs['code'],
            'uuid': uuid}
    res = req.request_api(method='post', url=url, headers=headers, json=data)
    token = res.json()['token']
    print(token)
    assert '操作成功' in res.text