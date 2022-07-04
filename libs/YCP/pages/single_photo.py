from libs.YCP import pages
from libs.YCP.locator import *


class SinglePhotoPage(pages.YCP_base.YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_share(self):
        self.click_element(eSinglePhotoPage.share_button)
        return pages.share.SharePage(self.driver)

    def click_beautify(self):
        self.click_element(eSinglePhotoPage.beautify_button)
        return pages.photo_edit.PhotoBeautifyPage(self.driver)

    def click_edit(self):
        self.click_element(eSinglePhotoPage.edit_button)
        return pages.photo_edit.PhotoEditPage(self.driver)

    def click_delete(self):
        self.click_element(eSinglePhotoPage.delete_button)
        return self

    def click_dialog_delete(self):
        self.click_element(eSinglePhotoPage.dialog_delete)
        return pages.photo_picker.PhotoPickerPage(self.driver)

    def click_dialog_cancel(self):
        self.click_element(eSinglePhotoPage.dialog_cancel)
        return self
