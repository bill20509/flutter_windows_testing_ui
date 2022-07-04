from libs.YCP import pages
from libs.YCP.locator import *


class LauncherPage(pages.YCP_base.YCPBase):

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_scroll_down_hint(self):
        self.click_element(eLauncherPage.scroll_down_hint_button)
        return self

    def click_settings(self):
        self.click_element(eLauncherPage.settings_button)
        return pages.settings.SettingsPage(self.driver)

    def click_premium(self):
        self.click_element(eLauncherPage.premium_button)
        return pages.settings.SettingsPage(self.driver)

    def click_app_logo(self):
        self.click_element(eLauncherPage.app_logo)
        return self

    def click_camera(self):
        self.click_element(eLauncherPage.camera_button)
        return pages.camera.CameraPage(self.driver)

    def click_photo_edit(self):
        self.click_element(eLauncherPage.photo_edit_button)
        return pages.photo_picker.PhotoPickerPage(self.driver)

    def click_beautify(self):
        self.click_element(eLauncherPage.beautify_button)
        return pages.beautify.BeautifyPage(self.driver)

    def click_collage(self):
        self.click_element(eLauncherPage.collage_button)
        return pages.collage.CollagePage(self.driver)

    def click_discovery(self):
        self.click_element(eLauncherPage.scroll_down_hint)
        self.click_element(eLauncherPage.discovery_button)
        return pages.discovery.DiscoveryPage(self.driver)

    def click_store(self):
        self.click_element(eLauncherPage.scroll_down_hint)
        self.click_element(eLauncherPage.store_button)
        return pages.store.StorePage(self.driver)

    def click_how_to_see_all(self):
        self.click_element(eLauncherPage.scroll_down_hint)
        self.click_element(eLauncherPage.how_to_see_all)
        return pages.how_to.HowToPage(self.driver)

    def click_trending_see_all(self):
        self.click_element(eLauncherPage.scroll_down_hint)
        self.click_element(eLauncherPage.trending_see_all)
        return pages.community_trending.CommunityTrendingPage(self.driver)

    def click_photo_challenge_see_all(self):
        self.click_element(eLauncherPage.scroll_down_hint)
        self.click_element(eLauncherPage.scroll_down_hint)
        self.click_element(eLauncherPage.photo_challenge_see_all)
        return pages.photo_challenge.PhotoChallengePage(self.driver)
