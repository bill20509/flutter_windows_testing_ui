from libs.YCP import pages
from libs.YCP.locator import *


class PhotoPickerPage(pages.YCP_base.YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_v(self):
        self.click_element(ePhotoPickerPage.v_button)
        # TODO: shoud return to right page
        return self

    def click_camera(self):
        self.click_element(ePhotoPickerPage.camera_button)
        return self

    def select_album_item(self, name: str):
        self.click_element_by_text(name)
        return self

    def select_photo_item(self, num: int):
        self.select_element_by_number(ePhotoPickerPage.photo_item, num)
        # TODO: probably need to specify which page be returnd
        return pages.photo_edit.PhotoEditPage(self.driver)

    def select_photo_magnifier_icon(self, num: int):
        self.select_element_by_number(
            ePhotoPickerPage.photo_magnifier_icon, num)
        return pages.single_photo.SinglePhotoPage(self.driver)

    def click_bc(self):
        self.click_element(ePhotoPickerPage.bc_button)
        # TODO: should return to bc page
        return self

    def click_delete(self):
        self.click_element(ePhotoPickerPage.delete_button)
        return self

    def click_delete_photo(self):
        self.click_element(ePhotoPickerPage.delete_photo_button)
        self.click_element_by_text("DELETE")
        # self.click_element_by_text("Allow")
        return self

    def click_delete_cancel(self):
        self.click_element(ePhotoPickerPage.delete_cancel_button)
        return self
