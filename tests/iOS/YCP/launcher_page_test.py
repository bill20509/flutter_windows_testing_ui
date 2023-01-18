import time
import pytest
from libs.app import App
from libs.YCP import pages


class Test(object):

    def setup_method(self):  # run before every test
        self.driver = App().set_auto()\
            .set_app("YCP")\
            .set_auto_launch(True)\
            .set_wait_time(5)\
            .set_newcommand_timeout(9999)\
            .create()
        self.app = pages.launcher.LauncherPage(self.driver)

    @pytest.mark.launcher
    def test_launcher_banner_gradient(self):  # Carolyn
        self.app.deeplink_to_launcher()\
            .screenshot("test_launcher_banner_gradient", 1)

    @pytest.mark.launcher
    def test_launcher_banner_scroll_hint(self):  # Carolyn
        self.app.deeplink_to_launcher() \
                .click_scroll_down_hint() \
                .screenshot("test_launcher_scroll_hint)", 3)

    @pytest.mark.launcher
    def test_launcher_header(self):  # Carolyn
        self.app.deeplink_to_launcher() \
                .click_app_logo() \
                .click_scroll_down_hint() \
                .screenshot("test_launcher_header", 1)

    @pytest.mark.launcher
    def test_launcher_logo(self):  # Carolyn
        self.app.deeplink_to_launcher()\
                .click_scroll_down_hint()\
                .click_app_logo()\
                .screenshot("test_launcher_logo", 1)

    @pytest.mark.launcher
    def test_launcher_discovery(self):  # Carolyn
        self.app.deeplink_to_launcher()\
                .click_discovery() \
                .screenshot("test_launcher_discovery", 5)

    @pytest.mark.launcher
    def test_launcher_store(self):  # Carolyn
        self.app.deeplink_to_launcher() \
                .click_app_logo() \
                .click_store() \
                .screenshot("test_launcher_store", 5)

    @pytest.mark.launcher
    def test_launcher_hot_wraparound(self):  # Carolyn
        self.app.deeplink_to_launcher() \
                .deeplink_hot_wraparound() \
                .screenshot("test_launcher_hot_wraparound", 1)

    @pytest.mark.launcher
    def test_launcher_hot_change_background(self):  # Carolyn
        self.app.deeplink_to_launcher() \
                .deeplink_hot_change_background() \
                .screenshot("test_launcher_hot_change_background", 1)

    @pytest.mark.launcher
    def test_launcher_hot_removal(self):  # Carolyn
        self.app.deeplink_to_launcher() \
                .deeplink_hot_removal() \
                .screenshot("test_launcher_hot_removal", 1)

    @pytest.mark.launcher
    def test_launcher_hot_my_stickers(self):  # Carolyn
        self.app.deeplink_to_launcher()\
                .deeplink_hot_my_stickers() \
                .screenshot("test_launcher_hot_my_stickers", 1)

    @pytest.mark.launcher
    def test_launcher_hot_template(self):  # Carolyn
        self.app.deeplink_to_launcher()\
                .deeplink_hot_template() \
                .screenshot("test_launcher_hot_template", 3)

    @pytest.mark.launcher
    def test_launcher_how_to_see_all(self):  # Carolyn
        self.app.deeplink_to_launcher() \
                .click_app_logo() \
                .click_how_to_see_all() \
                .screenshot("test_launcher_how_to_see_all", 1)

    @pytest.mark.launcher
    def test_launcher_community_see_all(self):  # Carolyn
        self.app.deeplink_to_launcher() \
                .click_app_logo() \
                .click_trending_see_all() \
                .screenshot("test_launcher_community_see_all", 1)

    @pytest.mark.launcher
    def test_launcher_photo_challenge_see_all(self): # Carolyn
        self.app.deeplink_to_launcher() \
                .click_app_logo() \
                .click_photo_challenge_see_all()\
                .screenshot("test_launcher_photo_challenge_see_all")

    @pytest.mark.launcher
    def test_launcher_apps_get(self):  # Carolyn
        self.app.deeplink_to_launcher() \
                .click_app_logo() \
                .click_scroll_down_hint()\
                .click_scroll_down_hint() \
                .click_scroll_down_hint() \
                .find_element_by_text("GET")\
                .click_element_by_text("GET")\
                .screenshot("test_launcher_apps_get", 1)

    @pytest.mark.launcher
    def test_launcher_apps_open(self):  # Carolyn
        self.app.deeplink_to_launcher() \
                .click_app_logo() \
                .click_scroll_down_hint() \
                .click_scroll_down_hint() \
                .click_scroll_down_hint() \
                .find_element_by_text("OPEN") \
                .click_element_by_text("OPEN") \
            .screenshot("test_launcher_apps_open", 1)

    @pytest.mark.launcher
    def test_launcher_settings(self): # Carolyn
        self.app.deeplink_to_launcher() \
                .click_app_logo() \
                .click_settings()\
                .screenshot("test_launcher_settings", 1)

    @pytest.mark.launcher
    def test_launcher_crown(self): # Carolyn
        self.app.deeplink_to_launcher() \
                .click_app_logo() \
                .click_premium() \
                .screenshot("test_launcher_crown", 1)

    @pytest.mark.launcher
    def test_launcher_camera(self): # Carolyn
        self.app.deeplink_to_launcher() \
                .click_app_logo() \
                .click_camera() \
                .screenshot("test_launcher_camera", 1)

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_launcher_banner_gradient()
    t.test_launcher_banner_scroll_hint()
    t.test_launcher_header()
    t.test_launcher_logo()
    t.test_launcher_discovery()
    t.test_launcher_store()
    t.test_launcher_hot_wraparound()
    t.test_launcher_hot_change_background()
    t.test_launcher_hot_removal()
    t.test_launcher_hot_my_stickers()
    t.test_launcher_hot_template()
    t.test_launcher_how_to_see_all()
    t.test_launcher_community_see_all()
    t.test_launcher_photo_challenge_see_all()
    t.test_launcher_apps_get()
    t.test_launcher_apps_open()
    t.test_launcher_settings()
    t.test_launcher_crown()
    t.test_launcher_camera()
    t.teardown_method()
