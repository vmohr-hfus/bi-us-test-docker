import pandas
import datetime

_INPUT_FILE_PATH = '/data/input_data/'
_OUTPUT_FILE_PATH = '/data/output_data/'


class simpleetl(object):
    def input(self):
        input_file = _INPUT_FILE_PATH + 'data.csv'
        df = pandas.read_csv(input_file, sep='|')

        return df

    def main(self, df):
        df['current_date'] = datetime.datetime.now().strftime('%Y-%m-%d')

        return df

    def output(self, df, args):
        output_file = _OUTPUT_FILE_PATH + args.output_name

        df.to_csv(output_file, sep=',', encoding='utf-8')
        exit(1)

    def run(self, args):
        df = self.input()
        df = self.main(df)
        self.output(df, args)
