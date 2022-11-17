

class Element:
    def __init__(self, element_id, element_type, desc=""):
        self.element_id = element_id
        self.element_type = element_type
        if desc == "":
            self.element_desc = str(self.element_id)
        else:
            self.element_desc = desc

        assert element_type in ["id", "xpath", "text", "class name"]
