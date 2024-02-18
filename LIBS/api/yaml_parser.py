import re


class YamlParser():
    def __init__(self, yaml, swagger):
        self.yaml = yaml
        self.swagger = swagger
        self.data = {}
        self.all_data = []
        self._vair_processing()

    def __is_valid_uuid(self, val):
        uuid_regex = re.compile(
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$',
            re.IGNORECASE
        )
        return bool(uuid_regex.match(val))
    
    def __vair_parser(self, value, num=0):
        for key_value, value_value in value.items():
            if '<' in value_value:
                self.data[key_value] = f'{value_value.split('<')[0]}{num+1}'
                continue
            if 'pool_id' in key_value and not self.__is_valid_uuid(value_value):
                data = self.swagger.start_method('pools', 'id', 'name')
                pool_id = [i['id'] for i in data if i['name'] == value_value][0]
                self.data[key_value] = pool_id
                continue
            if 'volume_name>' in value_value:
                data = self.swagger.start_method('volumes', 'id', 'name')
                volumes_id = [i['id'] for i in data if i['name'] == value_value.split('>')[-1]][0]
                self.data[key_value] = volumes_id
                continue
            # if '>' in value_value:
            #     cycle_name = value_value.split('>')
            #     for name_value in cycle_name:
                
            self.data[key_value] = value_value

    def _vair_processing(self):
        for key, value in self.yaml.items():
            if '|' in key:
                name = key.split('|')
                cycle = int(name[-1])
                for num in range(cycle):
                    self.data = {}
                    self.__vair_parser(value, num)
                    self.all_data.append({name[0]: self.data})
            else:
                self.__vair_parser(value)
                self.all_data.append({key: self.data})
