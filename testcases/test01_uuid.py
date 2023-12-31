import pytest
from common.request_util import RequestUtils

@pytest.mark.demo
def test_get_uuid():
    req = RequestUtils()
    res = req.request_api(method='get', url=r'http://kdtx-test.itheima.net/api/captchaImage')
    uuid = res.json()['uuid']
    print(uuid)
    assert uuid != None and res.status_code == 200