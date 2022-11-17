from libs.YCP import pages
from libs.base import BasePage
from libs.YCP.locator import *
from appium import webdriver
import time


class YCPDeeplink:
    launcher = "ycp://launcher/"
    hot_my_stickers = "ycp://action/pickphoto/sticker?my_sticker=true&editImageId=default_photo&is_launcher_featured=true"
    hot_removal = "ycp://action/pickphoto/removal?editImageId=default_photo&is_launcher_featured=true"
    hot_wraparound = "ycp://action/pickphoto/photo_animation?editImageId=default_photo&tab=wraparound&wraparound_guid=PF_Wraparound_line&is_launcher_featured=true"
    hot_change_background = "ycp://action/pickphoto/changebackground?editImageId=default_photo&is_launcher_featured=true"
    hot_template = "ycp://action/pickphoto/use_template?editImageId=default_photo&is_launcher_featured=true"
    photo_edit_with_photo = "ycp://action/pickphoto?editImageId=YouCamPerfectSample-18"
    photo_edit_perspective = "ycp://action/pickphoto/perspective?rotate=-30&horizontal=-30&vertical=-30&editImageId=YouCamPerfectSample-18"
    photo_edit_mirror = "ycp://action/pickphoto/mirror?editImageId=YouCamPerfectSample-18"


class YCPBase(BasePage):

    def __init__(self, driver=webdriver.Remote):
        super().__init__(driver)

    def deeplink_to_launcher(self):
        self.deeplink(YCPDeeplink.launcher)
        return pages.launcher.LauncherPage(self.driver)

    def deeplink_hot_wraparound(self):
        self.deeplink(YCPDeeplink.hot_wraparound)
        return pages.launcher.LauncherPage(self.driver)

    def deeplink_hot_removal(self):
        self.deeplink(YCPDeeplink.hot_removal)
        return pages.launcher.LauncherPage(self.driver)

    def deeplink_hot_my_stickers(self):
        self.deeplink(YCPDeeplink.hot_my_stickers)
        return pages.launcher.LauncherPage(self.driver)

    def deeplink_hot_template(self):
        self.deeplink(YCPDeeplink.hot_template)
        return pages.launcher.LauncherPage(self.driver)

    def deeplink_hot_change_background(self):
        self.deeplink(YCPDeeplink.hot_change_background)
        return pages.launcher.LauncherPage(self.driver)

    def deeplink_to_photo_edit(self):
        """Deeplink to photo edit lobby with image YouCamPerfectSample-18

        Returns:
           PhotoEditPage
        """
        self.deeplink(YCPDeeplink.photo_edit_with_photo)
        self.find_element_by_text("Tools")
        self.find_element_by_text("Effects")
        self.find_element_by_text("Animation")
        return pages.photo_edit.PhotoEditPage(self.driver)

    def deeplink_to_persprctive(self):
        self.deeplink(YCPDeeplink.photo_edit_perspective)
        self.find_element_by_text("Vertical")
        self.find_element_by_text("Horizontal")
        self.find_element_by_text("Rotate")
        return pages.photo_edit.PerspectivePage(self.driver)

    def deeplink_to_mirror(self):
        self.deeplink(YCPDeeplink.photo_edit_mirror)
        self.find_element_by_text("Mirror")
        return pages.photo_edit.MirrorPage(self.driver)

    def wait_progress_bar(self):
        self.wait_element_invisible(progress_bar)
        return self

    def wait_loading_panel(self):
        self.wait_element_invisible(loading_panel)
        return self

    def swipe_element_to_mid(self, element: Element):
        device_size = self.driver.get_window_size()
        device_x_mid = device_size['width']/3
        device_y_mid = device_size['height']/2
        e = self.driver.find_element(
            element.element_type, element.element_id)
        m_x = int(e.location["x"] + e.size["width"] / 3)
        m_y = int(e.location["y"] + e.size["height"] / 2)
        self.swipe(m_x, m_y, device_x_mid, device_y_mid, 1000)
        return self

    def draw_on_photo(self, x1: float, y1: float, x2: float, y2: float):

        el = self.driver.find_element(
            ePhotoEditTemplate.photo_view.element_type, ePhotoEditTemplate.photo_view.element_id)
        self.swipe(el.size["width"]*x1, el.size['height']*y1,
                   el.size['width']*x2, el.size['height']*y2, 1000)
        return self
