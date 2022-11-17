from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
import pytest
from pytest_html import extras

album_name1 = "1.Makeup"
album_name2 = "2.Redness"
album_name4 = "4.uneven_skintone"
album_name5 = "5.Wrinkle"

class Test(object):
    def setup_method(self):  # run before every test
        self.driver = App().set_auto() \
            .set_app("YMK") \
            .set_wait_time(5) \
            .set_newcommand_timeout(9999) \
            .create()
        self.app = YMKbase(self.driver)

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_smoother(self, extra):
        self.app.deeplink_to_skinsmoother()\
            .pick_photo(album_name1, 1)\
            .screenshot("test_edit_smoother_before", wait_time=3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_smoother_after", wait_time=3)\
            .click_save()\
            .pull_photo_from_device("1_test_edit_smoother_save") \
            .compose_gif("test_edit_smoother_compare_diff", "screenshot/test_edit_smoother_after.png",
                         "screenshot/test_edit_smoother_before.png", speed=2)
        extra.append(extras.image("savephoto/1_test_edit_smoother_save.jpg"))
        extra.append(extras.image("screenshot/test_edit_smoother_compare_diff.gif"))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_faceshaper_faceshape_overall(self, extra):
        self.app.deeplink_to_faceshape()\
            .pick_photo(album_name1, 1)\
            .screenshot("test_edit_faceshape_overall_before", wait_time=3)\
            .adjust_intensity_to_left()\
            .screenshot("test_edit_faceshape_overall_after_-100", wait_time=3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_faceshape_overall_after_100", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_faceshaper_faceshape_overall") \
            .compose_gif("test_edit_faceshape_overall_diff",
                         "screenshot/test_edit_faceshape_overall_before.png",
                         "screenshot/test_edit_faceshape_overall_after_-100.png",
                         "screenshot/test_edit_faceshape_overall_before.png",
                         "screenshot/test_edit_faceshape_overall_after_100.png",
                         speed=2)
        extra.append(extras.image("savephoto/1_test_edit_faceshaper_faceshape_overall.jpg"))
        extra.append(extras.image("screenshot/test_edit_faceshape_overall_diff.gif"))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_faceshaper_faceshape_left(self, extra):
        self.app.deeplink_to_faceshape()\
            .pick_photo(album_name1, 1)\
            .click_left()\
            .screenshot("test_edit_faceshape_left_before", wait_time=3)\
            .adjust_intensity_to_left()\
            .screenshot("test_edit_faceshape_left_after_-100", wait_time=3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_faceshape_left_after_100", wait_time=3)\
            .click_save()\
            .pull_photo_from_device("1_test_edit_faceshaper_faceshape_left") \
            .compose_gif("test_edit_faceshaper_faceshape_left_diff",
                         "screenshot/test_edit_faceshape_left_before.png",
                         "screenshot/test_edit_faceshape_left_after_-100.png",
                         "screenshot/test_edit_faceshape_left_before.png",
                         "screenshot/test_edit_faceshape_left_after_100.png",
                         speed=2)
        extra.append(extras.image("savephoto/1_test_edit_faceshaper_faceshape_left.jpg"))
        extra.append(extras.image("screenshot/test_edit_faceshaper_faceshape_left_diff.gif"))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_faceshaper_faceshape_right(self, extra):
        self.app.deeplink_to_faceshape()\
            .pick_photo(album_name1, 1)\
            .click_right()\
            .screenshot("test_edit_faceshape_right_before", wait_time=3)\
            .adjust_intensity_to_left()\
            .screenshot("test_edit_faceshape_right_after_-100", wait_time=3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_faceshape_right_after_100", wait_time=3)\
            .click_save()\
            .pull_photo_from_device("1_test_edit_faceshaper_faceshape_right") \
            .compose_gif("test_edit_faceshape_right_diff",
                         "screenshot/test_edit_faceshape_right_before.png",
                         "screenshot/test_edit_faceshape_right_after_-100.png",
                         "screenshot/test_edit_faceshape_right_before.png",
                         "screenshot/test_edit_faceshape_right_after_100.png",
                         speed=2)
        extra.append(extras.image("savephoto/1_test_edit_faceshaper_faceshape_right.jpg"))
        extra.append(extras.image("screenshot/test_edit_faceshape_right_diff.gif"))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_faceshaper_chinshape_overall(self, extra):
        self.app.deeplink_to_faceshape()\
            .pick_photo(album_name1, 1)\
            .select_faceshape_function("Chin Shape") \
            .screenshot("test_edit_chinshape_overall_before", wait_time=3) \
            .adjust_intensity_to_left()\
            .screenshot("test_edit_chinshape_overall_after_-100", wait_time=3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_chinshape_overall_after_100", wait_time=3)\
            .click_save()\
            .pull_photo_from_device("1_test_edit_faceshaper_chinshape_overall") \
            .compose_gif("test_edit_chinshape_overall_diff",
                         "screenshot/test_edit_chinshape_overall_before.png",
                         "screenshot/test_edit_chinshape_overall_after_-100.png",
                         "screenshot/test_edit_chinshape_overall_before.png",
                         "screenshot/test_edit_chinshape_overall_after_100.png",
                         speed=2)
        extra.append(extras.image("savephoto/1_test_edit_faceshaper_chinshape_overall.jpg"))
        extra.append(extras.image("screenshot/test_edit_chinshape_overall_diff.gif"))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_faceshaper_chinshape_left(self, extra):
        self.app.deeplink_to_faceshape() \
            .pick_photo(album_name1, 1)\
            .select_faceshape_function("Chin Shape") \
            .click_left() \
            .screenshot("test_edit_chinshape_left_before", wait_time=3) \
            .adjust_intensity_to_left()\
            .screenshot("test_edit_chinshape_left_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_chinshape_left_after_100", wait_time=3) \
            .click_save()\
            .pull_photo_from_device("1_test_edit_faceshaper_chinshape_left") \
            .compose_gif("test_edit_chinshape_left_diff",
                         "screenshot/test_edit_chinshape_left_before.png",
                         "screenshot/test_edit_chinshape_left_after_-100.png",
                         "screenshot/test_edit_chinshape_left_before.png",
                         "screenshot/test_edit_chinshape_left_after_100.png",
                         speed=2)
        extra.append(extras.image("savephoto/1_test_edit_faceshaper_chinshape_left.jpg"))
        extra.append(extras.image("screenshot/test_edit_chinshape_left_diff.gif"))

    @pytest.mark.B
    @pytest.mark.S2
    def test_edit_faceshaper_chinshape_right(self, extra):
        self.app.deeplink_to_faceshape() \
            .pick_photo(album_name1, 1)\
            .select_faceshape_function("Chin Shape") \
            .click_right() \
            .screenshot("test_edit_chinshape_right_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_chinshape_right_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_chinshape_right_after_100", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_faceshaper_chinshape_right") \
            .compose_gif("test_edit_chinshape_right_diff",
                         "screenshot/test_edit_chinshape_right_before.png",
                         "screenshot/test_edit_chinshape_right_after_-100.png",
                         "screenshot/test_edit_chinshape_right_before.png",
                         "screenshot/test_edit_chinshape_right_after_100.png",
                         speed=2)
        extra.append(extras.image("savephoto/1_test_edit_faceshaper_chinshape_right.jpg"))
        extra.append(extras.image("screenshot/test_edit_chinshape_right_diff.gif"))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_faceshaper_chinlength(self, extra):
        self.app.deeplink_to_faceshape() \
            .pick_photo(album_name1, 1)\
            .select_faceshape_function("Chin Length") \
            .screenshot("test_edit_chinlength_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_chinlength_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_chinlength_after_100", wait_time=3) \
            .click_save()\
            .pull_photo_from_device("1_test_edit_faceshaper_chinlength_100_save") \
            .compose_gif("test_edit_chinlength_diff",
                         "screenshot/test_edit_chinlength_before.png",
                         "screenshot/test_edit_chinlength_after_-100.png",
                         "screenshot/test_edit_chinlength_before.png",
                         "screenshot/test_edit_chinlength_after_100.png",
                         speed=2)
        extra.append(extras.image("savephoto/1_test_edit_faceshaper_chinlength_100_save.jpg"))
        extra.append(extras.image("screenshot/test_edit_chinlength_diff.gif"))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_faceshaper_width(self, extra):
        self.app.deeplink_to_faceshape() \
            .pick_photo(album_name1, 1)\
            .select_faceshape_function("Width") \
            .screenshot("test_edit_facewidth_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_facewidth_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_facewidth_after_100", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_faceshaper_facewidth_100_save") \
            .compose_gif("test_edit_facewidth_diff",
                         "screenshot/test_edit_facewidth_before.png",
                         "screenshot/test_edit_facewidth_after_-100.png",
                         "screenshot/test_edit_facewidth_before.png",
                         "screenshot/test_edit_facewidth_after_100.png",
                         speed=2)
        extra.append(extras.image("savephoto/1_test_edit_faceshaper_facewidth_100_save.jpg"))
        extra.append(extras.image("screenshot/test_edit_facewidth_diff.gif"))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_faceshaper_cheek(self, extra):
        self.app.deeplink_to_faceshape() \
            .pick_photo(album_name1, 1)\
            .select_faceshape_function("Cheek") \
            .screenshot("test_edit_facecheek_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_facecheek_after", wait_time=3) \
            .click_save()\
            .pull_photo_from_device("1_test_edit_faceshaper_facecheek_save") \
            .compose_gif("test_edit_facecheek_diff",
                         "screenshot/test_edit_facecheek_before.png",
                         "screenshot/test_edit_facecheek_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/1_test_edit_faceshaper_facecheek_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_facecheek_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_faceshaper_cheekbone(self, extra):
        self.app.deeplink_to_faceshape() \
            .pick_photo(album_name1, 1)\
            .select_faceshape_function("Cheekbone") \
            .screenshot("test_edit_facecheekbone_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_facecheekbone_after", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_faceshaper_facecheekbone_save") \
            .compose_gif("test_edit_facecheekbone_diff",
                         "screenshot/test_edit_facecheekbone_before.png",
                         "screenshot/test_edit_facecheekbone_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/1_test_edit_faceshaper_facecheekbone_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_facecheekbone_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_faceshaper_jaw(self, extra):
        self.app.deeplink_to_faceshape() \
            .pick_photo(album_name1, 1)\
            .select_faceshape_function("Jaw") \
            .screenshot("test_edit_facejaw_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_facejaw_after", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_faceshaper_facejaw_save") \
            .compose_gif("test_edit_facejaw_diff",
                         "screenshot/test_edit_facejaw_before.png",
                         "screenshot/test_edit_facejaw_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/1_test_edit_faceshaper_facejaw_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_facejaw_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_faceshaper_forehead(self, extra):
        self.app.deeplink_to_faceshape() \
            .pick_photo(album_name1, 1)\
            .select_faceshape_function("Forehead") \
            .screenshot("test_edit_forehead_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_forehead_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_forehead_after_100", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("1_test_edit_faceshaper_forehead_save") \
            .compose_gif("test_edit_forehead_diff",
                         "screenshot/test_edit_forehead_before.png",
                         "screenshot/test_edit_forehead_after_-100.png",
                         "screenshot/test_edit_forehead_before.png",
                         "screenshot/test_edit_forehead_after_100.png",
                         speed=2)
        extra.append(extras.image('savephoto/1_test_edit_faceshaper_forehead_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_forehead_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_nose_noseenhance(self, extra):
        self.app.deeplink_to_noseenhance()\
            .pick_photo(album_name4, 1)\
            .screenshot("test_edit_noseenhance_before", wait_time=3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_noseenhance_after", wait_time=3)\
            .click_save()\
            .pull_photo_from_device("4_test_edit_noseenhance_save") \
            .compose_gif("test_edit_noseenhance_diff",
                         "screenshot/test_edit_noseenhance_before.png",
                         "screenshot/test_edit_noseenhance_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/4_test_edit_noseenhance_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_noseenhance_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_nose_nosesize(self, extra):
        self.app.deeplink_to_noseenhance()\
            .pick_photo(album_name4, 1)\
            .select_noseenhance_function("Size") \
            .screenshot("test_edit_nosesize_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_nosesize_after_-100", wait_time=3)\
            .adjust_intensity_to_right() \
            .screenshot("test_edit_nosesize_after_100", wait_time=3) \
            .click_save()\
            .pull_photo_from_device("4_test_edit_nosesize_save") \
            .compose_gif("test_edit_nosesize_diff",
                         "screenshot/test_edit_nosesize_before.png",
                         "screenshot/test_edit_nosesize_after_-100.png",
                         "screenshot/test_edit_nosesize_before.png",
                         "screenshot/test_edit_nosesize_after_100.png",
                         speed=2)
        extra.append(extras.image('savephoto/4_test_edit_nosesize_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_nosesize_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_nose_noselift(self, extra):
        self.app.deeplink_to_noseenhance() \
            .pick_photo(album_name4, 1)\
            .select_noseenhance_function("Lift") \
            .screenshot("test_edit_noselift_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_noselift_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_noselift_after_100", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("4_test_edit_noselift_save") \
            .compose_gif("test_edit_noselift_diff",
                         "screenshot/test_edit_noselift_before.png",
                         "screenshot/test_edit_noselift_after_-100.png",
                         "screenshot/test_edit_noselift_before.png",
                         "screenshot/test_edit_noselift_after_100.png",
                         speed=2)
        extra.append(extras.image('savephoto/4_test_edit_noselift_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_noselift_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_nose_nosebridge(self, extra):
        self.app.deeplink_to_noseenhance() \
            .pick_photo(album_name4, 1)\
            .select_noseenhance_function("Bridge") \
            .screenshot("test_edit_nosebridge_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_nosebridge_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_nosebridge_after_100", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("4_test_edit_nosebridge_save") \
            .compose_gif("test_edit_nosebridge_diff",
                         "screenshot/test_edit_nosebridge_before.png",
                         "screenshot/test_edit_nosebridge_after_-100.png",
                         "screenshot/test_edit_nosebridge_before.png",
                         "screenshot/test_edit_nosebridge_after_100.png",
                         speed=2)
        extra.append(extras.image('savephoto/4_test_edit_nosebridge_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_nosebridge_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_nose_nosetip(self, extra):
        self.app.deeplink_to_noseenhance() \
            .pick_photo(album_name4, 1)\
            .select_noseenhance_function("Tip") \
            .screenshot("test_edit_nosetip_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_nosetip_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_nosetip_after_100", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("4_test_edit_nosetip_save") \
            .compose_gif("test_edit_nosetip_diff",
                         "screenshot/test_edit_nosetip_before.png",
                         "screenshot/test_edit_nosetip_after_-100.png",
                         "screenshot/test_edit_nosetip_before.png",
                         "screenshot/test_edit_nosetip_after_100.png",
                         speed=2)
        extra.append(extras.image('savephoto/4_test_edit_nosetip_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_nosetip_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_nose_nosewing(self, extra):
        self.app.deeplink_to_noseenhance() \
            .pick_photo(album_name4, 1)\
            .select_noseenhance_function("Wing") \
            .screenshot("test_edit_nosewing_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_nosewing_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_nosewing_after_100", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("4_test_edit_nosewing_save") \
            .compose_gif("test_edit_nosewing_diff",
                         "screenshot/test_edit_nosewing_before.png",
                         "screenshot/test_edit_nosewing_after_-100.png",
                         "screenshot/test_edit_nosewing_before.png",
                         "screenshot/test_edit_nosewing_after_100.png",
                         speed=2)
        extra.append(extras.image('savephoto/4_test_edit_nosewing_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_nosewing_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_nose_nosewidth(self, extra):
        self.app.deeplink_to_noseenhance() \
            .pick_photo(album_name4, 1)\
            .select_noseenhance_function("Width") \
            .screenshot("test_edit_nosewidth_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_nosewidth_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_nosewidth_after_100", wait_time=3) \
            .click_save() \
            .pull_photo_from_device("4_test_edit_nosewidth_save") \
            .compose_gif("test_edit_nosewidth_diff",
                         "screenshot/test_edit_nosewidth_before.png",
                         "screenshot/test_edit_nosewidth_after_-100.png",
                         "screenshot/test_edit_nosewidth_before.png",
                         "screenshot/test_edit_nosewidth_after_100.png",
                         speed=2)
        extra.append(extras.image('savephoto/4_test_edit_nosewidth_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_nosewidth_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_wrinkle(self, extra):
        self.app.deeplink_to_wrinkle()\
            .pick_photo(album_name5, 1)\
            .wait_face_animation()\
            .adjust_intensity_to_left()\
            .screenshot("test_edit_wrinkle_before", wait_time=5)\
            .adjust_intensity_to_right() \
            .screenshot("test_edit_wrinkle_after", wait_time=3) \
            .compare_photo("test_edit_wrinkle_before", "test_edit_wrinkle_after", "test_edit_wrinkle_diff") \
            .click_save()\
            .pull_photo_from_device("5_test_edit_wrinkle_save") \
            .compose_gif("test_edit_wrinkle",
                         "screenshot/test_edit_wrinkle_before.png",
                         "screenshot/test_edit_wrinkle_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/5_test_edit_wrinkle_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_wrinkle_diff.png'))
        extra.append(extras.image('screenshot/test_edit_wrinkle.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_redness(self, extra):
        self.app.deeplink_to_redness()\
            .pick_photo(album_name2, 1)\
            .wait_animation()\
            .adjust_intensity_to_left()\
            .screenshot("test_edit_redness_before", wait_time=5)\
            .adjust_intensity_to_right() \
            .screenshot("test_edit_redness_after", wait_time=3) \
            .click_save(timeout=10) \
            .pull_photo_from_device("2_test_edit_redness_save") \
            .compose_gif("test_edit_redness_diff",
                         "screenshot/test_edit_redness_before.png",
                         "screenshot/test_edit_redness_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/2_test_edit_redness_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_redness_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_uneven_skintone(self, extra):
        self.app.deeplink_to_unevenskintone()\
            .pick_photo(album_name2, 1) \
            .wait_animation() \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_uneven_skintone_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_uneven_skintone_after", wait_time=3) \
            .compare_photo("test_edit_uneven_skintone_before", "test_edit_uneven_skintone_after",
                           "test_edit_uneven_skintone_diff", threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("2_test_edit_uneven_skintone_save") \
            .compose_gif("test_edit_uneven_skintone",
                         "screenshot/test_edit_uneven_skintone_before.png",
                         "screenshot/test_edit_uneven_skintone_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/2_test_edit_uneven_skintone_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_uneven_skintone_diff.png'))
        extra.append(extras.image('screenshot/test_edit_uneven_skintone.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_pores(self, extra):
        self.app.deeplink_to_pores()\
            .pick_photo(album_name4, 1)\
            .wait_animation() \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_pores_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_pores_after", wait_time=3) \
            .compare_photo("test_edit_pores_before", "test_edit_pores_after",
                           "test_edit_pores_diff") \
            .click_save() \
            .pull_photo_from_device("4_test_edit_pores_save") \
            .compose_gif("test_edit_pores",
                         "screenshot/test_edit_pores_before.png",
                         "screenshot/test_edit_pores_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/4_test_edit_pores_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_pores_diff.png'))
        extra.append(extras.image('screenshot/test_edit_pores.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_foundation(self, extra):
        self.app.deeplink_to_foundation()\
            .pick_photo(album_name1, 1)\
            .screenshot("test_edit_foundation_before", wait_time=2) \
            .select_brand("PERFECT")\
            .select_color(1)\
            .adjust_intensity_to_top()\
            .screenshot("test_edit_foundation_after", wait_time=2) \
            .click_save()\
            .pull_photo_from_device("1_test_edit_foundation_save") \
            .compose_gif("test_edit_foundation_diff",
                         "screenshot/test_edit_foundation_before.png",
                         "screenshot/test_edit_foundation_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/1_test_edit_foundation_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_foundation_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_concealer(self, extra):
        self.app.deeplink_to_concealer()\
            .pick_photo(album_name2, 1)\
            .wait_animation()\
            .adjust_intensity_to_left()\
            .screenshot("test_edit_concealer_before", wait_time=2)\
            .adjust_intensity_to_right() \
            .screenshot("test_edit_concealer_after", wait_time=2)\
            .compare_photo("test_edit_concealer_before", "test_edit_concealer_after", "test_edit_concealer_diff",
                           threshold=0.05)\
            .click_save()\
            .pull_photo_from_device("2_test_edit_concealer_save") \
            .compose_gif("test_edit_concealer",
                         "screenshot/test_edit_concealer_before.png",
                         "screenshot/test_edit_concealer_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/2_test_edit_concealer_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_concealer_diff.png'))
        extra.append(extras.image('screenshot/test_edit_concealer.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_blush(self, extra):
        self.app.deeplink_to_blush()\
            .pick_photo(album_name1, 1)\
            .select_brand("PERFECT")\
            .screenshot("test_edit_blush_before", wait_time=2) \
            .select_color(5) \
            .adjust_intensity_to_top() \
            .screenshot("test_edit_blush_after", wait_time=2) \
            .click_save()\
            .pull_photo_from_device("1_test_edit_blush_save") \
            .compose_gif("test_edit_blush_diff",
                         "screenshot/test_edit_blush_before.png",
                         "screenshot/test_edit_blush_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/1_test_edit_blush_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_blush_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_contour(self, extra):
        self.app.deeplink_to_contour()\
            .pick_photo(album_name1, 1) \
            .select_brand("PERFECT") \
            .screenshot("test_edit_contour_before", wait_time=2)\
            .select_pattern(2)\
            .adjust_intensity_to_top()\
            .screenshot("test_edit_contour_after", wait_time=5)\
            .click_save()\
            .pull_photo_from_device("1_test_edit_contour_save") \
            .compose_gif("test_edit_contour_diff",
                         "screenshot/test_edit_contour_before.png",
                         "screenshot/test_edit_contour_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/1_test_edit_contour_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_contour_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_highlight(self, extra):
        self.app.deeplink_to_highlight()\
            .pick_photo(album_name1, 1)\
            .select_brand("PERFECT")\
            .screenshot("test_edit_highlight_before", wait_time=2)\
            .select_pattern(2)\
            .adjust_intensity_to_top()\
            .screenshot("test_edit_highlight_after", wait_time=5)\
            .click_save()\
            .pull_photo_from_device("1_test_edit_highlight_save") \
            .compose_gif("test_edit_highlight_diff",
                         "screenshot/test_edit_highlight_before.png",
                         "screenshot/test_edit_highlight_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/1_test_edit_highlight_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_highlight_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_facepaint(self, extra):
        self.app.deeplink_to_facepaint() \
            .pick_photo(album_name1, 1)\
            .screenshot("test_edit_facepaint_before", wait_time=2) \
            .select_pattern(2) \
            .screenshot("test_edit_facepaint_after", wait_time=2) \
            .click_save()\
            .pull_photo_from_device("1_test_edit_facepaint_save") \
            .compose_gif("test_edit_facepaint_diff",
                         "screenshot/test_edit_facepaint_before.png",
                         "screenshot/test_edit_facepaint_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/1_test_edit_facepaint_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_facepaint_diff.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_blemish(self, extra):
        self.app.deeplink_to_blemish()\
            .pick_photo(album_name2, 1)\
            .screenshot("test_edit_blemish_before", wait_time=3) \
            .switch_onoff()\
            .screenshot("test_edit_blemish_after", wait_time=3) \
            .compare_photo("test_edit_blemish_before", "test_edit_blemish_after",
                           "test_edit_blemish_diff")\
            .click_save() \
            .pull_photo_from_device("2_test_edit_blemish_save") \
            .compose_gif("test_edit_blemish",
                         "screenshot/test_edit_blemish_before.png",
                         "screenshot/test_edit_blemish_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/2_test_edit_blemish_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_blemish_diff.png'))
        extra.append(extras.image('screenshot/test_edit_blemish.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_edit_shinremoval(self, extra):
        self.app.deeplink_to_shineremoval()\
            .pick_photo(album_name4, 1)\
            .screenshot("test_edit_shinremoval_before", wait_time=3) \
            .adjust_intensity_to_right()\
            .screenshot("test_edit_shinremoval_after", wait_time=3) \
            .compare_photo("test_edit_shinremoval_before", "test_edit_shinremoval_after",
                           "test_edit_shinremoval_diff", threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("4_test_edit_shinremoval_save") \
            .compose_gif("test_edit_shinremoval",
                         "screenshot/test_edit_shinremoval_before.png",
                         "screenshot/test_edit_shinremoval_after.png",
                         speed=2)
        extra.append(extras.image('savephoto/4_test_edit_shinremoval_save.jpg'))
        extra.append(extras.image('screenshot/test_edit_shinremoval_diff.png'))
        extra.append(extras.image('screenshot/test_edit_shinremoval.gif'))

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


"""if __name__ == '__main__':
    #pytest.main(['--html=face_result.html', '--disable-warnings', './tests/YMK/', '-rA', '-m=Faces'])
    t = Test()
    t.setup_method()
    t.test_edit_wrinkle()
    t.teardown_method()"""
    
