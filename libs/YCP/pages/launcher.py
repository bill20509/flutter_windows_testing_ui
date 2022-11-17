
from time import time
from libs.YCP import pages
from libs.YCP.locator import *
from libs.exception import ElementMissingException


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
        for i in range(5):
            try:
                self.click_element(eLauncherPage.discovery_button)
                break
            except ElementMissingException:
                self.scroll_vertical(eLauncherPage.scroll_view)
        return pages.discovery.DiscoveryPage(self.driver)

    def click_store(self):
        for i in range(5):
            try:
                self.click_element(eLauncherPage.store_button)
                break
            except ElementMissingException:
                self.scroll_vertical(eLauncherPage.scroll_view)
        return pages.store.StorePage(self.driver)

    def click_how_to_see_all(self):
        for i in range(5):
            try:
                self.click_element(eLauncherPage.how_to_see_all)
                break
            except ElementMissingException:
                self.scroll_vertical(eLauncherPage.scroll_view)
        return pages.how_to.HowToPage(self.driver)

    def click_trending_see_all(self):
        for i in range(5):
            try:
                self.click_element(eLauncherPage.trending_see_all)
                break
            except ElementMissingException:
                self.scroll_vertical(eLauncherPage.scroll_view)
        return pages.community_trending.CommunityTrendingPage(self.driver)

    def click_photo_challenge_see_all(self):
        for i in range(5):
            try:
                self.click_element(eLauncherPage.photo_challenge_see_all)
                break
            except ElementMissingException:
                self.scroll_vertical(eLauncherPage.scroll_view)

        return pages.photo_challenge.PhotoChallengePage(self.driver)

    def click_photo_challenge_see_all(self):
        for i in range(5):
            try:
                self.click_element(eLauncherPage.template_see_all)
                break
            except ElementMissingException:
                self.scroll_vertical(eLauncherPage.scroll_view)

        return pages.photo_challenge.PhotoChallengePage(self.driver)

    def _find_hot_feature(self):
        for i in range(5):
            try:
                self.find_element(eLauncherPage.hot_feature_list)
                break
            except ElementMissingException:
                self.scroll_vertical(eLauncherPage.scroll_view)
        self.swipe_element_to_mid(eLauncherPage.hot_feature_list)
        return self

    def click_hot_feature_collage(self):
        self._find_hot_feature()
        self.click_element_in_list('Collage', eLauncherPage.hot_feature_list)
        return self

    def click_hot_feature_removal(self):
        self._find_hot_feature()
        self.click_element_in_list('Removal', eLauncherPage.hot_feature_list)
        return pages.photo_edit.RemovalPage(self.driver)

    def click_hot_feature_bodytuner(self):
        self._find_hot_feature()
        self.click_element_in_list(
            'Body Tuner', eLauncherPage.hot_feature_list)
        return self

    def click_hot_feature_templates(self):
        self._find_hot_feature()
        self.click_element_in_list('Templates', eLauncherPage.hot_feature_list)
        return pages.photo_edit.TemplatePage(self.driver)

    def click_hot_feature_face_shaper(self):
        self._find_hot_feature()
        self.click_element_in_list(
            'Face Shaper', eLauncherPage.hot_feature_list)
        return self

    def click_hot_feature_wraparound(self):
        self._find_hot_feature()
        self.click_element_in_list(
            'Wraparound', eLauncherPage.hot_feature_list)
        return pages.photo_edit.AnimationPage(self.driver)

    def click_hot_feature_change_background(self):
        self._find_hot_feature()
        self.click_element_in_list(
            'Chnage Background', eLauncherPage.hot_feature_list)
        return pages.photo_edit.ChangeBackgroundPage(self.driver)

    def click_hot_feature_my_stickers(self):
        self._find_hot_feature()
        self.click_element_in_list(
            'My Stickers', eLauncherPage.hot_feature_list)
        return pages.photo_edit.StickerPage(self.driver)

    def click_hot_feature_video_edit(self):
        self._find_hot_feature()
        self.click_element_in_list(
            'Viedo Edit', eLauncherPage.hot_feature_list)
        return self

    def click_hot_feature_makeup(self):
        self._find_hot_feature()
        self.click_element_in_list(
            'Makeup', eLauncherPage.hot_feature_list)
        return self
