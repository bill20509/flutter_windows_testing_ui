from libs.YMK.locators import CloudAlbumViewLocators, MeLocators
from libs.YMK import pages


class CloudAlbumView(pages.YMK_base.YMKbase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_back_button(self):
        self.wait_element_visible(CloudAlbumViewLocators.Back_button)
        self.click_element(CloudAlbumViewLocators.Back_button)
        return self

    def click_edit_button(self):
        self.wait_element_visible(CloudAlbumViewLocators.Edit_button)
        self.click_element(CloudAlbumViewLocators.Edit_button)
        return self

    def click_download_button(self):
        self.wait_element_visible(CloudAlbumViewLocators.Download_button)
        self.click_element(CloudAlbumViewLocators.Download_button)
        return self

    def click_delete_button(self):
        self.wait_element_visible(CloudAlbumViewLocators.Delete_button)
        self.click_element(CloudAlbumViewLocators.Delete_button)
        return self

    def select_live_makeup_button(self):
        self.wait_element_visible(CloudAlbumViewLocators.Live_makeup_button)
        self.click_element(CloudAlbumViewLocators.Live_makeup_button)
        return pages.makeupcam_page.MakeupCam(self.driver)

    def select_photo_makeup_button(self):
        self.wait_element_visible(CloudAlbumViewLocators.Photo_makeup_button)
        self.click_element(CloudAlbumViewLocators.Photo_makeup_button)
        return pages.photomakeup_page.PhotoMakeup(self.driver)

    def check_download_completed(self):
        self.wait_element_visible(CloudAlbumViewLocators.Download_completed, timeout=60)
        self.find_element(CloudAlbumViewLocators.Download_completed)
        return self

    def select_delete(self):
        self.wait_element_visible(CloudAlbumViewLocators.Dialog_delete_button)
        self.click_element(CloudAlbumViewLocators.Dialog_delete_button)
        return self

