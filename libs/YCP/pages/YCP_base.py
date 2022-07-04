from libs.YCP import pages
from libs.base import BasePage
from libs.YCP.locator import *
from appium import webdriver
import time


class YCPDeeplink:
    launcher = "ycp://launcher/"

    photo_edit_with_photo = "ycp://action/pickphoto?editImageId=YouCamPerfectSample-18"
    photo_edit_perspective = "ycp://action/pickphoto/perspective?rotate=-30&horizontal=-30&vertical=-30&editImageId=YouCamPerfectSample-18"
    photo_edit_mirror = "ycp://action/pickphoto/mirror?editImageId=YouCamPerfectSample-18"


class YCPBase(BasePage):

    def __init__(self, driver=webdriver.Remote):
        super().__init__(driver)

    def deeplink_to_launcher(self):
        self.deeplink(YCPDeeplink.launcher)
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
