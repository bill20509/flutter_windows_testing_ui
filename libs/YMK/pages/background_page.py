from libs.YMK.locators import PickPhotoLocators, BackgroundLocators
from libs.YMK import pages


class Background(pages.YMK_base.YMKbase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def pick_photo(self, folder, photo=1):
        for i in range(5):
            try:
                self.click_element_by_name(PickPhotoLocators.select_folder, folder)
                break
            except (ValueError, Exception):
                self.scroll_vertical(PickPhotoLocators.album_view)
        for j in range(5):
            try:
                self.select_element_by_number(PickPhotoLocators.select_photo, (photo-1))
                break
            except (ValueError, Exception):
                self.scroll_vertical(PickPhotoLocators.photo_view)
        return self

    def select_background(self, number):
        for i in range(5):
            try:
                self.select_element_by_number(BackgroundLocators.background_item, number)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(BackgroundLocators.background_view)
        return self

    def click_detect(self):
        self.click_element(BackgroundLocators.background_reset)
        return self

    def click_brush(self):
        self.click_element(BackgroundLocators.background_brush)
        return self

    def click_eraser(self):
        self.click_element(BackgroundLocators.background_eraser)
        return self

    def select_brush_size_1(self):
        self.click_element(BackgroundLocators.draw_size1)
        return self

    def select_brush_size_2(self):
        self.click_element(BackgroundLocators.draw_size2)
        return self

    def select_brush_size_3(self):
        self.click_element(BackgroundLocators.draw_size3)
        return self

    def select_brush_size_4(self):
        self.click_element(BackgroundLocators.draw_size4)
        return self

    def select_brush_size_5(self):
        self.click_element(BackgroundLocators.draw_size5)
        return self

    def click_store(self):
        return pages.store_page.Store(self.driver)

