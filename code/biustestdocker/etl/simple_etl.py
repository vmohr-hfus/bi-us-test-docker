import datetime

class MyTransformation(object):
    def transform_data(self, data):
        data['current_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
        return data

