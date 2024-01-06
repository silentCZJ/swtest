import pytest
from common.request_util import RequestUtils
from common.yaml_util import read_yaml

@pytest.mark.skip(reason="Skip this test case")
def test_add_course(token):
    info = read_yaml('./data/03_course.yaml')
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {token}'}
    data = {'name': info['name'],
            'subject': info['subject'],
            'price': info['price'],
            'applicablePerson': info['applicablePerson']}
    url = 'http://kdtx-test.itheima.net/api/clues/course'
    req = RequestUtils()
    res = req.request_api(method='post',url=url,headers=headers,json=data)
    print(res.text)
    assert '操作成功' in res.text