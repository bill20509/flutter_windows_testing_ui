import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
from pytest_html import extras
folder_name = "5.Wrinkle"


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
    @pytest.mark.S1
    def test_all_effects(self, extra):
        self.app.deeplink_to_setting() \
            .login_bc_account("bb@bb.com", "bbbbbb")
        start_time = time.time()
        self.app.deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_color(1) \
            .waiting_cursor() \
            .message("lip color applied!") \
            .select_lipreshape()\
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_lipreshape_function("Width") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_lipreshape_function("Height") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_lipreshape_function("Lip Peak") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .message("all mouth reshape applied!") \
            .select_smile() \
            .waiting_cursor() \
            .adjust_intensity_to_right() \
            .message("smile applied!") \
            .select_lipplumper()\
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .message("lip plumper applied!") \
            .select_lipplumper_function("Lip Wrinkle") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .message("lip wrinkle applied!") \
            .select_teethwhitener()\
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .message("teeth whitener applied!") \
            .select_lipart()\
            .select_lipart_pattern(1) \
            .waiting_cursor() \
            .message("all mouth functions applied!") \
            .select_face()\
            .select_smoother() \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .message("smoother applied!") \
            .select_faceshape() \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_faceshape_function("Chin Shape") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_faceshape_function("Chin Length") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_faceshape_function("Width") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_faceshape_function("Cheek") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_faceshape_function("Cheekbone") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_faceshape_function("Jaw") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_faceshape_function("Forehead") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .message("all face reshape applied!")\
            .select_noseenhance() \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_noseenhance_function("Size") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_noseenhance_function("Lift") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_noseenhance_function("Bridge") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_noseenhance_function("Tip") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_noseenhance_function("Wing") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_noseenhance_function("Width") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .message("all nose reshape applied!") \
            .select_wrinkle() \
            .wait_animation() \
            .message("wrinkle applied!") \
            .select_redness() \
            .wait_animation() \
            .message("redness applied!") \
            .select_Unevenskintone()\
            .wait_animation() \
            .message("uneven skintone applied!") \
            .select_pores()\
            .wait_animation() \
            .message("pore applied!") \
            .select_foundation() \
            .select_color(1) \
            .waiting_cursor() \
            .message("foundation applied!") \
            .select_concealer() \
            .wait_animation()\
            .waiting_cursor() \
            .message("concealer applied!") \
            .select_blush() \
            .select_color(1) \
            .waiting_cursor() \
            .message("blush applied!") \
            .select_contour() \
            .select_pattern(1) \
            .waiting_cursor() \
            .select_highlight() \
            .select_pattern(1) \
            .waiting_cursor() \
            .message("contour/highlight applied!") \
            .select_facepaint() \
            .waiting_cursor() \
            .select_pattern(1) \
            .waiting_cursor() \
            .message("face paint applied!") \
            .select_blemish() \
            .switch_onoff() \
            .waiting_cursor() \
            .message("blemish applied!") \
            .select_shineremoval() \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .message("all face functions applied!") \
            .select_eye()\
            .select_eyeliner() \
            .select_color(1) \
            .waiting_cursor() \
            .message("eye liner applied!") \
            .select_eyelashes() \
            .select_brand("PERFECT") \
            .click_mascara()\
            .select_color(1) \
            .waiting_cursor() \
            .message("eyelashes applied!") \
            .select_eyeshadow() \
            .select_brand("PERFECT") \
            .select_collection("4 Colors") \
            .waiting_cursor() \
            .message("eye shadow applied!") \
            .select_darkcircle()\
            .wait_animation() \
            .message("dark circle applied!") \
            .select_eyetuner() \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_eyetuner_function("Width") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_eyetuner_function("Height") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_eyetuner_function("Distance") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .select_eyetuner_function("Angle") \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .message("all eye reshape applied!") \
            .select_eyebrows() \
            .select_brand("PERFECT") \
            .waiting_cursor() \
            .select_pattern(2) \
            .waiting_cursor() \
            .message("eyebrow applied!") \
            .select_eyecolor() \
            .select_color(1) \
            .waiting_cursor() \
            .message("eye color applied!") \
            .select_eyebag() \
            .wait_animation() \
            .message("eye bag applied!") \
            .select_brighten() \
            .adjust_intensity_to_right() \
            .waiting_cursor() \
            .message("brighten applied!") \
            .select_doubleeyelid() \
            .select_pattern(1)\
            .waiting_cursor() \
            .message("double eyelids applied!") \
            .select_redeye() \
            .switch_onoff() \
            .message("all face functions applied!") \
            .select_hair()\
            .select_haircolor() \
            .select_color(4)\
            .waiting_cursor()\
            .select_hairstyle() \
            .waiting_cursor() \
            .wait_time()\
            .select_style("Wispy") \
            .waiting_cursor()\
            .message("all hair functions applied!") \
            .select_effects() \
            .select_collection(1) \
            .select_effect(1) \
            .message("effect applied!") \
            .select_background() \
            .select_background_item(2) \
            .message("background applied!") \
            .select_accessories() \
            .waiting_cursor() \
            .select_pattern(2) \
            .waiting_cursor() \
            .message("eyewear applied!") \
            .select_headband() \
            .waiting_cursor() \
            .select_headband_pattern(1) \
            .waiting_cursor() \
            .message("headband applied!") \
            .select_necklace() \
            .waiting_cursor() \
            .select_necklace_pattern(1) \
            .waiting_cursor() \
            .message("necklace applied!") \
            .select_earrings() \
            .waiting_cursor() \
            .select_earring_pattern(1) \
            .waiting_cursor() \
            .message("earrings applied!") \
            .select_hat() \
            .waiting_cursor() \
            .select_hat_pattern(3) \
            .waiting_cursor() \
            .message("hat applied!") \
            .add_to_favorite()\
            .waiting_cursor()\
            .message("add to favorite!") \
            .click_save() \
            .show_result_page() \
            .message("look saved!") \
            .pull_photo_from_device("5_all_effects_save")\
            .share_look("test_all_effects(auto test)")\
            .screenshot("5_all_effects_save", 3)
        end_time = time.time()
        print("完成花費時間:%f seconds" % (end_time - start_time))
        extra.append(extras.image('savephoto/5_all_effects_save.jpg'))
        extra.append(extras.image('screenshot/5_all_effects_save.png'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
