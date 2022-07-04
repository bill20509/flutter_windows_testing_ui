from libs.YMK.locators import PickPhotoLocators, BodyTunerLocators
from libs.YMK import pages


class BodyTuner(pages.YMK_base.YMKbase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    # Select folder and photo (folder name, photo number)
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

    def click_tutorial_ok(self):
        self.check_element_is_displayed(BodyTunerLocators.enhancer_slim_ok)
        return self

    def select_tool(self, name):
        try:
            self.click_element_by_name(BodyTunerLocators.toolbar, name)
        except (ValueError, Exception):
            self.scroll_horizontal(BodyTunerLocators.toolbar_view)
        return self

    def adjust_intensity_to_right(self):
        self.slidebar_to_right(BodyTunerLocators.effect_seekbar)
        return self

    def adjust_intensity_to_left(self):
        self.slidebar_to_left(BodyTunerLocators.effect_seekbar)
        return self

    def click_x(self):
        self.click_element(BodyTunerLocators.X_button)
        return pages.photomakeup_page.PhotoMakeup(self.driver)

    def click_v(self):
        self.click_element(BodyTunerLocators.V_button)
        return pages.photomakeup_page.PhotoMakeup(self.driver)

    def click_undo(self):
        self.click_element(BodyTunerLocators.undo)
        return self

    def click_redo(self):
        self.click_element(BodyTunerLocators.redo)
        return self

    def click_clear(self):
        self.click_element(BodyTunerLocators.clear)
        return self

    def smartbrush_onoff(self):
        self.click_element(BodyTunerLocators.smart_brush)
        return self

    def click_brush(self):
        self.click_element(BodyTunerLocators.brush)
        return self

    def click_eraser(self):
        self.click_element(BodyTunerLocators.eraser)
        return self

    def click_detect(self):
        self.click_element(BodyTunerLocators.detect)
        return self

    def waiting_cursor(self):
        self.wait_element_invisible(BodyTunerLocators.waiting_cursor)
        return self
