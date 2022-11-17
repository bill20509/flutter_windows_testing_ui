import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
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
    @pytest.mark.S1
    def test_edit_lipcolor_texture_sheer(self, extra):
        self.app.deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_color(1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipcolor_texture_sheer_save")
        extra.append(extras.image('savephoto/1_test_edit_lipcolor_texture_sheer_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_lipcolor_texture_matte(self, extra):
        self.app.deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_texture("Matte") \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipcolor_texture_matte_save")
        extra.append(extras.image('savephoto/1_test_edit_lipcolor_texture_matte_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_lipcolor_texture_gloss(self, extra):
        self.app.deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_texture("Gloss") \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipcolor_texture_gloss_save")
        extra.append(extras.image('savephoto/1_test_edit_lipcolor_texture_gloss_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_lipcolor_texture_satin(self, extra):
        self.app.deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_texture("Satin") \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipcolor_texture_satin_save")
        extra.append(extras.image('savephoto/1_test_edit_lipcolor_texture_satin_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_lipcolor_texture_shimmer(self, extra):
        self.app.deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_texture("Shimmer") \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipcolor_texture_shimmer_save")
        extra.append(extras.image('savephoto/1_test_edit_lipcolor_texture_shimmer_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_lipcolor_texture_metallic(self, extra):
        self.app.deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_texture("Metallic") \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipcolor_texture_metallic_save")
        extra.append(extras.image('savephoto/1_test_edit_lipcolor_texture_metallic_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_lipcolor_texture_holographic(self, extra):
        self.app.deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_texture("Holographic") \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipcolor_texture_holographic_save")
        extra.append(extras.image('savephoto/1_test_edit_lipcolor_texture_holographic_save.jpg'))

    @pytest.mark.mouth
    def test_edit_lipcolor_2colors(self, extra):
        self.app.deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .screenshot("test_edit_lipcolor_2colors_before", 3) \
            .select_tab("2 COLORS") \
            .select_color(1) \
            .screenshot("test_edit_lipcolor_2colors_after", 3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipcolor_2colors_save")
        extra.append(extras.image('savephoto/1_test_edit_lipcolor_2colors_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_lipcolor_2colors_after.png'))
        extra.append(extras.image('screenshot/test_edit_lipcolor_2colors_before.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_lipcolor_ombre(self, extra):
        self.app.deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .screenshot("test_edit_lipcolor_ombre_before", 3) \
            .select_tab("OMBRE") \
            .select_color(1) \
            .screenshot("test_edit_lipcolor_ombre_after", 3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipcolor_ombre_save")
        extra.append(extras.image('savephoto/1_test_edit_lipcolor_ombre_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_lipcolor_ombre_after.png'))
        extra.append(extras.image('screenshot/test_edit_lipcolor_ombre_before.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_lipart(self, extra):
        self.app.deeplink_to_lipart() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_lipart_before", 3) \
            .select_lipart_pattern(1) \
            .screenshot("test_edit_lipart_after", 3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipart_save")
        extra.append(extras.image('savephoto/1_test_edit_lipart_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_lipart_after.png'))
        extra.append(extras.image('screenshot/test_edit_lipart_before.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_lipcolor_intensity(self, extra):
        self.app.deeplink_to_lipstick() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_color(1) \
            .screenshot("test_edit_lipcolor_intensity_before", 3) \
            .adjust_intensity_to_top() \
            .screenshot("test_edit_lipcolor_intensity_after", 3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipcolor_intensity_save") \
            .compose_gif("1_test_edit_lipcolor_intensity", 'screenshot/test_edit_lipcolor_intensity_before.png',
                         'screenshot/test_edit_lipcolor_intensity_after.png', speed=1)
        extra.append(extras.image('savephoto/1_test_edit_lipcolor_intensity_save.jpg'))
        extra.append(extras.image('screenshot/1_test_edit_lipcolor_intensity.gif'))
        # extra.append(extras.image('screenshot/test_edit_lipcolor_intensity_after.png'))
        # extra.append(extras.image('screenshot/test_edit_lipcolor_intensity_before.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_lipshape_size(self, extra):
        self.app.deeplink_to_lipreshape() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_lipshape_size_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_lipshape_size_after", 3) \
            .compare_photo("test_edit_lipshape_size_before", "test_edit_lipshape_size_after",
                           "test_edit_lipshape_size_diff") \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipshape_size_save") \
            .compose_gif("1_test_edit_lipshape_size", 'screenshot/test_edit_lipshape_size_before.png',
                         'screenshot/test_edit_lipshape_size_after.png', speed=1)
        extra.append(extras.image('savephoto/1_test_edit_lipshape_size_save.jpg'))
        extra.append(extras.image('screenshot/1_test_edit_lipshape_size.gif'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_size_diff.png'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_size_after.png'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_size_before.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_lipshape_width(self, extra):
        self.app.deeplink_to_lipreshape() \
            .pick_photo(folder_name, 1) \
            .select_lipreshape_function("Width") \
            .screenshot("test_edit_lipshape_width_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_lipshape_width_after", 3) \
            .compare_photo("test_edit_lipshape_width_before", "test_edit_lipshape_width_after",
                           "test_edit_lipshape_width_diff") \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipshape_width_save") \
            .compose_gif("1_test_edit_lipshape_width", 'screenshot/test_edit_lipshape_width_before.png',
                         'screenshot/test_edit_lipshape_width_after.png', speed=1)
        extra.append(extras.image('savephoto/1_test_edit_lipshape_width_save.jpg'))
        extra.append(extras.image('screenshot/1_test_edit_lipshape_width.gif'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_width_diff.png'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_width_after.png'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_width_before.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_lipshape_height(self, extra):
        self.app.deeplink_to_lipreshape() \
            .pick_photo(folder_name, 1) \
            .select_lipreshape_function("Height") \
            .screenshot("test_edit_lipshape_height_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_lipshape_height_after", 3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipshape_height_save") \
            .compose_gif("1_test_edit_lipshape_height", 'screenshot/test_edit_lipshape_height_before.png',
                         'screenshot/test_edit_lipshape_height_after.png', speed=1)
        extra.append(extras.image('savephoto/1_test_edit_lipshape_height_save.jpg'))
        extra.append(extras.image('screenshot/1_test_edit_lipshape_height.gif'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_height_diff.png'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_height_after.png'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_height_before.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_lipshape_lippeak(self, extra):
        self.app.deeplink_to_lipreshape() \
            .pick_photo(folder_name, 1) \
            .select_lipreshape_function("Lip Peak") \
            .screenshot("test_edit_lipshape_lippeak_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_lipshape_lippeak_after", 3) \
            .compare_photo("test_edit_lipshape_lippeak_before", "test_edit_lipshape_lippeak_after",
                           "test_edit_lipshape_lippeak_diff") \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lipshape_lippeak_save") \
            .compose_gif("1_test_edit_lipshape_lippeak", 'screenshot/test_edit_lipshape_lippeak_before.png',
                         'screenshot/test_edit_lipshape_lippeak_after.png', speed=1)
        extra.append(extras.image('savephoto/1_test_edit_lipshape_lippeak_save.jpg'))
        extra.append(extras.image('screenshot/1_test_edit_lipshape_lippeak.gif'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_lippeak_diff.png'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_lippeak_after.png'))
        # extra.append(extras.image('screenshot/test_edit_lipshape_lippeak_before.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_smile(self, extra):
        self.app.deeplink_to_smile() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_smile_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_smile_after", 3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_smile_save") \
            .compose_gif("1_test_edit_smile", 'screenshot/test_edit_smile_before.png',
                         'screenshot/test_edit_smile_after.png', speed=1)
        extra.append(extras.image('savephoto/1_test_edit_smile_save.jpg'))
        extra.append(extras.image('screenshot/1_test_edit_smile.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_lip_plumper(self, extra):
        self.app.deeplink_to_lipplumper() \
            .pick_photo(folder_name, 1) \
            .screenshot("test_edit_lip_plumper_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_lip_plumper_after", 3) \
            .compare_photo("test_edit_lip_plumper_before", "test_edit_lip_plumper_after", "test_edit_lip_plumper_diff") \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lip_plumper_save") \
            .compose_gif("1_test_edit_lip_plumper", 'screenshot/test_edit_lip_plumper_before.png',
                         'screenshot/test_edit_lip_plumper_after.png', speed=1)
        extra.append(extras.image('savephoto/1_test_edit_lip_plumper_save.jpg'))
        extra.append(extras.image('screenshot/1_test_edit_lip_plumper.gif'))
        # extra.append(extras.image('screenshot/test_edit_lip_plumper_diff.png'))
        # extra.append(extras.image('screenshot/test_edit_lip_plumper_after.png'))
        # extra.append(extras.image('screenshot/test_edit_lip_plumper_before.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_lip_wrinkle(self, extra):
        self.app.deeplink_to_lipplumper() \
            .pick_photo(folder_name, 1) \
            .select_lipplumper_function("Lip Wrinkle") \
            .screenshot("test_edit_lip_wrinkle_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_lip_wrinkle_after", 3) \
            .compare_photo("test_edit_lip_wrinkle_before", "test_edit_lip_wrinkle_after", "test_edit_lip_wrinkle_diff") \
            .click_save() \
            .pull_photo_from_device("1_test_edit_lip_wrinkle_save") \
            .compose_gif("1_test_edit_lip_wrinkle", 'screenshot/test_edit_lip_wrinkle_before.png',
                         'screenshot/test_edit_lip_wrinkle_after.png', speed=1)
        extra.append(extras.image('savephoto/1_test_edit_lip_wrinkle_save.jpg'))
        extra.append(extras.image('screenshot/1_test_edit_lip_wrinkle.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_lip_teeth_whitener(self, extra):
        self.app.deeplink_to_teethwhitener() \
            .pick_photo("5.Wrinkle", 1) \
            .screenshot("test_edit_lip_teeth_whitener_before", 3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_lip_teeth_whitener_after", 3) \
            .click_save() \
            .pull_photo_from_device("5_test_edit_lip_teeth_whitener_save")
        extra.append(extras.image('savephoto/5_test_edit_lip_teeth_whitener_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_lip_teeth_whitener_after.png'))
        extra.append(extras.image('screenshot/test_edit_lip_teeth_whitener_before.png'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
