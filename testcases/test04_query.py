from common.request_util import RequestUtils

def test_query_course(token):
    url = 'http://kdtx-test.itheima.net/api/clues/course/list'
    headers = {'Authorization': token}
    req = RequestUtils()
    res = req.request_api(method='post',url=url,headers=headers)
    print(res)
    assert 200 in res.text


