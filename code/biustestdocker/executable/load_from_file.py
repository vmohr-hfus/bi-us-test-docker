import psycopg2

from biustestdocker.etl import simple_etl
from biustestdocker.common import parser_config

parser = parser_config.config_parser()

if __name__ == '__main__':
    args = parser.parse_args()

    my_etl = simple_etl.simpleetl()
    my_etl.run(args)


#python load_from_file.py --output_name TESTOUT.csv
#ls /data/output_data/