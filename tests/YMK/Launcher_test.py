from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
import pytest
from pytest_html import extras

folder_name = "1.Makeup"
folder_name1 = "5.Wrinkle"


class Test(object):
    def setup_method(self):  # run before every test
        self.driver = App().set_auto() \
            .set_app("YMK") \
            .set_wait_time(5) \
            .set_newcommand_timeout(9999) \
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_get_inspired(self, extra):
        self.app.deeplink_to_launcher() \
            .click_get_inspired_button() \
            .screenshot("test_get_inspired", 3)
        extra.append(extras.image('screenshot/test_get_inspired.png'))

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_crown_button(self, extra):
        self.app.deeplink_to_launcher() \
            .click_crown_button() \
            .screenshot("test_crown_button", 5)
        extra.append(extras.image('screenshot/test_crown_button.png'))

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_ycv_tile(self, extra):
        self.app.deeplink_to_launcher() \
            .click_ycv_tile() \
            .screenshot("test_ycv_tile", 3)
        extra.append(extras.image('screenshot/test_ycv_tile.png'))

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_ycp_tile(self, extra):
        self.app.deeplink_to_launcher() \
            .click_ycp_tile() \
            .screenshot("test_ycp_tile", 3)
        extra.append(extras.image('screenshot/test_ycp_tile.png'))

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_get_youcam_perfect(self, extra):
        self.app.deeplink_to_launcher() \
            .click_get_youcam_ycp()\
            .screenshot("test_get_youcam_perfect", 3)
        extra.append(extras.image('screenshot/test_get_youcam_perfect.png'))

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_get_youcam_video(self, extra):
        self.app.deeplink_to_launcher() \
            .click_get_youcam_ycv()\
            .screenshot("test_get_youcam_video", 3)
        extra.append(extras.image('screenshot/test_get_youcam_video.png'))

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_hot_feature(self, extra):
        self.app.deeplink_to_launcher() \
            .find_hot_feature()\
            .screenshot("test_hot_feature_on_launcher", 3)\
            .try_hot_feature() \
            .pick_photo(folder_name1, 1) \
            .waiting_cursor() \
            .screenshot("test_hot_feature", 3)
        extra.append(extras.image('screenshot/test_hot_feature.png'))
        extra.append(extras.image('screenshot/test_hot_feature_on_launcher.png'))

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_popular_look(self, extra):
        self.app.deeplink_to_launcher() \
            .find_popular_look()\
            .screenshot("test_popular_look_on_launcher", 3) \
            .try_popular_look() \
            .waiting_cursor() \
            .screenshot("test_popular_look", 3)
        extra.append(extras.image('screenshot/test_popular_look.png'))
        extra.append(extras.image('screenshot/test_popular_look_on_launcher.png'))

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_how_to(self, extra):
        self.app.deeplink_to_launcher() \
            .find_how_to() \
            .screenshot("test_how_to_on_launcher", 3) \
            .try_how_to() \
            .waiting_cursor() \
            .screenshot("test_how_to", 3)
        extra.append(extras.image('screenshot/test_how_to.png'))
        extra.append(extras.image('screenshot/test_how_to_on_launcher.png'))

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_trending(self, extra):
        self.app.deeplink_to_launcher() \
            .find_trending() \
            .screenshot("test_trending_on_launcher", 3) \
            .try_trending() \
            .waiting_cursor() \
            .screenshot("test_trending", 3)
        extra.append(extras.image('screenshot/test_trending.png'))
        extra.append(extras.image('screenshot/test_trending_on_launcher.png'))

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_makeover(self, extra):
        self.app.deeplink_to_launcher() \
            .find_makeover() \
            .screenshot("test_makeover_on_launcher", 3) \
            .try_makeover() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .screenshot("test_makeover", 3)
        extra.append(extras.image('screenshot/test_makeover.png'))
        extra.append(extras.image('screenshot/test_makeover_on_launcher.png'))

    @pytest.mark.B
    @pytest.mark.Launcher
    def test_shows(self, extra):
        self.app.deeplink_to_launcher() \
            .find_shows() \
            .screenshot("test_shows_on_launcher", 3) \
            .try_shows() \
            .waiting_cursor() \
            .screenshot("test_shows", 3)
        extra.append(extras.image('screenshot/test_shows.png'))
        extra.append(extras.image('screenshot/test_shows_on_launcher.png'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()

