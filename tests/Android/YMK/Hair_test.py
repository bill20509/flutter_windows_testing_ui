import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
from pytest_html import extras
import time

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

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_hairdye_multi(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .screenshot("test_edit_hairdye_multi_before", wait_time=3) \
            .select_color(1) \
            .screenshot("test_edit_hairdye_multi_after", wait_time=3) \
            .compare_photo("test_edit_hairdye_multi_before", "test_edit_hairdye_multi_after",
                           "test_edit_hairdye_multi_diff", threshold=0.1) \
            .click_save() \
            .message("Default Intensity= 50") \
            .pull_photo_from_device("1_test_edit_hairdye_multi_save")
        extra.append(extras.image('screenshot/test_edit_hairdye_multi_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_multi_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_hairdye_2colors(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("2 COLORS") \
            .screenshot("test_edit_hairdye_2colors_before", wait_time=3) \
            .select_color(3) \
            .screenshot("test_edit_hairdye_2colors_after", wait_time=3) \
            .compare_photo("test_edit_hairdye_2colors_before", "test_edit_hairdye_2colors_after",
                           "test_edit_hairdye_2colors_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_2colors_save")
        extra.append(extras.image('screenshot/test_edit_hairdye_2colors_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_2colors_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_hairdye_ombre(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("OMBRE") \
            .screenshot("test_edit_hairdye_ombre_before", wait_time=3) \
            .select_color(3) \
            .screenshot("test_edit_hairdye_ombre_after", wait_time=3) \
            .compare_photo("test_edit_hairdye_ombre_before", "test_edit_hairdye_ombre_after",
                           "test_edit_hairdye_ombre_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_ombre_save")
        extra.append(extras.image('screenshot/test_edit_hairdye_ombre_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_ombre_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_hairdye_1color_a(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("1 COLOR") \
            .screenshot("test_edit_hairdye_1color_a_before", wait_time=3) \
            .select_color(3) \
            .screenshot("test_edit_hairdye_1color_a_after", wait_time=3) \
            .compare_photo("test_edit_hairdye_1color_a_before", "test_edit_hairdye_1color_a_after",
                           "test_edit_hairdye_1color_a_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_1color_save")
        extra.append(extras.image('screenshot/test_edit_hairdye_1color_a_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_1color_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_hairdye_multi_intensity(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_color(1) \
            .screenshot("test_edit_hairdye_multi_intensity_before", wait_time=3) \
            .adjust_intensity_to_down() \
            .screenshot("test_edit_hairdye_multi_intensity_0", wait_time=3) \
            .adjust_intensity_to_top() \
            .screenshot("test_edit_hairdye_multi_intensity_100", wait_time=3) \
            .click_save() \
            .message("Export Intensity=100") \
            .pull_photo_from_device("1_test_edit_hairdye_multi_intensity_100_save") \
            .compose_gif("test_edit_hairdye_multi_intensity_compare",
                         "screenshot/test_edit_hairdye_multi_intensity_before.png",
                         "screenshot/test_edit_hairdye_multi_intensity_0.png",
                         "screenshot/test_edit_hairdye_multi_intensity_100.png", speed=2)
        extra.append(extras.image('screenshot/test_edit_hairdye_multi_intensity_compare.gif'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_multi_intensity_100_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_hairdye_2colors_blend(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("2 COLORS") \
            .select_color(3) \
            .screenshot("test_edit_hairdye_2colors_blend_before", wait_time=3) \
            .set_blend_to_100() \
            .screenshot("test_edit_hairdye_2colors_blend_100", wait_time=3) \
            .set_blend_to_0() \
            .screenshot("test_edit_hairdye_2colors_blend_0", wait_time=3) \
            .compare_photo("test_edit_hairdye_2colors_blend_100", "test_edit_hairdye_2colors_blend_0",
                           "test_edit_hairdye_2colors_blend_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_2colors_blend_save")
        extra.append(extras.image('screenshot/test_edit_hairdye_2colors_blend_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_2colors_blend_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_hairdye_2colors_coverage(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("2 COLORS") \
            .select_color(3) \
            .set_blend_to_0() \
            .message("Blend = 0") \
            .screenshot("test_edit_hairdye_2colors_coverage_before", wait_time=3) \
            .set_coverage_to_100() \
            .message("Coverage set to 100!") \
            .screenshot("test_edit_hairdye_2colors_coverage_100", wait_time=3) \
            .set_coverage_to_0() \
            .message("Coverage set to 0!") \
            .screenshot("test_edit_hairdye_2colors_coverage_0", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_2colors_coverage_save") \
            .message("Hairdye coverage of saved photo = 0") \
            .compose_gif("test_edit_hairdye_2colors_coverage_compare",
                         "screenshot/test_edit_hairdye_2colors_coverage_100.png",
                         "screenshot/test_edit_hairdye_2colors_coverage_before.png",
                         "screenshot/test_edit_hairdye_2colors_coverage_0.png", speed=2)
        extra.append(extras.image('screenshot/test_edit_hairdye_2colors_coverage_compare.gif'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_2colors_coverage_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_hairdye_ombre_blend(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("OMBRE") \
            .select_color(3) \
            .screenshot("test_edit_hairdye_ombre_blend_before", wait_time=3) \
            .set_blend_to_100() \
            .screenshot("test_edit_hairdye_ombre_blend_100", wait_time=3) \
            .set_blend_to_0() \
            .screenshot("test_edit_hairdye_ombre_blend_0", wait_time=3) \
            .compare_photo("test_edit_hairdye_ombre_blend_100", "test_edit_hairdye_ombre_blend_0",
                           "test_edit_hairdye_ombre_blend_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_ombre_blend_save")
        extra.append(extras.image('screenshot/test_edit_hairdye_ombre_blend_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_ombre_blend_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_hairdye_ombre_coverage(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("OMBRE") \
            .select_color(3) \
            .set_blend_to_0() \
            .message("Blend = 0") \
            .screenshot("test_edit_hairdye_ombre_coverage_before", wait_time=3) \
            .set_coverage_to_100() \
            .message("Coverage set to 100!") \
            .screenshot("test_edit_hairdye_ombre_coverage_100", wait_time=3) \
            .set_coverage_to_0() \
            .message("Coverage set to 0!") \
            .screenshot("test_edit_hairdye_ombre_coverage_0", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_ombre_coverage_save") \
            .message("Hairdye coverage of saved photo = 0") \
            .compose_gif("test_edit_hairdye_ombre_coverage_compare",
                         "screenshot/test_edit_hairdye_ombre_coverage_100.png",
                         "screenshot/test_edit_hairdye_ombre_coverage_before.png",
                         "screenshot/test_edit_hairdye_ombre_coverage_0.png", speed=2)
        extra.append(extras.image('screenshot/test_edit_hairdye_ombre_coverage_compare.gif'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_ombre_coverage_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_hairdye_1color_intensity_color(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("1 COLOR") \
            .select_color(3) \
            .screenshot("test_edit_hairdye_1color_intensity_color_before", wait_time=3) \
            .set_color_to_0() \
            .screenshot("test_edit_hairdye_1color_intensity_color_0", wait_time=3) \
            .set_color_to_100() \
            .screenshot("test_edit_hairdye_1color_intensity_color_100", wait_time=3) \
            .compare_photo("test_edit_hairdye_1color_intensity_color_0", "test_edit_hairdye_1color_intensity_color_100",
                           "test_edit_hairdye_1color_intensity_color_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_1color_color_save")
        extra.append(extras.image('screenshot/test_edit_hairdye_1color_intensity_color_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_1color_color_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_hairdye_1color_intensity_shine(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("1 COLOR") \
            .select_color(3) \
            .set_color_to_100() \
            .screenshot("test_edit_hairdye_1color_intensity_shine_before", wait_time=3) \
            .set_shine_to_0() \
            .screenshot("test_edit_hairdye_1color_intensity_shine_0", wait_time=3) \
            .set_shine_to_100() \
            .screenshot("test_edit_hairdye_1color_intensity_shine_100", wait_time=3) \
            .compare_photo("test_edit_hairdye_1color_intensity_shine_0", "test_edit_hairdye_1color_intensity_shine_100",
                           "test_edit_hairdye_1color_intensity_shine_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_1color_shine_save")
        extra.append(extras.image('screenshot/test_edit_hairdye_1color_intensity_shine_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_1color_shine_save.jpg'))

    """@pytest.mark.hair
    def test_edit_hairdye_2colors_edit(self):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("2 COLORS") \
            .select_color(3) \
            .screenshot("test_edit_hairdye_2colors_edit_before", wait_time=3) \
            .select_color(3) \
            .select_color_palette1() \
            .select_color_ball(6) \
            .screenshot("test_edit_hairdye_2colors_edit_after", wait_time=3) \
            .compare_photo("test_edit_hairdye_2colors_edit_before", "test_edit_hairdye_2colors_edit_after",
                           "test_edit_hairdye_2colors_edit_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_2colors_edit_save")"""

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_hairdye_finetune(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("1 COLOR") \
            .select_color(3) \
            .set_shine_to_100() \
            .set_color_to_100() \
            .screenshot("test_edit_hairdye_finetune_before", wait_time=3) \
            .click_finetune() \
            .select_brush() \
            .click_brush_size5() \
            .tap_central() \
            .screenshot("test_edit_hairdye_finetune_brush5", wait_time=3) \
            .select_eraser() \
            .click_brush_size4() \
            .tap_central() \
            .screenshot("test_edit_hairdye_finetune_brush5_eraser4", wait_time=3) \
            .compare_photo("test_edit_hairdye_finetune_brush5", "test_edit_hairdye_finetune_brush5_eraser4",
                           "test_edit_hairdye_finetune_brush5_eraser4_diff", threshold=0.1) \
            .click_finetune_apply() \
            .screenshot("test_edit_hairdye_finetune_after", wait_time=3) \
            .compare_photo("test_edit_hairdye_finetune_before", "test_edit_hairdye_finetune_after",
                           "test_edit_hairdye_finetune_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_finetune_save")
        extra.append(extras.image('screenshot/test_edit_hairdye_finetune_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_finetune_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_hairdye_flip(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .select_haircolor_tab("2 COLORS") \
            .select_color(3) \
            .set_blend_to_0() \
            .screenshot("test_edit_hairdye_flip_before", wait_time=3) \
            .click_flip_button() \
            .screenshot("test_edit_hairdye_flip_after", wait_time=3) \
            .compare_photo("test_edit_hairdye_flip_before", "test_edit_hairdye_flip_after",
                           "test_edit_hairdye_flip_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_flip_save")
        extra.append(extras.image('screenshot/test_edit_hairdye_flip_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_flip_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_hairdye_download(self, extra):
        self.app.deeplink_to_hairdye() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_brand("PERFECT") \
            .screenshot("test_edit_hairdye_download_before", wait_time=5) \
            .select_color(4) \
            .screenshot("test_edit_hairdye_download_after", wait_time=5) \
            .compare_photo("test_edit_hairdye_download_before", "test_edit_hairdye_download_after",
                           "test_edit_hairdye_download_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_hairdye_download_save")
        extra.append(extras.image('screenshot/test_edit_hairdye_download_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_hairdye_download_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_wig_download_fullcolor(self, extra):
        self.app.deeplink_to_hairstyle() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .screenshot("test_edit_wig_download_fullcolor_before", wait_time=5) \
            .select_style("Beach Wave") \
            .screenshot("test_edit_wig_download_fullcolor_after", wait_time=10) \
            .compare_photo("test_edit_wig_download_fullcolor_before", "test_edit_wig_download_fullcolor_after",
                           "test_edit_wig_download_fullcolor_diff", threshold=0.2) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_wig_download_fullcolor_save")
        extra.append(extras.image('screenshot/test_edit_wig_download_fullcolor_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_wig_download_fullcolor_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_wig_a(self, extra):
        self.app.deeplink_to_hairstyle() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .screenshot("test_edit_wig_a_before", wait_time=3) \
            .select_style("Wispy") \
            .screenshot("test_edit_wig_a_after", wait_time=3) \
            .compare_photo("test_edit_wig_a_before", "test_edit_wig_a_after", "test_edit_wig_a_diff", threshold=0) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_wig_a_save")
        extra.append(extras.image('screenshot/test_edit_wig_a_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_wig_a_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_wig_intensity(self, extra):
        self.app.deeplink_to_hairstyle() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_style("Pageboy") \
            .screenshot("test_edit_wig_intensity_before", wait_time=3) \
            .adjust_intensity_to_down() \
            .screenshot("test_edit_wig_intensity_0", wait_time=3) \
            .adjust_intensity_to_top() \
            .screenshot("test_edit_wig_intensity_100", wait_time=3) \
            .compare_photo("test_edit_wig_intensity_0", "test_edit_wig_intensity_100",
                           "test_edit_wig_intensity_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_wig_intensity_save")
        extra.append(extras.image('screenshot/test_edit_wig_intensity_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_wig_intensity_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_wig_color(self, extra):
        self.app.deeplink_to_hairstyle() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_style("Pageboy") \
            .click_color_tab() \
            .screenshot("test_edit_wig_color_before", wait_time=3) \
            .select_color(5) \
            .screenshot("test_edit_wig_color_after", wait_time=3) \
            .compare_photo("test_edit_wig_color_before", "test_edit_wig_color_after",
                           "test_edit_wig_color_diff", threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_wig_color_save")
        extra.append(extras.image('screenshot/test_edit_wig_color_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_wig_color_save.jpg'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_wig_store(self, extra):
        self.app.deeplink_to_hairstyle() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .screenshot("test_edit_wig_store_before", wait_time=3) \
            .click_store() \
            .select_female_new_download_wig(3, downloadtimeout=15) \
            .select_female_new_use_wig(3) \
            .screenshot("test_edit_wig_store_after", wait_time=3) \
            .compare_photo("test_edit_wig_store_before", "test_edit_wig_store_after", "test_edit_wig_store_diff",
                           threshold=0.1) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_wig_store_save")
        extra.append(extras.image('screenshot/test_edit_wig_store_diff.png'))
        extra.append(extras.image('savephoto/1_test_edit_wig_store_save.jpg'))

        """@pytest.mark.hair
        def test_edit_wig_store_delete(self, extra):
            self.app.deeplink_to_hairstyle() \
                .pick_photo(folder_name, 1) \
                .waiting_cursor() \
                .click_store() \
                .select_female_new_download_wig(2, downloadtimeout=15) \
                .select_female_new_use_wig(2) \
                .screenshot("test_edit_wig_store_delete_before", wait_time=3) \
                .compare_photo("test_edit_wig_store_before", "test_edit_wig_store_after", "test_edit_wig_store_diff",
                               threshold=0.1) \
                .click_save() \
                .pull_photo_from_device("1_test_edit_wig_save")"""

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
