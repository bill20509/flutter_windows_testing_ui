from libs.YMK.locators import BackgroundLocators, PickPhotoLocators
from libs.YMK import pages
from libs.YMK.pages.photomakeup_page import PhotoMakeup


class Background(pages.photomakeup_page.PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_background_item(self, number):
        for i in range(5):
            try:
                self.select_element_by_number(BackgroundLocators.background_item, (number-1))
                break
            except(ValueError, Exception):
                self.wait_element_visible(BackgroundLocators.background_view)
                self.scroll_horizontal(BackgroundLocators.background_view)
        return self

    def click_detect(self):
        self.wait_element_visible(BackgroundLocators.background_reset)
        self.click_element(BackgroundLocators.background_reset)
        return self

    def click_brush(self):
        self.wait_element_visible(BackgroundLocators.background_brush)
        self.click_element(BackgroundLocators.background_brush)
        return self

    def click_eraser(self):
        self.wait_element_visible(BackgroundLocators.background_eraser)
        self.click_element(BackgroundLocators.background_eraser)
        return self

    def select_brush_size_1(self):
        self.wait_element_visible(BackgroundLocators.draw_size1)
        self.click_element(BackgroundLocators.draw_size1)
        return self

    def select_brush_size_2(self):
        self.wait_element_visible(BackgroundLocators.draw_size2)
        self.click_element(BackgroundLocators.draw_size2)
        return self

    def select_brush_size_3(self):
        self.wait_element_visible(BackgroundLocators.draw_size3)
        self.click_element(BackgroundLocators.draw_size3)
        return self

    def select_brush_size_4(self):
        self.wait_element_visible(BackgroundLocators.draw_size4)
        self.click_element(BackgroundLocators.draw_size4)
        return self

    def select_brush_size_5(self):
        self.wait_element_visible(BackgroundLocators.draw_size5)
        self.click_element(BackgroundLocators.draw_size5)
        return self

    def click_store(self):
        self.wait_element_visible(BackgroundLocators.download_store)
        self.click_element(BackgroundLocators.download_store)
        return pages.store_page.Store(self.driver)

    def tap_central(self):
        self.wait_element_visible(BackgroundLocators.background_central)
        self.click_element(BackgroundLocators.background_central)
        return self

    def click_premium_item(self):
        for i in range(10):
            try:
                self.wait_element_visible(BackgroundLocators.premium_icon)
                self.click_element(BackgroundLocators.premium_icon)
                break
            except:
                self.wait_element_visible(BackgroundLocators.background_item, 4)
                self.select_element_by_number(BackgroundLocators.background_item, 4)
        self.find_element(BackgroundLocators.premium_icon)
        return self

    def select_photo_background(self, folder, photo=1):
        self.click_element(BackgroundLocators.photo_pick_icon)
        for i in range(5):
            try:
                self.click_element_by_name(PickPhotoLocators.select_folder, folder)
                break
            except:
                self.scroll_vertical(PickPhotoLocators.album_view, speed=2000)
        for j in range(5):
            try:
                self.select_element_by_number(PickPhotoLocators.select_photo, (photo - 1))
                break
            except (ValueError, Exception):
                self.scroll_vertical(PickPhotoLocators.photo_view)
        return self

    def check_dailog(self):
        try:
            self.wait_element_visible(BackgroundLocators.no_thanks_button)
            self.click_element(BackgroundLocators.no_thanks_button)
        except (ValueError, Exception):
            pass
        return self