from chas_url.checking_for_urls import check_urls

from tests.fixtures.expected_dics import RESULT_DICT


def test_check_with_urls_and_str():
    assert check_urls(['https://ru.hexlet.io/', 'https://mail.ru',
                       'hkjhkft', 'jgkkd', '576tfh']) == RESULT_DICT


def test_check_without_urls_():
    assert check_urls(['hkjhkft', 'jgkkd', '576tfh']) == 'No URL to process.'
