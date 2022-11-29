from chas_url.formatter import formatting
from chas_url.url_poll import url_poll
from chas_url.validator import non_validate_strings
from chas_url.validator import validate_strings


def check_urls(list_of_all_urls: list):
    """Возвращает JSON, состоящий из ссылок и информации о доступных методах.

    Args:
        list_of_all_urls: список передаваемых строк.

    Возвращает:
        JSON, состоящий из ссылок и информации о доступных методах.
    """
    list_of_valid_urls = validate_strings(list_of_all_urls)
    poll_dict = {}
    for valid_url in list_of_valid_urls:
        poll_dict[valid_url] = url_poll(valid_url)
    print(non_validate_strings(list_of_all_urls))
    if poll_dict:
        return formatting(poll_dict)
    else:
        return f'No URL to process.'
