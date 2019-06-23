import yaml

import example

with open('example/example.yml') as f:
    yaml_content = yaml.load(f)

dataset = example.DatasetConfig()
assert dataset.root == yaml_content['dataset']['root']
assert dataset.step == yaml_content['dataset']['step']
assert dataset.parallel == yaml_content['dataset']['parallel']
assert dataset.export() == yaml_content['dataset']

class_info = example.ClassInfoConfig()
assert class_info.name == yaml_content['class_info']['name']
assert class_info.students == yaml_content['class_info']['students']
assert class_info.export() == yaml_content['class_info']

class_info.name = 'Anything'
class_info.students = []
assert class_info.export() != yaml_content['class_info']

class_info.load(yaml_content['class_info'])
assert class_info.export() == yaml_content['class_info']

custom_yaml = {
    'name': 'Snow',
    'students': ['319', '326']
}
class_info = example.ClassInfoConfig(dictionary=custom_yaml)
assert class_info.name == custom_yaml['name']
assert class_info.students == custom_yaml['students']
assert class_info.export() == custom_yaml

students_yaml = [
    {
        'name': 'Alice',
        'age': 20
    },
    {
        'name': 'Bob',
        'age': 22
    }
]

students = example.StudentsConfig.load_list(students_yaml)
assert len(students) == 2
for student, dictionary in zip(students, students_yaml):
    assert isinstance(student, example.StudentsConfig)
    assert student.export() == dictionary
