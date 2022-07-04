from libs.YMK.locators import AgingLocators
from libs.YMK import pages


class Aging(pages.YMK_base.YMKbase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_Tryit(self):
        self.click_element(AgingLocators.Try_it)
        return self

    def choose_photo(self):
        self.click_element(AgingLocators.Choose_photo)
        return self

    def click_photo(self):
        self.click_element(AgingLocators.Choose_photo)
        return self

    def click_Start(self):
        self.click_element(AgingLocators.Start)
        return self

    def click_Allow(self):
        self.click_element(AgingLocators.Allow)
        return self

    def click_Back(self):
        self.click_element(AgingLocators.Back)
        return pages.launcher_page.Launcher(self.driver)
