import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
from libs.YMK.locators import SettingLocators
from pytest_html import extras
folder_name = "1.Makeup"


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
    @pytest.mark.S2
    def test_setting_check_name_thumbnail_mail_userid(self, extra):
        self.app.deeplink_to_setting() \
            .login_bc_account("bb@bb.com", "bbbbbb")\
            .wait_element_visible(SettingLocators.user_id) \
            .screenshot("test_setting_check_name_thumbnail_mail_userid", 2)
        extra.append(extras.image('screenshot/test_setting_check_name_thumbnail_mail_userid.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_about_me(self, extra):
        self.app.deeplink_to_setting() \
            .login_bc_account("bb@bb.com", "bbbbbb")\
            .click_about_me() \
            .input_text_about_me() \
            .input_text_website() \
            .screenshot("test_setting_about_me", 2) \
            .click_apply()
        extra.append(extras.image('screenshot/test_setting_about_me.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_setting_quality_high(self, extra):
        self.app.deeplink_to_setting() \
            .click_quality() \
            .wait_time(1) \
            .select_high() \
            .click_back() \
            .deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_save() \
            .pull_photo_from_device("test_setting_quality_high") \
            .get_image_dimension("savephoto/test_setting_quality_high.jpg")
        extra.append(extras.image('savephoto/test_setting_quality_high.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_quality_ultrahigh(self, extra):
        self.app.deeplink_to_setting() \
            .click_quality() \
            .wait_time(1) \
            .select_ultrahigh() \
            .click_back() \
            .deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_save() \
            .pull_photo_from_device("test_setting_quality_ultrahigh") \
            .get_image_dimension("savephoto/test_setting_quality_ultrahigh.jpg")
        extra.append(extras.image('savephoto/test_setting_quality_ultrahigh.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_setting_quality_normal(self, extra):
        self.app.deeplink_to_setting() \
            .click_quality() \
            .wait_time(1) \
            .select_normal() \
            .click_back() \
            .deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_save() \
            .pull_photo_from_device("test_setting_quality_normal")\
            .get_image_dimension("savephoto/test_setting_quality_normal.jpg")
        extra.append(extras.image('savephoto/test_setting_quality_normal.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_quality_smart_hd(self, extra):
        self.app.deeplink_to_setting() \
            .click_quality() \
            .wait_time(1) \
            .select_smart_hd() \
            .click_back() \
            .deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_save() \
            .pull_photo_from_device("test_setting_quality_smart_hd")\
            .get_image_dimension("savephoto/test_setting_quality_smart_hd.jpg")
        extra.append(extras.image('savephoto/test_setting_quality_smart_hd.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_feedback(self):
        self.app.deeplink_to_setting() \
            .click_faq() \
            .click_send_feedback() \
            .input_text_feedback() \
            .click_submit() \
            .wait_element_visible(SettingLocators.feedback_dialog)

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_app_version(self, extra):
        self.app.deeplink_to_setting() \
            .click_about() \
            .wait_time(1) \
            .screenshot("setting_app_version")
        extra.append(extras.image('screenshot/setting_app_version.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_legal_notice(self, extra):
        self.app.deeplink_to_setting() \
            .click_about() \
            .wait_time(1) \
            .click_legal_notice() \
            .wait_time(2) \
            .screenshot("test_setting_legal_notice")
        extra.append(extras.image('screenshot/test_setting_legal_notice.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_terms_of_service(self, extra):
        self.app.deeplink_to_setting() \
            .click_about() \
            .wait_time(1) \
            .click_term_of_service() \
            .wait_time(2) \
            .screenshot("test_setting_terms_of_service")
        extra.append(extras.image('screenshot/test_setting_terms_of_service.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_privacy_policy(self, extra):
        self.app.deeplink_to_setting() \
            .click_about() \
            .wait_time(1) \
            .click_privacy_policy() \
            .wait_time(2) \
            .screenshot("test_setting_privacy_policy")
        extra.append(extras.image('screenshot/test_setting_privacy_policy.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_setting_events_version(self, extra):
        self.app.deeplink_to_setting() \
            .click_events() \
            .wait_time(2) \
            .screenshot("test_setting_events_version")
        extra.append(extras.image('screenshot/test_setting_events_version.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_setting_tutorials(self, extra):
        self.app.deeplink_to_setting() \
            .click_tutorials() \
            .screenshot("test_setting_tutorials", 3)
        extra.append(extras.image('screenshot/test_setting_tutorials.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_country(self, extra):
        self.app.deeplink_to_setting() \
            .click_country() \
            .switch_country()\
            .waiting_cursor() \
            .check_country()\
            .screenshot("test_setting_country", 2)
        extra.append(extras.image('screenshot/test_setting_country.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_setting_auto_save(self, extra):
        self.app.deeplink_to_setting() \
            .click_auto_save() \
            .screenshot("test_setting_auto_save", 2) \
            .deeplink_to_makeupcam() \
            .waiting_cursor() \
            .wait_time(2) \
            .click_capture_for_timer() \
            .screenshot("test_setting_auto_save_1", 2) \
            .deeplink_to_setting() \
            .click_auto_save()
        extra.append(extras.image('screenshot/test_setting_auto_save_1.png'))
        extra.append(extras.image('screenshot/test_setting_auto_save.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_front_camera_mirror(self, extra):
        self.app.deeplink_to_setting() \
            .click_front_camera_mirror() \
            .screenshot("test_setting_front_camera_mirror_1", 2) \
            .deeplink_to_makeupcam() \
            .screenshot("test_setting_front_camera_mirror_2", 3) \
            .click_capture() \
            .click_photo_save()\
            .wait_time(3)\
            .pull_photo_from_device("test_setting_front_camera_mirror")\
            .deeplink_to_setting() \
            .click_front_camera_mirror()
        extra.append(extras.image('savephoto/test_setting_front_camera_mirror.jpg'))
        extra.append(extras.image('screenshot/test_setting_front_camera_mirror_2.png'))
        extra.append(extras.image('screenshot/test_setting_front_camera_mirror_1.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_skin_beautifier(self, extra):
        self.app.deeplink_to_setting() \
            .click_skin_beautifier() \
            .screenshot("test_setting_skin_beautifier_1") \
            .deeplink_to_makeupcam() \
            .select_reshape()\
            .screenshot("test_setting_skin_beautifier", 3) \
            .deeplink_to_setting() \
            .click_skin_beautifier()
        extra.append(extras.image('screenshot/test_setting_skin_beautifier.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_setting_gps_disable(self, extra):
        self.app.deeplink_to_setting() \
            .click_access_gps() \
            .screenshot("test_setting_gps_disable_1", 3) \
            .deeplink_to_makeupcam() \
            .click_capture()\
            .click_photo_save()\
            .pull_photo_from_device("test_setting_gps_disable")\
            .deeplink_to_setting() \
            .click_access_gps()
        extra.append(extras.image('savephoto/test_setting_gps_disable.jpg'))
        extra.append(extras.image('screenshot/test_setting_gps_disable_1.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_photo_watermark_disable(self, extra):
        self.app.deeplink_to_setting() \
            .find_video_watermark() \
            .screenshot("test_setting_photo_watermark") \
            .deeplink_to_photomakeup() \
            .pick_photo("3.Bodytuner", 1) \
            .wait_time(3) \
            .select_looks() \
            .select_look_item("Lotus") \
            .waiting_cursor()\
            .click_save()\
            .pull_photo_from_device("test_setting_photo_watermark_disable")
        extra.append(extras.image('savephoto/test_setting_photo_watermark_disable.jpg'))
        extra.append(extras.image('screenshot/test_setting_photo_watermark.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_setting_video_watermark_disable(self, extra):
        self.app.deeplink_to_setting() \
            .find_video_watermark()\
            .screenshot("test_setting_video_watermark")\
            .deeplink_to_makeupcam() \
            .switch_to_video_mode() \
            .click_record()\
            .click_stop()\
            .click_video_save()\
            .pull_video_from_device("mp4", "test_setting_video_watermark_disable")
        extra.append(extras.video('savephoto/test_setting_video_watermark_disable.mp4', extension='mp4'))
        extra.append(extras.image('screenshot/test_setting_video_watermark.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_setting_rate_us(self, extra):
        self.app.deeplink_to_setting() \
            .click_rate_us() \
            .wait_time(5) \
            .screenshot("test_setting_rate_us")
        extra.append(extras.image('screenshot/test_setting_rate_us.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_setting_follow_us(self, extra):
        self.app.deeplink_to_setting() \
            .wait_time(1) \
            .click_follow_us() \
            .wait_time(5) \
            .screenshot("test_setting_follow_us")
        extra.append(extras.image('screenshot/test_setting_follow_us.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_setting_premium_status_sub(self, extra):
        self.app.deeplink_to_setting() \
            .click_premium_banner() \
            .screenshot("test_setting_premium_status_sub", 5)
        extra.append(extras.image('screenshot/test_setting_premium_status_sub.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_setting_save_path(self, extra):
        self.app.deeplink_to_setting() \
            .check_save_path() \
            .screenshot("test_setting_save_path", 1)
        extra.append(extras.image('screenshot/test_setting_save_path.png'))

    @pytest.mark.N2
    def test_setting_premium_banner_non_sub(self, extra):
        self.app.deeplink_to_setting() \
            .screenshot("test_setting_premium_banner_non_sub", 2)
        extra.append(extras.image('screenshot/test_setting_premium_banner_non_sub.png'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
