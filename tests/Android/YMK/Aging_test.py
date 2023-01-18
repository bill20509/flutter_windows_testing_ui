from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
import pytest
from pytest_html import extras

album_name1 = "1.Makeup"
album_name2 = "2.Redness"
album_name4 = "4.uneven_skintone"
album_name5 = "5.Wrinkle"

class Test(object):
    def setup_method(self):  # run before every test
        self.driver = App().set_auto() \
            .set_app("YMK") \
            .set_wait_time(5) \
            .set_newcommand_timeout(9999) \
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.A
    @pytest.mark.S1
    def test_aging_animation_check(self, extra):
        self.app.deeplink_to_aging() \
            .click_tryit() \
            .choose_photo() \
            .pick_photo(album_name1, 1) \
            .start_screen_recording() \
            .wait_animation() \
            .stop_screen_recording("aging_animation")
        extra.append(extras.video('screenshot/aging_animation.mp4', extension='mp4'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_aging_photo_aging(self, extra):
        self.app.deeplink_to_aging()\
            .click_tryit()\
            .choose_photo()\
            .pick_photo(album_name1, 1)\
            .wait_animation()\
            .click_photo()\
            .adjust_intensity_to_left() \
            .click_save() \
            .pull_photo_from_device("1_aging_photoaging_save") \
            .share_to_bc("share_aging_photo(auto test)")
        self.app.deeplink_to_me() \
            .click_posts_tab() \
            .screenshot("test_aging_share_photo")
        extra.append(extras.image('savephoto/1_aging_photoaging_save.jpg'))
        extra.append(extras.image('screenshot/test_aging_share_photo.png'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_aging_before_after_aging(self, extra):
        self.app.deeplink_to_aging() \
            .click_tryit() \
            .choose_photo() \
            .pick_photo(album_name1, 1) \
            .wait_animation() \
            .click_save() \
            .pull_photo_from_device("1_aging_before_after_aging_save") \
            .share_to_bc("share_aging_before_after(auto test)")
        self.app.deeplink_to_me() \
            .click_posts_tab() \
            .screenshot("test_aging_share_before_after")
        extra.append(extras.image('savephoto/1_aging_before_after_aging_save.jpg'))
        extra.append(extras.image('screenshot/test_aging_share_before_after.png'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_aging_grid_aging(self, extra):
        self.app.deeplink_to_aging() \
            .click_tryit() \
            .choose_photo() \
            .pick_photo(album_name1, 1) \
            .wait_animation() \
            .click_grid() \
            .click_save() \
            .pull_photo_from_device("1_aging_grid_aging_save") \
            .share_to_bc("share_aging_grid(auto test)")
        self.app.deeplink_to_me() \
            .click_posts_tab() \
            .screenshot("test_aging_share_grid")
        extra.append(extras.image('savephoto/1_aging_grid_aging_save.jpg'))
        extra.append(extras.image('screenshot/test_aging_share_grid.png'))

    @pytest.mark.A
    @pytest.mark.S1
    def test_aging_video_aging(self, extra):
        self.app.deeplink_to_aging() \
            .click_tryit() \
            .choose_photo() \
            .pick_photo(album_name1, 1) \
            .wait_animation() \
            .click_video() \
            .click_save() \
            .pull_video_from_device(format="mp4", rename="1_test_aging_video_save",
                                    app_name="YMK") \
            .share_to_bc("share_aging_video(auto test)")
        self.app.deeplink_to_me() \
            .click_posts_tab() \
            .screenshot("test_aging_share_video")
        extra.append(extras.video('savephoto/1_test_aging_video_save.mp4', extension='mp4'))
        extra.append(extras.image('screenshot/test_aging_share_video.png'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
