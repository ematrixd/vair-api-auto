from LIBS.requests_util import Requests

class DataMeta(type):

    def __setattr__(cls, name, value):
        if callable(value):
            pass
            
        super().__setattr__(name, value)

    def __getattribute__(self, __name: str):
        return super().__getattribute__(__name)


class Data(metaclass=DataMeta):
    pass


class Swagger():

    def __init__(self, url, login, password, url_swagger):
        self.data = []
        self.index = 0
        self.d = Data()
        self.method = ''
        self.task_id = ''
        self.request = Requests(url=url, login=login, password=password)
        self.request.token_authentication_api()
        data_swagger = self.request.get(url_swagger)
        for key, value in data_swagger['paths'].items():
            name = key.replace('-', '_').replace('{', '').replace('}', '')
            method_name = '_'.join(list(filter(None, name.split('/')))[2:])
            required_fields = value.get('required', [])
            method = self.create_method(method_name, required_fields, value.keys())
            setattr(Data, method_name.upper(), key)
            setattr(Data, method_name, method)

    def _get_for_key(self, data, *args, recursive=False):
        if isinstance(data, dict):
            data = [data]
        for d in data:
            if not recursive:
                self.data.append({})
            for key, value in d.items():
                if isinstance(value, dict):
                    self._get_for_key([value], *args, recursive=True)
                if key in args:
                    self.index = len(self.data) - 1
                    self.data[self.index].update({key: value})
        return self.data

    def create_method(swagger, name, required, method):
        def dynamic_method(self, *args, **kwargs):
            if 'get' in method:
                data = swagger.request.get(path=kwargs['path'])
                return data
            if 'post' in method:
                path = kwargs['path']
                del kwargs['path']
                data = swagger.request.post(kwargs, path=path)
                return data

        return dynamic_method
    
    def get_all_methods(self):
        methods = []
        for data in dir(self.d):
            if data and not data.isupper() and not data.startswith('_'):
                methods.append(data)
        return methods

    def start_method(self, url, *args, **kwargs):
        self.data = []
        self.index = 0
        path = getattr(self.d, url.upper())
        if kwargs.get('path', False):
            path = kwargs['path']
            del kwargs['path']
        data = getattr(self.d, url)(path=path, *args, **kwargs)
        if not data.get('data', False) and data.get('id', False):
            self.task_id = data['id']
        if isinstance(data, dict) and data.get('data', {}):
            return self._get_for_key(data['data'], *args)
