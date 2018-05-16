import pandas
import datetime

_FILE_PATH = '/data/'

class simpleetl(object):
    def input(self):
        input_file = _FILE_PATH + 'data.csv'
        df = pandas.read_csv(input_file, sep='|')

        return df

    def main(self, df):
        df['current_date'] = datetime.datetime.now().strftime('%Y-%m-%d')

        return df

    def output(self, df):
        output_file = _FILE_PATH + 'data_w_date.csv'

        df.to_csv(output_file, sep=',', encoding='utf-8')
        exit(1)

    def run(self):
        df = self.input()
        df = self.main(df)
        self.output(df)