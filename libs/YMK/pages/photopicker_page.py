from libs.YMK.locators import PickPhotoLocators, DialogLocators
from libs.YMK import pages


class PhotoPicker(pages.YMK_base.YMKbase):
    def __init__(self, driver):
        super().__init__(driver)
        # self.receive_page = receive_page

    def check_bipa_and_close(self):
        try:
            self.wait_element_visible(DialogLocators.BIPA_Agree, timeout=5)
            self.click_element(DialogLocators.BIPA_Agree)
        except (ValueError, Exception):
            pass
        return self

    def pick_album(self, folder):
        for i in range(5):
            try:
                self.click_element_by_name(PickPhotoLocators.select_folder, folder)
                break
            except (ValueError, Exception):
                self.scroll_vertical(PickPhotoLocators.album_view, speed=2000)
        return self

    def check_photo_picker_ad(self):
        try:
            self.wait_element_visible(PickPhotoLocators.photo_picker_ad, timeout=10)
            return 1
        except (ValueError, Exception):
            return 0

    def delete_photos(self):
        self.wait_element_visible(PickPhotoLocators.delete_button)
        self.click_element(PickPhotoLocators.delete_button)
        self.select_element_by_number(PickPhotoLocators.select_photo, 0)
        self.select_element_by_number(PickPhotoLocators.select_photo, 1)
        self.click_element_by_text("Delete Items (2)")
        self.wait_element_visible(PickPhotoLocators.dialog_delete_button)
        self.click_element(PickPhotoLocators.dialog_delete_button)
        self.wait_element_visible(PickPhotoLocators.system_delete_button)
        self.click_element(PickPhotoLocators.system_delete_button)
        return self

    def pick_photo(self):
        self.wait_element_visible(PickPhotoLocators.select_photo)
        self.select_element_by_number(PickPhotoLocators.select_photo, 0)
        return self

    def click_photopicker_back(self):
        self.wait_element_visible(PickPhotoLocators.Back_to_album)
        self.click_element(PickPhotoLocators.Back_to_album)
        return self

    def click_album_back(self):
        self.wait_element_visible(PickPhotoLocators.Back_to_launcher)
        self.click_element(PickPhotoLocators.Back_to_launcher)
        return self
        # return pages.launcher_page.Launcher(self.driver)

    # TODO: return page object?
    # Select folder and photo (folder name, photo number)
    # def pick_photo2(self, folder, photo=1):
    #     self.click_element_by_name(PickPhotoLocators.select_folder, folder)
    #     self.select_element_by_number(PickPhotoLocators.select_photo, (photo-1))
    #     print(self.send_page, self.receive_page)
    #     return self.receive_page(self.driver)
