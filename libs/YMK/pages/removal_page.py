from libs.YMK.locators import RemovalLocators
from libs.YMK import pages


class Removal(pages.photomakeup_page.PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def check_alert_dialog(self):
        try:
            self.wait_element_visible(RemovalLocators.quality_alert_ok)
            self.click_element(RemovalLocators.quality_alert_ok)
            self.message("Quality Alert dialog shown!")
            self.message("Clicked OK!")
        except (ValueError, Exception):
            self.message("Quality Alert dialog not shown!")
        return self

    def click_brush(self):
        self.wait_element_visible(RemovalLocators.brush_button)
        self.click_element(RemovalLocators.brush_button)
        self.message("Using brush!")
        return self

    def click_eraser(self):
        self.wait_element_visible(RemovalLocators.eraser_button)
        self.click_element(RemovalLocators.eraser_button)
        self.message("Using eraser!")
        return self

    def click_apply(self):
        self.wait_element_visible(RemovalLocators.apply_button)
        self.click_element(RemovalLocators.apply_button)
        self.message("Applying...!")
        self.wait_time(5)
        self.wait_element_visible(RemovalLocators.apply_button)
        self.message("Removal Applied!")
        return self

    def click_x(self):
        self.wait_element_visible(RemovalLocators.x_button)
        self.click_element(RemovalLocators.x_button)
        self.message("Clicked X!")
        return self

    def click_v(self):
        self.wait_element_visible(RemovalLocators.v_button)
        self.click_element(RemovalLocators.v_button)
        self.message("Clicked V!")
        return self

    def click_undo(self):
        self.wait_element_visible(RemovalLocators.undo_redo_panel)
        self.click_element(RemovalLocators.undo_button)
        self.message("Clicked undo!")
        return self

    def click_redo(self):
        self.wait_element_visible(RemovalLocators.undo_redo_panel)
        self.click_element(RemovalLocators.redo_button)
        self.message("Clicked redo!")
        return self

    def check_noface_dialog(self):
        try:
            self.wait_element_visible(RemovalLocators.save_button)
        except (ValueError, Exception):
            self.wait_element_visible(RemovalLocators.addface_button)
            self.message("No face detected, add face!")
            self.click_element(RemovalLocators.addface_button)
            self.wait_element_visible(RemovalLocators.addface_v_button)
            self.click_element(RemovalLocators.addface_v_button)
            self.wait_element_visible(RemovalLocators.save_button)
        return self

    def draw_on_photo(self, x1: float, y1: float, x2: float, y2: float):

        el = self.driver.find_element(RemovalLocators.removal_canvas.element_type,
                                      RemovalLocators.removal_canvas.element_id)
        self.swipe(el.size["width"]*x1, el.size['height']*y1,
                   el.size['width']*x2, el.size['height']*y2, 1000)
        self.message("Draw complete!")
        return self
        #  Use 0.1-0.9 for drawing coordinates
