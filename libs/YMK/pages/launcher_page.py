from libs.YMK.locators import LauncherLocators
from libs.YMK import pages


class Launcher(pages.YMK_base.YMKbase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_makeupcam_button(self):
        self.click_element(LauncherLocators.Makeup_cam)
        return pages.makeupcam_page.MakeupCam(self.driver)
