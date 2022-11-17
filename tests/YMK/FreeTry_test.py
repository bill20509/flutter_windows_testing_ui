import pytest
from appium.webdriver.common.touch_action import TouchAction
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from libs.YMK.locators import ResultLocators, PhotoMakeupLocators, LauncherLocators, PickPhotoLocators
from pytest_html import extras
import time
folder_name = "1.Makeup"
folder_name_2 = "2.Redness"

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
    def check_photo_iap(self, timeout=5):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .find_element(PickPhotoLocators.iap) \
            .screenshot("Photo_picker_iap")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_hairdye_multi(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_hairdye() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .select_brand("PERFECT") \
                    .select_color(1) \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_hairdye_multi(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_hairdye_multi(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N1
    def test_free_try_hairdye_2colors(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_hairdye() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .select_brand("PERFECT") \
                    .select_haircolor_tab("2 COLORS") \
                    .select_color(3) \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_hairdye_2colors(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_hairdye_2colors(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_hairdye_ombre(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_hairdye() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .select_brand("PERFECT") \
                    .select_haircolor_tab("OMBRE") \
                    .select_color(3) \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_ombre(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_ombre(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N1
    def test_free_try_smile(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_smile() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_smile(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_smile(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N1
    def test_free_try_plumper(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_lipplumper() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_plumper(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_plumper(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_teeth_whitener(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_teethwhitener() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_teeth_whitener(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_teeth_whitener(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_lipart(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_lipart() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .select_lipart_pattern(1) \
                    .wait_element_invisible(PhotoMakeupLocators.Mouth.mouth_download_progress) \
                    .wait_time() \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_lipart(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_lipart(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_lip_reshape(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_lipreshape() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_lip_reshape(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_lip_reshape(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_lip_color_texture(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_lipstick() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .select_brand("PERFECT") \
                    .select_texture("Matte") \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_lip_color_texture(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_lip_color_texture(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_face_shaper(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_faceshape() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .select_faceshape_function("Chin Shape") \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_face_shaper(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_face_shaper(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_nose_size(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_noseenhance() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .select_noseenhance_function("Size") \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_nose_size(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_nose_size(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N1
    def test_free_try_wrinkle(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_wrinkle() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .wait_animation() \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_wrinkle(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_wrinkle(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_redness(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_redness() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .wait_animation() \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_redness(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_redness(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_uneven_skintone(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_unevenskintone() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .wait_animation() \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_uneven_skintone(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_uneven_skintone(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    # @pytest.mark.free_try
    # def test_free_try_pores(self, extra):
    #     for i in range(1, 5):
    #         try:
    #             self.app.deeplink_to_pores() \
    #                 .pick_photo(folder_name, 1) \
    #                 .wait_animation() \
    #                 .adjust_intensity_to_right() \
    #                 .wait_time(3) \
    #                 .click_save(5)
    #         except:
    #             self.app.find_element_by_text("Subscribe Now")
    #             self.app.screenshot("test_free_try_pores(第%d次)" % i)
    #             extra.append(extras.image('screenshot/test_free_try_pores(第%d次).png' % i))
    #             break
    #     try:
    #         self.app.find_element_by_text("Subscribe Now")
    #     except:
    #         pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_blemish(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_blemish() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .switch_onoff() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_blemish(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_blemish(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_dark_circle(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_darkcircle() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .wait_animation() \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_dark_circle(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_dark_circle(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N1
    def test_free_try_eye_bag(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_eyebag() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .wait_animation() \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_eye_bag(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_eye_bag(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N1
    def test_free_try_brow_reshape(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_browreshape() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .select_browsreshape_function("Thickness") \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_brow_reshape(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_brow_reshape(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_eyetuner(self, extra):
        for i in range(1, 5):
            try:
                self.app.deeplink_to_eyetuner() \
                    .pick_photo(folder_name, 1) \
                    .check_iap_AD() \
                    .select_eyetuner_function("Angle") \
                    .adjust_intensity_to_right() \
                    .wait_time(3) \
                    .click_save(5)
            except:
                self.app.find_element_by_text("Subscribe Now")
                self.app.screenshot("test_free_try_eyetuner(第%d次)" % i)
                extra.append(extras.image('screenshot/test_free_try_eyetuner(第%d次).png' % i))
                break
        try:
            self.app.find_element_by_text("Subscribe Now")
        except:
            pytest.fail("Can't show subscription panel")

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_premium_look(self, extra):
        try:
            self.app.deeplink_to_photomakeup() \
                .pick_photo(folder_name, 1) \
                .check_iap_AD() \
                .select_looks() \
                .click_crown() \
                .click_look_pack() \
                .wait_download_pack() \
                .waiting_cursor() \
                .click_save(5)
        except:
            self.app.find_element_by_text("Subscribe Now")
            self.app.screenshot("test_free_try_premium_look")
            extra.append(extras.image('screenshot/test_free_try_premium_look.png'))

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_premium_effect(self, extra):
        try:
            self.app.deeplink_to_effect() \
                .pick_photo(folder_name, 1) \
                .check_iap_AD() \
                .click_premium_effect_pack() \
                .wait_download_pack() \
                .click_effect() \
                .click_save(5)
        except:
            self.app.find_element_by_text("Subscribe Now")
            self.app.screenshot("test_free_try_premium_effect")
            extra.append(extras.image('screenshot/test_free_try_premium_effect.png'))

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_premium_background(self, extra):
        try:
            self.app.deeplink_to_background() \
                .pick_photo(folder_name, 1) \
                .check_iap_AD() \
                .click_premium_item() \
                .wait_time() \
                .click_save(5)
        except:
            self.app.find_element_by_text("Subscribe Now")
            self.app.screenshot("test_free_try_premium_background")
            extra.append(extras.image('screenshot/test_free_try_premium_background.png'))

    @pytest.mark.A
    @pytest.mark.N1
    def test_free_try_photo_background(self, extra):
        try:
            self.app.deeplink_to_background() \
                .pick_photo(folder_name, 1) \
                .check_iap_AD() \
                .waiting_cursor() \
                .select_photo_background(folder_name, 1) \
                .wait_time(3) \
                .check_dailog() \
                .click_save(5) \
                .show_result_page() \
                .click_photo_picker() \
                .pick_photo(folder_name, 1) \
                .check_iap_AD() \
                .select_background() \
                .select_photo_background(folder_name, 1) \
                .wait_time(3) \
                .check_dailog() \
                .click_save(5)
        except:
            self.app.find_element_by_text("Subscribe Now")
            self.app.screenshot("test_free_try_photo_background(第二次)")
            extra.append(extras.image('screenshot/test_free_try_photo_background(第二次).png'))

    @pytest.mark.A
    @pytest.mark.N2
    def test_free_try_costume_look(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo("3.Bodytuner", 1) \
            .check_iap_AD() \
            .wait_time(3) \
            .select_looks() \
            .select_look_item("Lotus") \
            .waiting_cursor() \
            .screenshot("test_free_try_costume_look_watermark") \
            .click_watermark()
        # TouchAction(self.driver).tap(None, 950, 1350, 1).perform()
        self.app.find_element(PickPhotoLocators.iap)
        self.app.wait_time()
        self.app.screenshot("test_free_try_costume_look_panel")
        extra.append(extras.image('screenshot/test_free_try_costume_look_panel.png'))
        extra.append(extras.image('screenshot/test_free_try_costume_look_watermark.png'))


    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_free_try_hairdye_multi()
    t.teardown_method()
