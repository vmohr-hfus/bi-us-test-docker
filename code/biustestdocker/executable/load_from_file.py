import psycopg2

from biustestdocker.common import parser_config
from biustestdocker.etl.simple_etl import MyTransformation

import pandas
import datetime

_INPUT_FILE_PATH = '/data/input_data/'
_OUTPUT_FILE_PATH = '/data/output_data/'


class SimpleEtl(object):

    def input(self):
        input_file = _INPUT_FILE_PATH + 'data.csv'
        df = pandas.read_csv(input_file, sep='|')

        return df

    def main(self, df):

        transformation = MyTransformation()

        df = transformation.transform_data(df)

        return df

    def output(self, df, args):
        output_file = (_OUTPUT_FILE_PATH + args.output_name + "_"
                       + datetime.datetime.now().strftime('%Y_%m_%d')
                       + ".csv")

        df.to_csv(output_file, sep=',', encoding='utf-8')
        exit(1)

    def run(self, args):
        df = self.input()
        df = self.main(df)
        self.output(df, args)


if __name__ == '__main__':
    parser = parser_config.config_parser()
    args = parser.parse_args()

    my_etl = SimpleEtl()
    my_etl.run(args)
