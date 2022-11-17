from pytest_html import extras
import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
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
    def test_edit_eyeliner_color(self, extra):
        self.app.deeplink_to_eyeliner() \
            .pick_photo(folder_name, 1) \
            .select_brand("PERFECT") \
            .screenshot("test_edit_eyeliner_color_before", 1) \
            .select_color(5) \
            .adjust_intensity_to_top() \
            .screenshot("test_edit_eyeliner_color_after", 1) \
            .compare_photo("test_edit_eyeliner_color_before", "test_edit_eyeliner_color_after"
                           , "test_edit_eyeliner_color_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eyeliner_color") \
            .compose_gif("test_edit_eyeliner_color", 'screenshot/test_edit_eyeliner_color_before.png'
                         , 'screenshot/test_edit_eyeliner_color_after.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eyeliner_color.jpg'))
        extra.append(extras.image('screenshot/test_edit_eyeliner_color.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eyeliner_pattern(self, extra):
        self.app.deeplink_to_eyeliner() \
            .pick_photo(folder_name, 1) \
            .select_brand("PERFECT") \
            .click_pattern() \
            .screenshot("test_edit_eyeliner_pattern_before", 1) \
            .select_pattern(2) \
            .screenshot("test_edit_eyeliner_pattern_after", 1) \
            .compare_photo("test_edit_eyeliner_pattern_before", "test_edit_eyeliner_pattern_after"
                           , "test_edit_eyeliner_pattern_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eyeliner_pattern") \
            .compose_gif("test_edit_eyeliner_pattern", 'screenshot/test_edit_eyeliner_pattern_before.png'
                         , 'screenshot/test_edit_eyeliner_pattern_after.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eyeliner_pattern.jpg'))
        extra.append(extras.image('screenshot/test_edit_eyeliner_pattern.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eyelashes_pattern(self, extra):
        self.app.deeplink_to_eyelashes() \
            .pick_photo(folder_name, 1) \
            .click_eyelashes() \
            .select_brand("PERFECT") \
            .screenshot("test_edit_eyelashes_pattern_before", 1) \
            .select_pattern(2) \
            .screenshot("test_edit_eyelashes_pattern_after", 1) \
            .compare_photo("test_edit_eyelashes_pattern_before", "test_edit_eyelashes_pattern_after"
                           , "test_edit_eyelashes_pattern_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eyelashes_pattern") \
            .compose_gif("test_edit_eyelashes_pattern", 'screenshot/test_edit_eyelashes_pattern_before.png'
                         , 'screenshot/test_edit_eyelashes_pattern_after.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eyelashes_pattern.jpg'))
        extra.append(extras.image('screenshot/test_edit_eyelashes_pattern.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eyelashes_mascara(self, extra):
        self.app.deeplink_to_eyelashes() \
            .pick_photo(folder_name, 1) \
            .click_mascara() \
            .select_brand("PERFECT") \
            .screenshot("test_edit_eyelashes_mascara_before", 1) \
            .select_color(5) \
            .screenshot("test_edit_eyelashes_mascara_after", 1) \
            .compare_photo("test_edit_eyelashes_mascara_before", "test_edit_eyelashes_mascara_after"
                           , "test_edit_eyelashes_mascara_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eyelashes_mascara") \
            .compose_gif("test_edit_eyelashes_mascara", 'screenshot/test_edit_eyelashes_mascara_before.png'
                         , 'screenshot/test_edit_eyelashes_mascara_after.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eyelashes_mascara.jpg'))
        extra.append(extras.image('screenshot/test_edit_eyelashes_mascara.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_dark_circle(self, extra):
        self.app.deeplink_to_darkcircle() \
            .pick_photo(folder_name, 1) \
            .wait_animation() \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_dark_circle_before", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_dark_circle_after", 1) \
            .compare_photo("test_edit_dark_circle_before", "test_edit_dark_circle_after", "test_edit_dark_circle_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_dark_circle") \
            .compose_gif("test_edit_dark_circle", 'screenshot/test_edit_dark_circle_before.png'
                         , 'screenshot/test_edit_dark_circle_after.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_dark_circle.jpg'))
        extra.append(extras.image('screenshot/test_edit_dark_circle.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eye_contact_pattern(self, extra):
        self.app.deeplink_to_eyecolor() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .screenshot("test_edit_eye_contact_pattern_before", 1) \
            .select_color(2) \
            .screenshot("test_edit_eye_contact_pattern_after", 1) \
            .select_color(1) \
            .screenshot("test_edit_eye_contact_pattern_after2", 1) \
            .compare_photo("test_edit_eye_contact_pattern_before", "test_edit_eye_contact_pattern_after2"
                           , "test_edit_eye_contact_pattern_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_contact_pattern") \
            .compose_gif("test_edit_eye_contact_pattern", 'screenshot/test_edit_eye_contact_pattern_before.png'
                         , 'screenshot/test_edit_eye_contact_pattern_after.png'
                         , 'screenshot/test_edit_eye_contact_pattern_after2.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_contact_pattern.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_contact_pattern.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eye_contact_color(self, extra):
        self.app.deeplink_to_eyecolor() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .click_color() \
            .select_color(1) \
            .screenshot("test_edit_eye_contact_color_before", 1) \
            .select_color(7) \
            .screenshot("test_edit_eye_contact_color_after", 1) \
            .set_color_to_100() \
            .screenshot("test_edit_eye_contact_color_after2", 1) \
            .compare_photo("test_edit_eye_contact_color_before", "test_edit_eye_contact_color_after2"
                           , "test_edit_eye_contact_color_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_contact_color") \
            .compose_gif("test_edit_eye_contact_color", 'screenshot/test_edit_eye_contact_color_before.png'
                         , 'screenshot/test_edit_eye_contact_color_after.png'
                         , 'screenshot/test_edit_eye_contact_color_after2.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_contact_color.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_contact_color.gif'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_eye_contact_size(self, extra):
        self.app.deeplink_to_eyecolor() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .click_color() \
            .select_color(7) \
            .screenshot("test_edit_eye_contact_size_before", 1) \
            .set_size_to_100() \
            .screenshot("test_edit_eye_contact_size_after", 1) \
            .compare_photo("test_edit_eye_contact_size_before", "test_edit_eye_contact_size_after"
                           , "test_edit_eye_contact_size_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_contact_size") \
            .compose_gif("test_edit_eye_contact_size", 'screenshot/test_edit_eye_contact_size_before.png'
                         , 'screenshot/test_edit_eye_contact_size_after.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_contact_size.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_contact_size.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eye_bag(self, extra):
        self.app.deeplink_to_eyebag() \
            .pick_photo(folder_name, 1) \
            .wait_animation() \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_eye_bag_before", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_eye_bag_after", 1) \
            .compare_photo("test_edit_eye_bag_before", "test_edit_eye_bag_after", "test_edit_eye_bag_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_bag") \
            .compose_gif("test_edit_eye_bag", 'screenshot/test_edit_eye_bag_before.png'
                         , 'screenshot/test_edit_eye_bag_after.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_bag.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_bag.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eye_brighten(self, extra):
        self.app.deeplink_to_brighten() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .screenshot("test_edit_eye_brighten_before", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_eye_brighten_after", 1) \
            .compare_photo("test_edit_eye_brighten_before", "test_edit_eye_brighten_after"
                           , "test_edit_eye_brighten_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_brighten") \
            .compose_gif("test_edit_eye_brighten", 'screenshot/test_edit_eye_brighten_before.png'
                         , 'screenshot/test_edit_eye_brighten_after.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_brighten.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_brighten.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_double_eyelid(self, extra):
        self.app.deeplink_to_doubleeyelid() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .screenshot("test_edit_double_eyelid_before", 1) \
            .select_pattern(2) \
            .adjust_intensity_to_top() \
            .screenshot("test_edit_double_eyelid_after", 1) \
            .compare_photo("test_edit_double_eyelid_before", "test_edit_double_eyelid_after"
                           , "test_edit_double_eyelid_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_double_eyelid") \
            .compose_gif("test_edit_double_eyelid", 'screenshot/test_edit_double_eyelid_before.png'
                         , 'screenshot/test_edit_double_eyelid_after.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_double_eyelid.jpg'))
        extra.append(extras.image('screenshot/test_edit_double_eyelid.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_red_eye(self, extra):
        self.app.deeplink_to_redeye() \
            .pick_photo("6.Red_eyes", 1) \
            .waiting_cursor() \
            .screenshot("test_edit_red_eye_before", 1) \
            .switch_onoff() \
            .screenshot("test_edit_red_eye_after", 1) \
            .compare_photo("test_edit_red_eye_before", "test_edit_red_eye_after", "test_edit_red_eye_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_red_eye") \
            .compose_gif("test_edit_red_eye", 'screenshot/test_edit_red_eye_before.png'
                         , 'screenshot/test_edit_red_eye_after.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_red_eye.jpg'))
        extra.append(extras.image('screenshot/test_edit_red_eye.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_brow_reshape_height(self, extra):
        self.app.deeplink_to_browreshape() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .screenshot("test_edit_brow_reshape_height_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_brow_reshape_height_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_brow_reshape_height_after+100", 1) \
            .compare_photo("test_edit_brow_reshape_height_before", "test_edit_brow_reshape_height_after+100"
                           , "test_edit_brow_reshape_height_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_brow_reshape_height") \
            .compose_gif("test_edit_brow_reshape_height", 'screenshot/test_edit_brow_reshape_height_before.png'
                         , 'screenshot/test_edit_brow_reshape_height_after-100.png'
                         , 'screenshot/test_edit_brow_reshape_height_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_brow_reshape_height.jpg'))
        extra.append(extras.image('screenshot/test_edit_brow_reshape_height.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_brow_reshape_thickness(self, extra):
        self.app.deeplink_to_browreshape() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_browsreshape_function("Thickness") \
            .screenshot("test_edit_brow_reshape_thickness_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_brow_reshape_thickness_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_brow_reshape_thickness_after+100", 1) \
            .compare_photo("test_edit_brow_reshape_thickness_before", "test_edit_brow_reshape_thickness_after+100"
                           , "test_edit_brow_reshape_thickness_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_brow_reshape_thickness") \
            .compose_gif("test_edit_brow_reshape_thickness", 'screenshot/test_edit_brow_reshape_thickness_before.png'
                         , 'screenshot/test_edit_brow_reshape_thickness_after-100.png'
                         , 'screenshot/test_edit_brow_reshape_thickness_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_brow_reshape_thickness.jpg'))
        extra.append(extras.image('screenshot/test_edit_brow_reshape_thickness.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_brow_reshape_arch(self, extra):
        self.app.deeplink_to_browreshape() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_browsreshape_function("Arch") \
            .screenshot("test_edit_brow_reshape_arch_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_brow_reshape_arch_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_brow_reshape_arch_after+100", 1) \
            .compare_photo("test_edit_brow_reshape_arch_before", "test_edit_brow_reshape_arch_after+100"
                           , "test_edit_brow_reshape_arch_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_brow_reshape_arch") \
            .compose_gif("test_edit_brow_reshape_arch", 'screenshot/test_edit_brow_reshape_arch_before.png'
                         , 'screenshot/test_edit_brow_reshape_arch_after-100.png'
                         , 'screenshot/test_edit_brow_reshape_arch_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_brow_reshape_arch.jpg'))
        extra.append(extras.image('screenshot/test_edit_brow_reshape_arch.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_brow_reshape_distance(self, extra):
        self.app.deeplink_to_browreshape() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_browsreshape_function("Distance") \
            .screenshot("test_edit_brow_reshape_distance_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_brow_reshape_distance_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_brow_reshape_distance_after+100", 1) \
            .compare_photo("test_edit_brow_reshape_distance_before", "test_edit_brow_reshape_distance_after+100"
                           , "test_edit_brow_reshape_distance_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_brow_reshape_distance") \
            .compose_gif("test_edit_brow_reshape_distance"
                         , 'screenshot/test_edit_brow_reshape_distance_before.png'
                         , 'screenshot/test_edit_brow_reshape_distance_after-100.png'
                         , 'screenshot/test_edit_brow_reshape_distance_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_brow_reshape_distance.jpg'))
        extra.append(extras.image('screenshot/test_edit_brow_reshape_distance.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eye_reshape_size_overall(self, extra):
        self.app.deeplink_to_eyetuner() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .screenshot("test_edit_eye_reshape_size_overall_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_eye_reshape_size_overall_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_eye_reshape_size_overall_after+100", 1) \
            .compare_photo("test_edit_eye_reshape_size_overall_before", "test_edit_eye_reshape_size_overall_after+100"
                           , "test_edit_eye_reshape_size_overall_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_reshape_size_overall") \
            .compose_gif("test_edit_eye_reshape_size_overall"
                         , 'screenshot/test_edit_eye_reshape_size_overall_before.png'
                         , 'screenshot/test_edit_eye_reshape_size_overall_after-100.png'
                         , 'screenshot/test_edit_eye_reshape_size_overall_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_reshape_size_overall.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_reshape_size_overall.gif'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_eye_reshape_size_left(self, extra):
        self.app.deeplink_to_eyetuner() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_left() \
            .screenshot("test_edit_eye_reshape_size_left_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_eye_reshape_size_left_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_eye_reshape_size_left_after+100", 1) \
            .compare_photo("test_edit_eye_reshape_size_left_before", "test_edit_eye_reshape_size_left_after+100", "test_edit_eye_reshape_size_left_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_reshape_size_left") \
            .compose_gif("test_edit_eye_reshape_size_left", 'screenshot/test_edit_eye_reshape_size_left_before.png'
                         , 'screenshot/test_edit_eye_reshape_size_left_after-100.png'
                         , 'screenshot/test_edit_eye_reshape_size_left_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_reshape_size_left.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_reshape_size_left.gif'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_eye_reshape_size_right(self, extra):
        self.app.deeplink_to_eyetuner() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .click_right() \
            .screenshot("test_edit_eye_reshape_size_right_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_eye_reshape_size_right_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_eye_reshape_size_right_after+100", 1) \
            .compare_photo("test_edit_eye_reshape_size_right_before", "test_edit_eye_reshape_size_right_after+100"
                           , "test_edit_eye_reshape_size_right_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_reshape_size_right") \
            .compose_gif("test_edit_eye_reshape_size_right", 'screenshot/test_edit_eye_reshape_size_right_before.png'
                         , 'screenshot/test_edit_eye_reshape_size_right_after-100.png'
                         , 'screenshot/test_edit_eye_reshape_size_right_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_reshape_size_right.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_reshape_size_right.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eye_reshape_width(self, extra):
        self.app.deeplink_to_eyetuner() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_eyetuner_function("Width") \
            .screenshot("test_edit_eye_reshape_width_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_eye_reshape_width_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_eye_reshape_width_after+100", 1) \
            .compare_photo("test_edit_eye_reshape_width_before", "test_edit_eye_reshape_width_after+100"
                           , "test_edit_eye_reshape_width_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_reshape_width") \
            .compose_gif("test_edit_eye_reshape_width", 'screenshot/test_edit_eye_reshape_width_before.png'
                         , 'screenshot/test_edit_eye_reshape_width_after-100.png'
                         , 'screenshot/test_edit_eye_reshape_width_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_reshape_width.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_reshape_width.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eye_reshape_height(self, extra):
        self.app.deeplink_to_eyetuner() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_eyetuner_function("Height") \
            .screenshot("test_edit_eye_reshape_height_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_eye_reshape_height_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_eye_reshape_height_after+100", 1) \
            .compare_photo("test_edit_eye_reshape_height_before", "test_edit_eye_reshape_height_after+100"
                           , "test_edit_eye_reshape_height_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_reshape_height") \
            .compose_gif("test_edit_eye_reshape_height", 'screenshot/test_edit_eye_reshape_height_before.png'
                         , 'screenshot/test_edit_eye_reshape_height_after-100.png'
                         , 'screenshot/test_edit_eye_reshape_height_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_reshape_height.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_reshape_height.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eye_reshape_distance(self, extra):
        self.app.deeplink_to_eyetuner() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_eyetuner_function("Distance") \
            .screenshot("test_edit_eye_reshape_distance_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_eye_reshape_distance_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_eye_reshape_distance_after+100", 1) \
            .compare_photo("test_edit_eye_reshape_distance_before", "test_edit_eye_reshape_distance_after+100"
                           , "test_edit_eye_reshape_distance_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_reshape_distance") \
            .compose_gif("test_edit_eye_reshape_distance", 'screenshot/test_edit_eye_reshape_distance_before.png'
                         , 'screenshot/test_edit_eye_reshape_distance_after-100.png'
                         , 'screenshot/test_edit_eye_reshape_distance_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_reshape_distance.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_reshape_distance.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eye_reshape_angle(self, extra):
        self.app.deeplink_to_eyetuner() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_eyetuner_function("Angle") \
            .screenshot("test_edit_eye_reshape_angle_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_eye_reshape_angle_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_eye_reshape_angle_after+100", 1) \
            .compare_photo("test_edit_eye_reshape_angle_before", "test_edit_eye_reshape_angle_after+100"
                           , "test_edit_eye_reshape_angle_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_reshape_angle") \
            .compose_gif("test_edit_eye_reshape_angle", 'screenshot/test_edit_eye_reshape_angle_before.png'
                         , 'screenshot/test_edit_eye_reshape_angle_after-100.png'
                         , 'screenshot/test_edit_eye_reshape_angle_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_reshape_angle.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_reshape_angle.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eyebrows_color(self, extra):
        self.app.deeplink_to_eyebrows() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_pattern(1) \
            .click_color() \
            .screenshot("test_edit_eyebrows_color_before", 1) \
            .select_color(6) \
            .screenshot("test_edit_eyebrows_color_after", 1) \
            .set_color_to_100() \
            .screenshot("test_edit_eyebrows_color_after+100", 1) \
            .compare_photo("test_edit_eyebrows_color_before", "test_edit_eyebrows_color_after+100"
                           , "test_edit_eyebrows_color_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eyebrows_color") \
            .compose_gif("test_edit_eyebrows_color", 'screenshot/test_edit_eyebrows_color_before.png'
                         , 'screenshot/test_edit_eyebrows_color_after.png'
                         , 'screenshot/test_edit_eyebrows_color_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eyebrows_color.jpg'))
        extra.append(extras.image('screenshot/test_edit_eyebrows_color.gif'))

    @pytest.mark.B
    @pytest.mark.YMK
    def test_edit_eyebrows_shape(self, extra):
        self.app.deeplink_to_eyebrows() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_pattern(1) \
            .screenshot("test_edit_eyebrows_shape_before", 1) \
            .set_shape_to_0() \
            .screenshot("test_edit_eyebrows_shape_after+0", 1) \
            .set_shape_to_100() \
            .screenshot("test_edit_eyebrows_shape_after+100", 1) \
            .compare_photo("test_edit_eyebrows_shape_before", "test_edit_eyebrows_shape_after+100"
                           , "test_edit_eyebrows_shape_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eyebrows_shape") \
            .compose_gif("test_edit_eyebrows_shape", 'screenshot/test_edit_eyebrows_shape_before.png'
                         , 'screenshot/test_edit_eyebrows_shape_after+0.png'
                         , 'screenshot/test_edit_eyebrows_shape_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eyebrows_shape.jpg'))
        extra.append(extras.image('screenshot/test_edit_eyebrows_shape.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eyebrows_pattern(self, extra):
        self.app.deeplink_to_eyebrows() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .screenshot("test_edit_eyebrows_pattern_before", 1) \
            .select_pattern(1) \
            .set_color_to_100() \
            .set_shape_to_100() \
            .screenshot("test_edit_eyebrows_pattern_pattern1", 1) \
            .select_pattern(2) \
            .set_color_to_100() \
            .set_shape_to_100() \
            .screenshot("test_edit_eyebrows_pattern_pattern2", 1) \
            .compare_photo("test_edit_eyebrows_pattern_before", "test_edit_eyebrows_pattern_pattern2"
                           , "test_edit_eyebrows_pattern_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eyebrows_pattern") \
            .compose_gif("test_edit_eyebrows_pattern", 'screenshot/test_edit_eyebrows_pattern_before.png'
                         , 'screenshot/test_edit_eyebrows_pattern_pattern1.png'
                         , 'screenshot/test_edit_eyebrows_pattern_pattern2.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eyebrows_pattern.jpg'))
        extra.append(extras.image('screenshot/test_edit_eyebrows_pattern.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eye_shadow_color(self, extra):
        self.app.deeplink_to_eyeshadow() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .screenshot("test_edit_eye_shadow_color_before", 1) \
            .select_brand("PERFECT") \
            .select_collection("3 Colors") \
            .screenshot("test_edit_eye_shadow_color_after_3_Colors", 1) \
            .select_brand("PERFECT") \
            .select_collection("4 Colors") \
            .screenshot("test_edit_eye_shadow_color_after_4_Colors", 1) \
            .compare_photo("test_edit_eye_shadow_color_before", "test_edit_eye_shadow_color_after_4_Colors"
                           , "test_edit_eye_shadow_color_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_shadow_color") \
            .compose_gif("test_edit_eye_shadow_color", 'screenshot/test_edit_eye_shadow_color_before.png'
                         , 'screenshot/test_edit_eye_shadow_color_after_3_Colors.png'
                         , 'screenshot/test_edit_eye_shadow_color_after_4_Colors.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_shadow_color.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_shadow_color.gif'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_eye_shadow_pattern(self, extra):
        self.app.deeplink_to_eyeshadow() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_collection("1 Color") \
            .screenshot("test_edit_eye_shadow_pattern_before", 1) \
            .click_pattern() \
            .screenshot("test_edit_eye_shadow_pattern_pattern_1", 1) \
            .select_pattern(4) \
            .screenshot("test_edit_eye_shadow_pattern_pattern_2", 1) \
            .compare_photo("test_edit_eye_shadow_pattern_before", "test_edit_eye_shadow_pattern_pattern_2"
                           , "test_edit_eye_shadow_pattern_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_shadow_pattern") \
            .compose_gif("test_edit_eye_shadow_pattern", 'screenshot/test_edit_eye_shadow_pattern_before.png'
                         , 'screenshot/test_edit_eye_shadow_pattern_pattern_1.png'
                         , 'screenshot/test_edit_eye_shadow_pattern_pattern_2.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_shadow_pattern.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_shadow_pattern.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_eye_shadow_shimmer(self, extra):
        self.app.deeplink_to_eyeshadow() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_collection("1 Color") \
            .select_palette_box1() \
            .screenshot("test_edit_eye_shadow_shimmer_before", 1) \
            .click_shimmer_icon() \
            .screenshot("test_edit_eye_shadow_shimmer_after", 1) \
            .compare_photo("test_edit_eye_shadow_shimmer_before", "test_edit_eye_shadow_shimmer_after"
                           , "test_edit_eye_shadow_shimmer_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_shadow_shimmer") \
            .compose_gif("test_edit_eye_shadow_shimmer", 'screenshot/test_edit_eye_shadow_shimmer_before.png'
                         , 'screenshot/test_edit_eye_shadow_shimmer_after.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_shadow_shimmer.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_shadow_shimmer.gif'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_eye_shadow_intensity(self, extra):
        self.app.deeplink_to_eyeshadow() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_collection("1 Color") \
            .select_palette_box1() \
            .screenshot("test_edit_eye_shadow_intensity_before", 1) \
            .adjust_intensity_to_down() \
            .screenshot("test_edit_eye_shadow_intensity_after_0", 1) \
            .adjust_intensity_to_top() \
            .screenshot("test_edit_eye_shadow_intensity_after_100", 1) \
            .compare_photo("test_edit_eye_shadow_intensity_before", "test_edit_eye_shadow_intensity_after_100"
                           , "test_edit_eye_shadow_intensity_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eye_shadow_intensity") \
            .compose_gif("test_edit_eye_shadow_intensity", 'screenshot/test_edit_eye_shadow_intensity_before.png'
                         , 'screenshot/test_edit_eye_shadow_intensity_after_0.png'
                         , 'screenshot/test_edit_eye_shadow_intensity_after_100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eye_shadow_intensity.jpg'))
        extra.append(extras.image('screenshot/test_edit_eye_shadow_intensity.gif'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_eye_shadow_add_delete_palette(self, extra):
        self.app.deeplink_to_eyeshadow() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_collection("4 Colors") \
            .select_palette_box1() \
            .click_palette_colorball() \
            .adjust_intensity_to_top() \
            .screenshot("test_edit_eye_shadow_add_palette_before", 1) \
            .click_heart_icon() \
            .screenshot("test_edit_eye_shadow_add_palette_after", 1) \
            .compare_photo("test_edit_eye_shadow_add_palette_before", "test_edit_eye_shadow_add_palette_after",
                           "test_edit_eye_shadow_add_palette_diff") \
            .compose_gif("test_edit_eye_shadow_add_palette", 'screenshot/test_edit_eye_shadow_add_palette_before.png'
                         , 'screenshot/test_edit_eye_shadow_add_palette_after.png', speed=2) \
            .select_palette_box1() \
            .click_palette_colorball() \
            .click_heart_icon() \
            .select_brand("PERFECT") \
            .select_collection("Favorite") \
            .click_extra() \
            .screenshot("test_edit_eye_shadow_delete_palette_before", 1) \
            .long_press_palette() \
            .delete_palette() \
            .screenshot("test_edit_eye_shadow_delete_palette_after", 1) \
            .compare_photo("test_edit_eye_shadow_delete_palette_before", "test_edit_eye_shadow_delete_palette_after"
                           , "test_edit_eye_shadow_delete_palette_diff") \
            .click_keycode_back() \
            .compose_gif("test_edit_eye_shadow_delete_palette"
                         , 'screenshot/test_edit_eye_shadow_delete_palette_before.png'
                         , 'screenshot/test_edit_eye_shadow_delete_palette_after.png', speed=2)
        extra.append(extras.image('screenshot/test_edit_eye_shadow_delete_palette.gif'))
        extra.append(extras.image('screenshot/test_edit_eye_shadow_add_palette.gif'))

    @pytest.mark.B
    @pytest.mark.YMK
    def test_edit_eyebrows_arch(self, extra):
        self.app.deeplink_to_eyebrows() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_3D_tab("ARCH") \
            .screenshot("test_edit_eyebrows_arch_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_eyebrows_arch_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_eyebrows_arch_after+100", 1) \
            .compare_photo("test_edit_eyebrows_arch_before", "test_edit_eyebrows_arch_after+100"
                           , "test_edit_eyebrows_arch_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eyebrows_arch") \
            .compose_gif("test_edit_eyebrows_arch", 'screenshot/test_edit_eyebrows_arch_before.png'
                         , 'screenshot/test_edit_eyebrows_arch_after-100.png'
                         , 'screenshot/test_edit_eyebrows_arch_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eyebrows_arch.jpg'))
        extra.append(extras.image('screenshot/test_edit_eyebrows_arch.gif'))

    @pytest.mark.B
    @pytest.mark.YMK
    def test_edit_eyebrows_thickness(self, extra):
        self.app.deeplink_to_eyebrows() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_3D_tab("THICKNESS") \
            .screenshot("test_edit_eyebrows_thickness_before", 1) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_eyebrows_thickness_after-100", 1) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_eyebrows_thickness_after+100", 1) \
            .compare_photo("test_edit_eyebrows_thickness_before", "test_edit_eyebrows_thickness_after+100"
                           , "test_edit_eyebrows_thickness_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eyebrows_thickness") \
            .compose_gif("test_edit_eyebrows_thickness", 'screenshot/test_edit_eyebrows_thickness_before.png'
                         , 'screenshot/test_edit_eyebrows_thickness_after-100.png'
                         , 'screenshot/test_edit_eyebrows_thickness_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eyebrows_thickness.jpg'))
        extra.append(extras.image('screenshot/test_edit_eyebrows_thickness.gif'))

    @pytest.mark.B
    @pytest.mark.YMK
    def test_edit_eyebrows_position_x(self, extra):
        self.app.deeplink_to_eyebrows() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_3D_tab("POSITION") \
            .screenshot("test_edit_eyebrows_position_x_before", 1) \
            .set_position_to_together() \
            .screenshot("test_edit_eyebrows_position_x_after-100", 1) \
            .set_position_to_apart() \
            .screenshot("test_edit_eyebrows_position_x_after+100", 1) \
            .compare_photo("test_edit_eyebrows_position_x_before", "test_edit_eyebrows_position_x_after+100"
                           , "test_edit_eyebrows_position_x_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eyebrows_position_x") \
            .compose_gif("test_edit_eyebrows_position_x", 'screenshot/test_edit_eyebrows_position_x_before.png'
                         , 'screenshot/test_edit_eyebrows_position_x_after-100.png'
                         , 'screenshot/test_edit_eyebrows_position_x_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eyebrows_position_x.jpg'))
        extra.append(extras.image('screenshot/test_edit_eyebrows_position_x.gif'))

    @pytest.mark.B
    @pytest.mark.YMK
    def test_edit_eyebrows_position_y(self, extra):
        self.app.deeplink_to_eyebrows() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_3D_tab("POSITION") \
            .screenshot("test_edit_eyebrows_position_y_before", 1) \
            .set_position_to_down() \
            .screenshot("test_edit_eyebrows_position_y_after-100", 1) \
            .set_position_to_up() \
            .screenshot("test_edit_eyebrows_position_y_after+100", 1) \
            .compare_photo("test_edit_eyebrows_position_y_before", "test_edit_eyebrows_position_y_after+100"
                           , "test_edit_eyebrows_position_y_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_eyebrows_position_y") \
            .compose_gif("test_edit_eyebrows_position_y", 'screenshot/test_edit_eyebrows_position_y_before.png'
                         , 'screenshot/test_edit_eyebrows_position_y_after-100.png'
                         , 'screenshot/test_edit_eyebrows_position_y_after+100.png', speed=2)
        extra.append(extras.image('savephoto/test_edit_eyebrows_position_y.jpg'))
        extra.append(extras.image('screenshot/test_edit_eyebrows_position_y.gif'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_eye_shadow_add_delete_palette()
    t.teardown_method()
