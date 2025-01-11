#!/usr/bin/python3
"""
This will be the "base" for all other classes in this project. the goal of it is to manage id attribute in all our future classes and avoid duplicaing the same code
"""
import json
import os
import csv

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0 or list_dictionaries == None:
            return []
        else:
            json_list = []
            for rep in list_dictionaries:
                json_list.append(rep)
            return json.dumps(json_list)

    @classmethod
    def save_to_file(cls, list_objs):
        rep_list = []
        if list_objs == None or len(list_objs) == 0:
            with open(self.__class__.__name__ + ".json", "w") as f:
                f.write('[]')
        else:
            for rep in list_objs:
                rep_list.append(rep.__dict__)
        rep_list = Base.to_json_string(rep_list)

        with open(cls.__name__ + ".json", "w") as f:
            f.write(rep_list)

    @staticmethod
    def from_json_string(json_string):
        if json_string == None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        new = cls(1,1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        if os.path.exists(cls.__name__ + ".json"):
            loaded = ""
            list_of_instances =[]
            with open(cls.__name__ + ".json") as f:
                content = f.read()
                loaded = cls.from_json_string(content)

            for dic in loaded:
                add = cls.create(**dic)
                list_of_instances.append(add)
            return list_of_instances
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        fields = list(list_objs[0].__dict__.keys())
        rows = []

        for obj in list_objs:
            rows.append(obj.__dict__.values())

        with open(cls.__name__ + '.csv', 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(fields)
            csv_writer.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        with open(cls.__name__ + '.csv', 'r') as f:
            csv_reader = csv.reader(f)
            list_obj = []

            next(csv_reader)

            for l in csv_reader:

                new = cls(1,1)
                if cls.__name__ == 'Square':
                    del l[1]
                new.update(*l)
                list_obj.append(new)
            return list_obj
