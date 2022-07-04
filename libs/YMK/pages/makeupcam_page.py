from libs.YMK.locators import MakeupCamLocators
from libs.YMK import pages


class MakeupCam(pages.YMK_base.YMKbase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_BIPA_agree(self):
        self.click_element(MakeupCamLocators.BIPA_Agree)
        return self

    def click_back_launcher(self):
        self.click_element(MakeupCamLocators.Back)
        return pages.launcher_page.Launcher(self.driver)
