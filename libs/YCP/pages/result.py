from libs.YCP import pages
from libs.YCP.locator import *


class ResultPage(pages.YCP_base.YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_bc(self):
        self.click_element(eResultPage.bc_button)
        return pages.bc.BCMePage(self.driver)

    def select_photo_list_item(self):
        self.click_element(eResultPage.photo_list_item)
        return pages.photo_picker.PhotoPickerPage(self.driver)

    def click_share(self):
        self.click_element(eResultPage.share_button)
        return pages.share.SharePage(self.driver)

    def click_continue_editing(self):
        self.click_element(eResultPage.continue_editing)
        return pages.photo_edit.PhotoEditPage(self.driver)

    def click_home(self):
        self.click_element(eResultPage.home_button)
        return pages.launcher.LauncherPage(self.driver)

    def click_library_icon(self):
        self.click_element(eResultPage.library_icon)
        return pages.photo_picker.PhotoPickerPage(self.driver)

    def click_enhance(self):
        self.click_element_by_text('ENHANCE')
        return pages.photo_picker.PhotoPickerPage(self.driver)

    def click_get_for_free(self):
        self.click_element_by_text('Get for FREE')
        return self

    def click_create(self):
        self.click_element_by_text('CREATE')
        return self
