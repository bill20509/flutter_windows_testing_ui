import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time


class TestMouth(object):
    def setup_method(self):  # run before every test
        # 設定device
        self.driver = App().set_udid("6L59ZXRCVS7XFUJ7")\
            .set_platform("Android")\
            .set_version("11")\
            .set_app("YMK")\
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.mouth
    def test_edit_lipcolor_sheer(self):
        self.app.deeplink_to_lipstick()\
            .pick_photo("YMK_test_photos", 4) \
            .waiting_cursor() \
            .select_brand("PERFECT")\
            .screenshot("test_edit_lipcolor_sheer_before", 3)\
            .select_color(1)\
            .screenshot("test_edit_lipcolor_sheer_after", 3)\
            .compare_photo("test_edit_lipcolor_sheer_before", "test_edit_lipcolor_sheer_after", "test_edit_lipcolor_sheer_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipcolor_sheer_save")

    @pytest.mark.mouth
    def test_edit_lipcolor_matte(self):
        self.app.deeplink_to_lipstick()\
            .pick_photo("YMK_test_photos", 4) \
            .waiting_cursor() \
            .select_brand("PERFECT")\
            .screenshot("test_edit_lipcolor_matte_before", 3)\
            .select_texture("Matte")\
            .screenshot("test_edit_lipcolor_matte_after", 3)\
            .compare_photo("test_edit_lipcolor_matte_before", "test_edit_lipcolor_matte_after", "test_edit_lipcolor_matte_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipcolor_matte_save")

    @pytest.mark.mouth
    def test_edit_lipcolor_gloss(self):
        self.app.deeplink_to_lipstick()\
            .pick_photo("YMK_test_photos", 4) \
            .waiting_cursor() \
            .select_brand("PERFECT")\
            .screenshot("test_edit_lipcolor_gloss_before", 3)\
            .select_texture("Gloss")\
            .screenshot("test_edit_lipcolor_gloss_after", 3)\
            .compare_photo("test_edit_lipcolor_gloss_before", "test_edit_lipcolor_gloss_after", "test_edit_lipcolor_gloss_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipcolor_gloss_save")

    @pytest.mark.mouth
    def test_edit_lipcolor_satin(self):
        self.app.deeplink_to_lipstick()\
            .pick_photo("YMK_test_photos", 4) \
            .waiting_cursor() \
            .select_brand("PERFECT")\
            .screenshot("test_edit_lipcolor_satin_before", 3)\
            .select_texture("Satin")\
            .screenshot("test_edit_lipcolor_satin_after", 3)\
            .compare_photo("test_edit_lipcolor_satin_before", "test_edit_lipcolor_satin_after", "test_edit_lipcolor_satin_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipcolor_satin_save")

    @pytest.mark.mouth
    def test_edit_lipcolor_shimmer(self):
        self.app.deeplink_to_lipstick()\
            .pick_photo("YMK_test_photos", 4) \
            .waiting_cursor() \
            .select_brand("PERFECT")\
            .screenshot("test_edit_lipcolor_shimmer_before", 3)\
            .select_texture("Shimmer")\
            .screenshot("test_edit_lipcolor_shimmer_after", 3)\
            .compare_photo("test_edit_lipcolor_shimmer_before", "test_edit_lipcolor_shimmer_after", "test_edit_lipcolor_shimmer_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipcolor_shimmer_save")

    @pytest.mark.mouth
    def test_edit_lipcolor_metallic(self):
        self.app.deeplink_to_lipstick()\
            .pick_photo("YMK_test_photos", 4) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .screenshot("test_edit_lipcolor_metallic_before", 3)\
            .select_texture("Metallic")\
            .screenshot("test_edit_lipcolor_metallic_after", 3)\
            .compare_photo("test_edit_lipcolor_metallic_before", "test_edit_lipcolor_metallic_after", "test_edit_lipcolor_metallic_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipcolor_metallic_save")

    @pytest.mark.mouth
    def test_edit_lipcolor_holographic(self):
        self.app.deeplink_to_lipstick()\
            .pick_photo("YMK_test_photos", 4) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .screenshot("test_edit_lipcolor_holographic_before", 3)\
            .select_texture("Holographic")\
            .screenshot("test_edit_lipcolor_holographic_after", 3)\
            .compare_photo("test_edit_lipcolor_holographic_before", "test_edit_lipcolor_holographic_after", "test_edit_lipcolor_holographic_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipcolor_holographic_save")


    @pytest.mark.mouth
    def test_edit_lipcolor_2colors(self):
        self.app.deeplink_to_lipstick()\
            .pick_photo("YMK_test_photos", 4) \
            .waiting_cursor() \
            .select_brand("PERFECT")\
            .screenshot("test_edit_lipcolor_2colors_before", 3)\
            .select_tab("2 COLORS")\
            .select_color(1)\
            .screenshot("test_edit_lipcolor_2colors_after", 3)\
            .compare_photo("test_edit_lipcolor_2colors_before", "test_edit_lipcolor_2colors_after", "test_edit_lipcolor_2colors_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipcolor_2colors_save")

    @pytest.mark.mouth
    def test_edit_lipcolor_ombre(self):
        self.app.deeplink_to_lipstick()\
            .pick_photo("YMK_test_photos", 4) \
            .waiting_cursor() \
            .select_brand("PERFECT")\
            .screenshot("test_edit_lipcolor_ombre_before", 3)\
            .select_tab("OMBRE")\
            .select_color(1)\
            .screenshot("test_edit_lipcolor_ombre_after", 3)\
            .compare_photo("test_edit_lipcolor_ombre_before", "test_edit_lipcolor_ombre_after", "test_edit_lipcolor_ombre_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipcolor_ombre_save")

    @pytest.mark.mouth
    def test_edit_lipart(self):
        self.app.deeplink_to_lipstick()\
            .pick_photo("YMK_test_photos", 4)\
            .select_lipart()\
            .screenshot("test_edit_lipart_before", 3) \
            .select_lipart_pattern(1)\
            .screenshot("test_edit_lipart_after", 3)\
            .compare_photo("test_edit_lipart_before", "test_edit_lipart_after", "test_edit_lipart_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipart_save")

    @pytest.mark.mouth
    def test_edit_lipcolor_intensity(self):
        self.app.deeplink_to_lipstick()\
            .pick_photo("YMK_test_photos", 4)\
            .waiting_cursor()\
            .select_brand("PERFECT")\
            .select_color(1)\
            .screenshot("test_edit_lipcolor_intensity_before", 3)\
            .adjust_intensity_to_top()\
            .screenshot("test_edit_lipcolor_intensity_after", 3)\
            .compare_photo("test_edit_lipcolor_intensity_before", "test_edit_lipcolor_intensity_after", "test_edit_lipcolor_intensity_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipcolor_intensity_save")


    @pytest.mark.mouth
    def test_edit_lipshape_size(self):
        self.app.deeplink_to_lipreshape()\
            .pick_photo("YMK_test_photos", 4)\
            .screenshot("test_edit_lipshape_size_before", 3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_lipshape_size_after", 3)\
            .compare_photo("test_edit_lipshape_size_before", "test_edit_lipshape_size_after", "test_edit_lipshape_size_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipshape_size_save")


    @pytest.mark.mouth
    def test_edit_lipshape_width(self):
        self.app.deeplink_to_lipreshape()\
            .pick_photo("YMK_test_photos", 4)\
            .select_lipreshape_function("Width")\
            .screenshot("test_edit_lipshape_width_before", 3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_lipshape_width_after", 3)\
            .compare_photo("test_edit_lipshape_width_before", "test_edit_lipshape_width_after", "test_edit_lipshape_width_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipshape_width_save")

    @pytest.mark.mouth
    def test_edit_lipshape_height(self):
        self.app.deeplink_to_lipreshape()\
            .pick_photo("YMK_test_photos", 4)\
            .select_lipreshape_function("Height")\
            .screenshot("test_edit_lipshape_height_before", 3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_lipshape_height_after", 3)\
            .compare_photo("test_edit_lipshape_height_before", "test_edit_lipshape_height_after", "test_edit_lipshape_height_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_lipshape_height_save")

    @pytest.mark.mouth
    def test_edit_lipshape_lippeak(self):
        self.app.deeplink_to_lipreshape() \
            .pick_photo("YMK_test_photos", 4) \
            .select_lipreshape_function("Lip Peak")\
            .screenshot("test_edit_lipshape_lippeak_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_lipshape_lippeak_after", 3) \
            .compare_photo("test_edit_lipshape_lippeak_before", "test_edit_lipshape_lippeak_after","test_edit_lipshape_lippeak_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_lipshape_lippeak_save")

    @pytest.mark.mouth
    def test_edit_smile(self):
        self.app.deeplink_to_smile() \
            .pick_photo("YMK_test_photos", 4) \
            .screenshot("test_edit_smile_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_smile_after", 3) \
            .compare_photo("test_edit_smile_before", "test_edit_smile_after","test_edit_smile_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_smile_save")

    @pytest.mark.mouth
    def test_edit_lip_plumper(self):
        self.app.deeplink_to_lipplumper() \
            .pick_photo("YMK_test_photos", 4) \
            .screenshot("test_edit_lip_plumper_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_lip_plumper_after", 3) \
            .compare_photo("test_edit_lip_plumper_before", "test_edit_lip_plumper_after","test_edit_lip_plumper_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_lip_plumper_save")

    @pytest.mark.mouth
    def test_edit_lip_wrinkle(self):
        self.app.deeplink_to_lipplumper() \
            .pick_photo("YMK_test_photos", 4) \
            .select_lipplumper_function("Lip Wrinkle")\
            .screenshot("test_edit_lip_wrinkle_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_lip_wrinkle_after", 3) \
            .compare_photo("test_edit_lip_wrinkle_before", "test_edit_lip_wrinkle_after","test_edit_lip_wrinkle_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_lip_wrinkle_save")

    @pytest.mark.mouth
    def test_edit_lip_teeth_whitener(self):
        self.app.deeplink_to_teethwhitener() \
            .pick_photo("YMK_test_photos", 3) \
            .screenshot("test_edit_lip_teeth_whitener_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_lip_teeth_whitener_after", 3) \
            .compare_photo("test_edit_lip_teeth_whitener_before", "test_edit_lip_teeth_whitener_after","test_edit_lip_teeth_whitener_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_lip_teeth_whitener_save")


    @pytest.mark.aa
    def test_edit_lip_art(self):
        self.app.deeplink_to_lipart() \
            .pick_photo("YMK_test_photos", 4) \
            .screenshot("test_edit_lip_art_before", 3) \
            .select_texture(1)\
            .screenshot("test_edit_lip_art_after", 3) \
            .compare_photo("test_edit_lip_art_before", "test_edit_lip_art_after","test_edit_lip_art_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_lip_art_save")

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
