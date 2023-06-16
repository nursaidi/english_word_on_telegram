import json
import datetime

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {
                'value': obj.strftime('%d/%m/%Y %H:%M:%S'),
                '__datetime__': True
            }
        elif isinstance(obj, datetime.date):
            return {
                'value': obj.strftime('%d/%m/%Y'),
                '__date__': True
            }
        return json.JSONEncoder.default(self, obj)

data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'birthday': datetime.date(1986, 9, 29),
    'hired_at': datetime.datetime(2006, 9, 29, 12, 30 ,5),
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}

json_data = json.dumps(data, cls=ComplexEncoder)
print(json_data)