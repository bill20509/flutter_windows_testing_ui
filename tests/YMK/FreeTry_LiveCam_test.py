import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from libs.YMK.locators import ResultLocators, PhotoMakeupLocators, LauncherLocators, PickPhotoLocators, MakeupCamLocators
import time
from pytest_html import extras

class Test(object):
    def setup_method(self):  # run before every test
        # 設定device
        self.driver = App().set_auto() \
            .set_app("YMK") \
            .set_wait_time(5) \
            .set_newcommand_timeout(9999) \
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.A
    @pytest.mark.N1
    def test_free_try_live_hairdye_multi(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_makeupcam() \
                    .select_hair() \
                    .select_brand("PERFECT") \
                    .click_capture() \
                    .click_photo_save() \
                    .wait_time(3)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_live_hairdye_multi(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_live_hairdye_multi(第%d次).png' % i))
                break

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_live_hairdye_2_colors(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_makeupcam() \
                    .select_hair() \
                    .select_brand("PERFECT") \
                    .select_haircolor_tab(" 2 COLORS ") \
                    .click_capture() \
                    .click_photo_save() \
                    .wait_time(3)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_live_hairdye_2_colors(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_live_hairdye_2_colors(第%d次).png' % i))
                break

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_live_hairdye_ombre(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_makeupcam() \
                    .select_hair() \
                    .select_brand("PERFECT") \
                    .select_haircolor_tab(" OMBRE ") \
                    .click_capture() \
                    .click_photo_save() \
                    .wait_time(3)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_live_hairdye_ombre(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_live_hairdye_ombre(第%d次).png' % i))
                break

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_live_premium_lip_art(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_makeupcam() \
                    .select_makeup() \
                    .select_feature_list(" Lip Color ") \
                    .select_brand("PERFECT") \
                    .select_color_tab("LIP ART") \
                    .click_premium_lip() \
                    .click_capture() \
                    .click_photo_save() \
                    .wait_time(3)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_live_lip_art")
                extra.append(extras.image('screenshot/test_free_try_live_lip_art.png'))
                break

    @pytest.mark.A
    @pytest.mark.N1
    def test_free_try_live_lip_texture(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_makeupcam() \
                    .select_makeup() \
                    .select_feature_list(" Lip Color ") \
                    .select_brand("PERFECT") \
                    .click_element_by_text("Matte") \
                    .click_capture() \
                    .click_photo_save() \
                    .wait_time(3)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_live_lip_texture(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_live_lip_texture(第%d次).png' % i))
                break

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_live_premium_look(self, extra):
        try:
            self.app.deeplink_to_makeupcam() \
                .select_looks() \
                .click_premium_category() \
                .click_premium_pack() \
                .click_capture() \
                .click_photo_save()
        except:
            self.app.find_element_by_text("Subscribe Now")
            self.app.screenshot("test_free_try_live_premium_look")
            extra.append(extras.image('screenshot/test_free_try_live_premium_look.png'))

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_live_premium_effect(self, extra):
        try:
            self.app.deeplink_to_makeupcam() \
                .select_effects() \
                .select_premium_pack() \
                .click_premium_effect() \
                .click_capture() \
                .click_photo_save()
        except:
            self.app.find_element_by_text("Subscribe Now")
            self.app.screenshot("test_free_try_live_premium_look")
            extra.append(extras.image('screenshot/test_free_try_live_premium_look.png'))

    @pytest.mark.A
    @pytest.mark.N1
    def test_free_try_live_video_watermark(self, extra):
        self.app.deeplink_to_makeupcam() \
            .switch_to_video_mode() \
            .select_looks() \
            .click_element_by_text("Alluring") \
            .click_record() \
            .click_stop() \
            .screenshot("test_free_try_live_video_watermark") \
            .click_remove_watermark() \
            .check_watermark_iap() \
            .screenshot("test_free_try_live_video_watermark_IAP")
        extra.append(extras.image('screenshot/test_free_try_live_video_watermark_IAP.png'))
        extra.append(extras.image('screenshot/test_free_try_live_video_watermark.png'))

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_live_video_premium_collection(self, extra):
        self.app.deeplink_to_makeupcam() \
            .wait_element_visible(MakeupCamLocators.premium_categorya) \
            .screenshot("test_free_try_live_premium_collection") \
            .switch_to_video_mode() \
            .wait_element_invisible(MakeupCamLocators.premium_categorya) \
            .screenshot("test_free_try_live_no_premium_collection")
        extra.append(extras.image('screenshot/test_free_try_live_no_premium_collection.png'))
        extra.append(extras.image('screenshot/test_free_try_live_premium_collection.png'))

    @pytest.mark.A
    @pytest.mark.N1
    def test_free_try_live_premium_reshape(self, extra):
        try:
            self.app.deeplink_to_makeupcam() \
                .select_reshape() \
                .select_feature_list(" Width ") \
                .slide_bar_to_right() \
                .click_capture() \
                .click_photo_save()
        except:
            self.app.find_element_by_text("Subscribe Now")
            self.app.screenshot("test_free_try_live_premium_reshape")
            extra.append(extras.image('screenshot/test_free_try_live_premium_reshape.png'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_free_try_live_lip_art()
    # t.teardown_method()
