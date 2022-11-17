from libs.YMK.locators import MeLocators, CloudAlbumViewLocators
from libs.YMK import pages


class MePage(pages.YMK_base.YMKbase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_setting(self):
        self.wait_element_visible(MeLocators.setting_button)
        self.click_element(MeLocators.setting_button)
        return pages.setting_page.SettingPage(self.driver)

    def click_home_button(self):
        self.wait_element_visible(MeLocators.Home_button)
        self.click_element(MeLocators.Home_button)
        return pages.launcher_page.Launcher(self.driver)

    def enable_backup_button(self):
        try:
            self.wait_element_visible(MeLocators.Enable_backup_button)
            self.click_element(MeLocators.Enable_backup_button)
        except (ValueError, Exception):
            pass
        return self

    def click_backuped_photo(self):
        self.wait_element_visible(MeLocators.Backup_view)
        for i in range(5):
            self.select_element_by_number(MeLocators.Backup_view, i)
            try:
                self.find_element(CloudAlbumViewLocators.Download_video_icon)
                self.click_element(CloudAlbumViewLocators.Back_button)
            except (ValueError, Exception):
                break
        return pages.cloud_album_view_page.CloudAlbumView(self.driver)

    def find_try_look_photo(self):
        self.wait_element_visible(MeLocators.Backup_view)
        for i in range(5):
            self.select_element_by_number(MeLocators.Backup_view, i)
            try:
                self.find_element(CloudAlbumViewLocators.Try_it_button)
                self.click_element(CloudAlbumViewLocators.Try_it_button)
                break
            except (ValueError, Exception):
                self.click_element(CloudAlbumViewLocators.Back_button)
        return pages.cloud_album_view_page.CloudAlbumView(self.driver)

    def click_backuped_video(self):
        for i in range(10):
            try:
                self.wait_element_visible(MeLocators.Video_play_icon)
                self.click_element(MeLocators.Video_play_icon)
                break
            except (ValueError, Exception):
                self.scroll_vertical(MeLocators.Backup_view, speed=1000)
        return pages.cloud_album_view_page.CloudAlbumView(self.driver)

    def click_posts_tab(self):
        self.wait_text_element_visible("Posts")
        self.click_element_by_text("Posts")
        self.wait_element_visible(MeLocators.Post_view)
        self.wait_time()
        return self









