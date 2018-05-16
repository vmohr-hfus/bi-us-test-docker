import pandas
import psycopg2
import datetime

_FILE_PATH = '/data/'





if __name__ == '__main__':
    my_etl = simpleetl()
    my_etl.run()