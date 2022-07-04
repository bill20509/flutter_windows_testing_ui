from libs.YCP import pages
from libs.YCP.locator import *


class CameraPage(pages.YCP_base.YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_switch_camera(self):
        self.click_element(eCameraPage.switch_camera_button)
        return self

    def click_timer(self):
        self.click_element(eCameraPage.timer_button)
        return self

    def click_more_settings(self):
        self.click_element(eCameraPage.more_settings_button)
        return self

    def click_more_autosave(self):
        self.click_element(eCameraPage.more_autosave_button)
        return self

    def click_more_timestamp(self):
        self.click_element(eCameraPage.more_timestamp_button)
        return self

    def click_more_grid(self):
        self.click_element(eCameraPage.more_grid_button)
        return self

    def click_more_blur(self):
        self.click_element(eCameraPage.more_blur_button)
        return self

    def click_more(self):
        self.click_element(eCameraPage.more_button)
        return self

    def click_mode_wave_detect(self):
        self.click_element(eCameraPage.mode_wave_detect)
        return self

    def click_mode_detect(self):
        self.click_element(eCameraPage.mode_detect)
        return self

    def click_mode_touch(self):
        self.click_element(eCameraPage.mode_touch)
        return self

    def click_mode_general(self):
        self.click_element(eCameraPage.mode_general)
        return self

    def click_mode(self):
        self.click_element(eCameraPage.mode_button)
        return self
