import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Check for URLs')
    parser.add_argument('-s',
                        '--strings_to_check',
                        help='List of links for processing',
                        nargs='+',
                        type=str)

    return parser.parse_args()
