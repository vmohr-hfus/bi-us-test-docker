import argparse


def config_parser():
    parser = argparse.ArgumentParser(description='Output CSV Name')
    parser.add_argument(
        '--output_name',
        dest='output_name',
        help='CSV Output File Name',
        required=True
    )

    return parser

