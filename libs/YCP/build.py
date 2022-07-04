from libs.YCP import locator
from libs.YCP import pages
import inspect

# name = pattern.sub('_', name).lower()
# eXxxxxxPage -> XxxxxPage
# every element el in eXxxxxPage -> click_el() in XxxxPage
# xxx_button -> click_xxx
template = """
    def click_{}(self):
        self.click_element({}.{})
        return class

"""
module_map = {}  # name to module, k v
page_to_module_path = {}  # class name to module path
page_to_func = {}  # [Str] class name to [str list]: function
for k, v in pages.__dict__.items():
    if k.startswith("_") or k == "YCP_base":
        continue
    module_map[k] = v

    for i, j in v.__dict__.items():
        if not i.startswith("_") and not i.startswith('e') and inspect.isclass(j):
            page_to_module_path[i] = v.__file__
            page_to_func[i] = []
            for m, n in j.__dict__.items():
                if not m.startswith('_'):
                    page_to_func[i].append(m)


for k, v in locator.__dict__.items():
    if k.startswith('e'):
        for i, j in v.__dict__.items():
            org_id = i
            i = i.replace('_button', '')
            if not i.startswith('_') \
                    and not i.endswith('bar')\
                    and "click_" + i not in page_to_func[k[1:]] \
                    and "scroll_" + i not in page_to_func[k[1:]] \
                    and "select_" + i not in page_to_func[k[1:]]:
                print(k, i)
                with open(page_to_module_path[k[1:]], encoding="utf-8") as f:
                    lines = f.readlines()

                python_code = template.format(i, k, org_id)
                print(python_code)
                flag = False
                with open(page_to_module_path[k[1:]], 'w', encoding="utf-8") as f:
                    for i in range(len(lines)):
                        if flag == True:
                            break
                        if('class ' + k[1:] in lines[i]):
                            for j in range(i, len(lines)):
                                init_function = """super().__init__"""
                                if(init_function in lines[j]):
                                    f.writelines(lines[0:j+1])
                                    f.writelines(python_code)
                                    f.writelines(lines[j+2:])
                                    flag = True
                                    print('replace')
                                    break
