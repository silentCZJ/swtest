import pytest
import time
from common.logger_util import LoggerUtil


@pytest.mark.log
def test_log():
    util = LoggerUtil()
    logger = util.get_logger()

    time.sleep(1)
    logger.info('after 1 sec')

    time.sleep(1)
    logger.info('after 2 sec')

    time.sleep(1)
    logger.info('after 3 sec')

    assert 1 == 1
