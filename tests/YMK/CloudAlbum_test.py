import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
from pytest_html import extras
from libs.YMK.locators import MeLocators
from libs.YMK import pages

folder_name = "1.Makeup"
folder_name1 = "8.HEIC"


class Test(object):
    def setup_method(self):  # run before every test
        # 設定device
        self.driver = App().set_auto() \
            .set_app("YMK") \
            .set_wait_time(5) \
            .set_newcommand_timeout(9999) \
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.B
    @pytest.mark.S1
    def test_photo_backup(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .login_bc_account("backup@bb.bb", "bbbbbb") \
            .screenshot("test_backup_photo_1", wait_time=2) \
            .click_back() \
            .screenshot("test_backup_photo_2", wait_time=2) \
            .enable_backup_button()
        self.app.deeplink_to_makeupcam()\
            .select_looks() \
            .click_element_by_text("Alluring") \
            .click_capture() \
            .click_photo_save() \
            .click_back() \
            .click_me_button() \
            .wait_time(30) \
            .screenshot("test_backup_photo_3", wait_time=2) \
            .compose_gif("test_backup_photo_compare_diff", "screenshot/test_backup_photo_3.png",
                         "screenshot/test_backup_photo_2.png", "screenshot/test_backup_photo_1.png", speed=1)
        extra.append(extras.image("screenshot/test_backup_photo_compare_diff.gif"))
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_log_out()

    @pytest.mark.B
    @pytest.mark.S1
    def test_photo_download(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .login_bc_account("backup@bb.bb", "bbbbbb") \
            .screenshot("test_backup_photo_1", wait_time=2) \
            .click_back() \
            .screenshot("test_backup_photo_2", wait_time=2) \
            .enable_backup_button()
        self.app.deeplink_to_me()\
            .click_backuped_photo() \
            .click_download_button() \
            .check_download_completed() \
            .screenshot("test_photo_download", wait_time=2) \
            .pull_photo_from_device("test_photo_download_save")
        extra.append(extras.image("screenshot/test_photo_download.png"))
        extra.append(extras.image("savephoto/test_photo_download_save.jpg"))
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_log_out()

    @pytest.mark.B
    @pytest.mark.S2
    def test_try_look_in_live_cam(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .login_bc_account("backup@bb.bb", "bbbbbb") \
            .screenshot("test_backup_photo_1", wait_time=2) \
            .click_back() \
            .screenshot("test_backup_photo_2", wait_time=2) \
            .enable_backup_button()
        self.app.deeplink_to_me()\
            .find_try_look_photo()\
            .select_live_makeup_button()\
            .waiting_cursor() \
            .screenshot("test_try_look_in_live_cam", wait_time=2)
        extra.append(extras.image("screenshot/test_try_look_in_live_cam.png"))
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_log_out()

    @pytest.mark.B
    @pytest.mark.S2
    def test_try_look_in_photo_cam(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .login_bc_account("backup@bb.bb", "bbbbbb") \
            .screenshot("test_backup_photo_1", wait_time=2) \
            .click_back() \
            .screenshot("test_backup_photo_2", wait_time=2) \
            .enable_backup_button()
        self.app.deeplink_to_me() \
            .find_try_look_photo()\
            .select_photo_makeup_button()\
            .pick_photo(folder_name1, 1) \
            .waiting_cursor() \
            .screenshot("test_try_look_in_photo_cam", wait_time=2)
        extra.append(extras.image("screenshot/test_try_look_in_photo_cam.png"))
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_log_out()

    @pytest.mark.B
    @pytest.mark.S2
    def test_photo_delete(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .login_bc_account("backup@bb.bb", "bbbbbb") \
            .screenshot("test_backup_photo_1", wait_time=2) \
            .click_back() \
            .screenshot("test_backup_photo_2", wait_time=2) \
            .enable_backup_button()
        self.app.deeplink_to_me() \
            .screenshot("test_photo_delete_before", 2) \
            .click_backuped_photo() \
            .click_delete_button() \
            .screenshot("test_photo_delete_ing", 2) \
            .select_delete() \
            .waiting_cursor() \
            .screenshot("test_photo_delete_after")\
            .compose_gif("test_photo_delete_compare_diff", "screenshot/test_photo_delete_after.png",
                         "screenshot/test_photo_delete_ing.png", "screenshot/test_photo_delete_before.png", speed=1)
        extra.append(extras.image("screenshot/test_photo_delete_compare_diff.gif"))
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_log_out()

    @pytest.mark.B
    @pytest.mark.S1
    def test_video_backup(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .login_bc_account("backup@bb.bb", "bbbbbb") \
            .screenshot("test_backup_photo_1", wait_time=2) \
            .click_back() \
            .screenshot("test_backup_photo_2", wait_time=2) \
            .enable_backup_button()
        self.app.deeplink_to_me() \
            .screenshot("test_video_backup_before", 2) \
            .enable_backup_button()
        self.app.deeplink_to_makeupcam()\
            .select_looks() \
            .switch_to_video_mode() \
            .click_element_by_text("Alluring") \
            .waiting_cursor() \
            .click_record() \
            .click_stop() \
            .click_video_save() \
            .click_home() \
            .click_me_button() \
            .wait_time(30) \
            .screenshot("test_video_backup_after") \
            .compose_gif("test_video_backup_compare_diff", "screenshot/test_video_backup_after.png",
                         "screenshot/test_video_backup_before.png", speed=2)
        extra.append(extras.image("screenshot/test_video_backup_compare_diff.gif"))
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_log_out()

    @pytest.mark.B
    @pytest.mark.S2
    def test_video_download(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .login_bc_account("backup@bb.bb", "bbbbbb") \
            .screenshot("test_backup_photo_1", wait_time=2) \
            .click_back() \
            .screenshot("test_backup_photo_2", wait_time=2) \
            .enable_backup_button()
        self.app.deeplink_to_me()\
            .click_backuped_video() \
            .click_download_button() \
            .check_download_completed() \
            .screenshot("test_video_download")
        extra.append(extras.image("screenshot/test_video_download.png"))
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_log_out()

    @pytest.mark.B
    @pytest.mark.S2
    def test_video_delete(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .login_bc_account("backup@bb.bb", "bbbbbb") \
            .screenshot("test_backup_photo_1", wait_time=2) \
            .click_back() \
            .screenshot("test_backup_photo_2", wait_time=2) \
            .enable_backup_button()
        self.app.deeplink_to_me() \
            .screenshot("test_video_delete_before", wait_time=2) \
            .click_backuped_video() \
            .click_delete_button() \
            .screenshot("test_video_delete_ing", wait_time=2) \
            .select_delete() \
            .waiting_cursor() \
            .screenshot("test_video_delete_after")\
            .compose_gif("test_video_delete_compare_diff", "screenshot/test_video_delete_after.png",
                         "screenshot/test_video_delete_ing.png", "screenshot/test_video_delete_before.png", speed=1)
        extra.append(extras.image("screenshot/test_video_delete_compare_diff.gif"))
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_log_out()

    @pytest.mark.B
    @pytest.mark.cloud_album
    def test_premium_look_edit(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .login_bc_account("backup@bb.bb", "bbbbbb") \
            .screenshot("test_backup_photo_1", wait_time=2) \
            .click_back() \
            .screenshot("test_backup_photo_2", wait_time=2) \
            .enable_backup_button()
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks() \
            .click_crown() \
            .select_look_by_number(1) \
            .wait_download_pack() \
            .click_save()
        self.app.deeplink_to_me() \
            .click_backuped_photo() \
            .click_edit_button() \
            .waiting_cursor() \
            .screenshot("test_premium_look_edit", wait_time=2)
        extra.append(extras.image("screenshot/test_premium_look_edit.png"))
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_log_out()

    @pytest.mark.B
    def test_premium_look_try(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .login_bc_account("backup@bb.bb", "bbbbbb") \
            .screenshot("test_backup_photo_1", wait_time=2) \
            .click_back() \
            .screenshot("test_backup_photo_2", wait_time=2) \
            .enable_backup_button()
        self.app.deeplink_to_me() \
            .find_try_look_photo() \
            .waiting_cursor() \
            .screenshot("test_premium_look_try", wait_time=2)
        extra.append(extras.image("screenshot/test_premium_look_try.png"))
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_log_out()

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()

