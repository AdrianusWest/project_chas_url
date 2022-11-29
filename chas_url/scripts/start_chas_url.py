#!/usr/bin/env python
import sys

from chas_url.checking_for_urls import check_urls
from chas_url.cli import parse_args


def main():
    args = parse_args()
    try:
        print(check_urls(args.strings_to_check))
    except Exception:
        print(f'Enter the lines, please.')
        sys.exit(1)
    else:
        print(f'Address verification is complete.')


if __name__ == '__main__':
    main()
