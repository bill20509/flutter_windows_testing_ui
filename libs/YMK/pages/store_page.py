from libs.YMK import pages


class Store(pages.YMK_base.YMKbase):
    def __init__(self, driver):
        super().__init__(driver)

    def click_looks(self):
        self.click_element_by_text("Looks")
        return self

    def click_download(self):
        self.click_element_by_text("Download")
        return self

    def click_use(self):
        self.click_element_by_text("Use")
        return self

    def select_premium_collection(self):
        self.click_element_by_text("9a4a7288-61e4-49af-8f62-15cc56c86b71")
        return self
