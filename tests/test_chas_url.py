from chas_url.checking_for_urls import check_urls

from tests.fixtures.expected_dics import RESULT_DICT


def test_check_urls():
    assert check_urls(['https://ru.hexlet.io/', 'https://mail.ru',
                       'hkjhkft', 'jgkkd', '576tfh']) == RESULT_DICT
