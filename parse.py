from os import listdir
from os.path import isfile, join
import json
from importlib.machinery import SourceFileLoader


def parse(name):
    mypath = './tests/' + name + '/'
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    test_case = []
    for file_name in files:
        if(file_name.startswith('_')):
            continue
        item = {"case_name": file_name, "path": mypath + file_name, "class": "Test",
                "cases": []}
        foo = SourceFileLoader("module.test", mypath + file_name).load_module()
        for my_class in dir(foo):
            if(my_class.startswith('Test')):
                item['class'] = my_class
        case_class = getattr(foo, item['class'])
        for case in dir(case_class):
            if(case.startswith('test')):

                item["cases"].append(case)
        test_case.append(item)
    with open(name + "_cases.json", "w") as outfile:
        json.dump(test_case, outfile)


parse('YCP')
parse('YMK')
print('Reload ready')
