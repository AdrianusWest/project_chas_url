from validators import url


def validate_strings(list_of_strings: list) -> list:
    list_of_valid_urls = [elem for elem in list_of_strings if url(elem)]
    return list_of_valid_urls


def non_validate_strings(list_of_strings: list) -> str:
    list_of_non_valid_urls = [elem for elem in list_of_strings if not url(elem)]
    res = ', '.join(list_of_non_valid_urls)
    return f'Lines {res} are not URLs.'
