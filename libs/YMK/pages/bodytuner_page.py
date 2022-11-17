from libs.YMK.locators import BodyTunerLocators
from libs.YMK import pages


class BodyTuner(pages.photomakeup_page.PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def check_tutorial(self):
        self.wait_element_visible(BodyTunerLocators.tutorial_dialog)
        return self

    def click_tutorial_ok(self):
        self.click_element(BodyTunerLocators.tutorial_OK)
        return self

    def select_tool(self, name):
        for i in range(10):
            try:
                self.click_element_by_name(BodyTunerLocators.toolbar, name)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(BodyTunerLocators.toolbar_view)
        return BodyTuner(self.driver)

    def adjust_intensity_to_right(self):
        self.slidebar_to_right(BodyTunerLocators.effect_seekbar)
        return self

    def adjust_intensity_to_left(self):
        self.slidebar_to_left(BodyTunerLocators.effect_seekbar)
        return self

    def click_x(self):
        self.click_element(BodyTunerLocators.X_button)
        return self

    def click_v(self):
        self.click_element(BodyTunerLocators.V_button)
        return self

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
