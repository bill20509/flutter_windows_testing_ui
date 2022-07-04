from libs.YMK.locators import PickPhotoLocators
from libs.YMK import pages


class PhotoPicker(pages.YMK_base.YMKbase):
    def __init__(self, driver, receive_page):
        super().__init__(driver)
        self.receive_page = receive_page

    # TODO: return page object?
    # Select folder and photo (folder name, photo number)
    # def pick_photo2(self, folder, photo=1):
    #     self.click_element_by_name(PickPhotoLocators.select_folder, folder)
    #     self.select_element_by_number(PickPhotoLocators.select_photo, (photo-1))
    #     print(self.send_page, self.receive_page)
    #     return self.receive_page(self.driver)
