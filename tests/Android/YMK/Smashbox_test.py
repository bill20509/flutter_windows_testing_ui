from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
import pytest
from pytest_html import extras

album_name1 = "1.Makeup"

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
    def test_smashbox_entry(self, extra):
        photo_entry = self.app.deeplink_to_me() \
            .click_setting() \
            .click_country() \
            .switch_country_to("Italy") \
            .waiting_cursor() \
            .click_back() \
            .deeplink_to_eyeshadow() \
            .pick_photo(album_name1, 1) \
            .select_brand("PERFECT") \
            .select_collection("4 Colors") \
            .check_smashbox_entry_is_exist()
        self.app.screenshot("test_smashbox_photo_entry", wait_time=3)

        extra.append(extras.image('screenshot/test_smashbox_photo_entry.png'))

        if photo_entry == 1:
            print("\nResult: PASS\n" + "Show Smashbox entry in Photo Edit\n")
        else:
            pytest.fail("No Smashbox entry in Photo Edit")

        cam_entry = self.app.deeplink_to_makeupcam_eyeshadow() \
            .select_brand("PERFECT") \
            .check_smashbox_entry_is_exist()
        self.app.screenshot("test_smashbox_cam_entry", wait_time=3)

        extra.append(extras.image('screenshot/test_smashbox_cam_entry.png'))

        if cam_entry == 1:
            print("\nResult: PASS\n" + "Show Smashbox entry in Makeup Cam\n")
        else:
            pytest.fail("No Smashbox entry in Makeup Cam")

    @pytest.mark.A
    @pytest.mark.S1
    def test_smashbox_try_sku_and_share(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_country() \
            .switch_country_to("Italy") \
            .waiting_cursor() \
            .deeplink_to_makeupcam_eyeshadow() \
            .select_brand("PERFECT") \
            .click_smashbox_entry() \
            .wait_smashbox_analysis_report_page() \
            .screenshot("test_smashbox_eye_detect_result", wait_time=3) \
            .try_sku() \
            .screenshot("test_smashbox_try_sku_1", wait_time=3) \
            .change_palette("LOOK AUDACE") \
            .screenshot("test_smashbox_try_sku_2", wait_time=3) \
            .change_palette("LOOK SMOKY") \
            .screenshot("test_smashbox_try_sku_3", wait_time=3) \
            .compose_gif("test_smashbox_try_sku", "screenshot/test_smashbox_try_sku_1.png",
                         "screenshot/test_smashbox_try_sku_2.png", "screenshot/test_smashbox_try_sku_3.png", speed=1) \
            .click_capture_button() \
            .screenshot("test_smashbox_try_sku_collage", wait_time=3) \
            .click_save_photo_button() \
            .pull_photo_from_device("test_smashbox_save_photo") \
            .share_to_bc("share_smashbox(auto test)")
        self.app.deeplink_to_me() \
            .click_posts_tab() \
            .screenshot("test_smashbox_share")

        extra.append(extras.image('screenshot/test_smashbox_eye_detect_result.png'))
        extra.append(extras.image('screenshot/test_smashbox_try_sku.gif'))
        extra.append(extras.image('screenshot/test_smashbox_try_sku_collage.png'))
        extra.append(extras.image('savephoto/test_smashbox_save_photo.jpg'))
        extra.append(extras.image('screenshot/test_smashbox_share.png'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
