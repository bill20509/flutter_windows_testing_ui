from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
import pytest

class TestFace(object):
    def setup_method(self):  # run before every test
        self.driver = App().set_udid("98061FFBA0020R")\
            .set_platform("Android")\
            .set_version("11")\
            .set_app("YMK")\
            .create()

        self.app = YMKbase(self.driver)

    @pytest.mark.Faces
    def test_edit_smoother(self):
        self.app.deeplink_to_skinsmoother()\
        .pick_photo("YMK_test_photos",1)\
        .screenshot("test_edit_smoother_before", wait_time=3)\
        .adjust_intensity_to_right()\
        .screenshot("test_edit_smoother_after", wait_time=3)\
        .compare_photo("test_edit_smoother_before", "test_edit_smoother_after","test_edit_smoother_diff")\
        .click_save()\
        .pull_photo_from_device("test_edit_smoother_save")

    @pytest.mark.Faces
    def test_edit_faceshaper_faceshape_overall(self):
        self.app.deeplink_to_faceshape()\
        .pick_photo("YMK_test_photos",1)\
        .screenshot("test_edit_faceshape_overall_before", wait_time=3)\
        .adjust_intensity_to_left()\
        .screenshot("test_edit_faceshape_overall_after_-100", wait_time=3)\
        .adjust_intensity_to_right()\
        .screenshot("test_edit_faceshape_overall_after_100", wait_time=3)\
        .compare_photo("test_edit_faceshape_overall_before", "test_edit_faceshape_overall_after_-100", "test_edit_faceshape_overall_diff_-100", threshold=0.05)\
        .compare_photo("test_edit_faceshape_overall_before", "test_edit_faceshape_overall_after_100", "test_edit_faceshape_overall_diff_100", threshold=0.05)\
        .click_save()\
        .pull_photo_from_device("test_edit_faceshape_overall")

    @pytest.mark.Faces
    def test_edit_faceshaper_faceshape_left(self):
        self.app.deeplink_to_faceshape()\
        .pick_photo("YMK_test_photos",1)\
        .click_left()\
        .screenshot("test_edit_faceshape_left_before", wait_time=3)\
        .adjust_intensity_to_left()\
        .screenshot("test_edit_faceshape_left_after_-100", wait_time=3)\
        .adjust_intensity_to_right()\
        .screenshot("test_edit_faceshape_left_after_100", wait_time=3)\
        .compare_photo("test_edit_faceshape_left_before", "test_edit_faceshape_left_after_-100", "test_edit_faceshape_left_diff_-100", threshold=0.05)\
        .compare_photo("test_edit_faceshape_left_before", "test_edit_faceshape_left_after_100", "test_edit_faceshape_left_diff_100", threshold=0.05)\
        .click_save()\
        .pull_photo_from_device("test_edit_faceshape_left")

    @pytest.mark.Faces
    def test_edit_faceshaper_faceshape_right(self):
        self.app.deeplink_to_faceshape()\
        .pick_photo("YMK_test_photos",1)\
        .click_right()\
        .screenshot("test_edit_faceshape_right_before", wait_time=3)\
        .adjust_intensity_to_left()\
        .screenshot("test_edit_faceshape_right_after_-100", wait_time=3)\
        .adjust_intensity_to_right()\
        .screenshot("test_edit_faceshape_right_after_100", wait_time=3)\
        .compare_photo("test_edit_faceshape_right_before", "test_edit_faceshape_right_after_-100", "test_edit_faceshape_right_diff_-100", threshold=0.05)\
        .compare_photo("test_edit_faceshape_right_before", "test_edit_faceshape_right_after_100", "test_edit_faceshape_right_diff_100", threshold=0.05)\
        .click_save()\
        .pull_photo_from_device("test_edit_faceshape_right")


    @pytest.mark.Faces
    def test_edit_faceshaper_chinshape_overall(self):
        self.app.deeplink_to_faceshape()\
            .pick_photo("YMK_test_photos", 1)\
            .select_faceshape_function("Chin Shape") \
            .screenshot("test_edit_chinshape_overall_before", wait_time=3) \
            .adjust_intensity_to_left()\
            .screenshot("test_edit_chinshape_overall_after_-100", wait_time=3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_chinshape_overall_after_100", wait_time=3)\
            .compare_photo("test_edit_chinshape_overall_before", "test_edit_chinshape_overall_after_-100",
                           "test_edit_chinshape_overall_diff_-100", threshold=0.05)\
            .compare_photo("test_edit_chinshape_overall_before", "test_edit_chinshape_overall_after_100",
                           "test_edit_chinshape_overall_diff_100", threshold=0.05)\
            .click_save()\
            .pull_photo_from_device("test_edit_chinshape_overall")

    @pytest.mark.Faces
    def test_edit_faceshaper_chinshape_left(self):
        self.app.deeplink_to_faceshape() \
            .pick_photo("YMK_test_photos", 2) \
            .select_faceshape_function("Chin Shape") \
            .click_left() \
            .screenshot("test_edit_chinshape_left_before", wait_time=3) \
            .adjust_intensity_to_left()\
            .screenshot("test_edit_chinshape_left_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_chinshape_left_after_100", wait_time=3) \
            .compare_photo("test_edit_chinshape_left_before", "test_edit_chinshape_left_after_-100",
                           "test_edit_chinshape_left_diff_-100", threshold=0.05) \
            .compare_photo("test_edit_chinshape_left_before", "test_edit_chinshape_left_after_100",
                           "test_edit_chinshape_left_diff_100", threshold=0.05) \
            .click_save()\
            .pull_photo_from_device("test_edit_chinshape_left")

    @pytest.mark.Faces
    def test_edit_faceshaper_chinshape_right(self):
        self.app.deeplink_to_faceshape() \
            .pick_photo("YMK_test_photos", 2) \
            .select_faceshape_function("Chin Shape") \
            .click_right() \
            .screenshot("test_edit_chinshape_right_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_chinshape_right_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_chinshape_right_after_100", wait_time=3) \
            .compare_photo("test_edit_chinshape_right_before", "test_edit_chinshape_right_after_-100",
                           "test_edit_chinshape_right_diff_-100", threshold=0.05) \
            .compare_photo("test_edit_chinshape_right_before", "test_edit_chinshape_right_after_100",
                           "test_edit_chinshape_right_diff_100", threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("test_edit_chinshape_right")

    @pytest.mark.Faces
    def test_edit_faceshaper_chinlength(self):
        self.app.deeplink_to_faceshape() \
            .pick_photo("YMK_test_photos", 1) \
            .select_faceshape_function("Chin Length") \
            .screenshot("test_edit_chinlength_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_chinlength_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_chinlength_after_100", wait_time=3) \
            .compare_photo("test_edit_chinlength_before", "test_edit_chinlength_after_-100",
                           "test_edit_chinlength_right_diff_-100", threshold=0.05) \
            .compare_photo("test_edit_chinlength_before", "test_edit_chinlength_after_100",
                           "test_edit_chinlength_left_diff_100", threshold=0.05) \
            .click_save()\
            .pull_photo_from_device("test_edit_chinlength_100_save")

    @pytest.mark.Faces
    def test_edit_faceshaper_width(self):
        self.app.deeplink_to_faceshape() \
            .pick_photo("YMK_test_photos", 1) \
            .select_faceshape_function("Width") \
            .screenshot("test_edit_facewidth_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_facewidth_after_-100", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_facewidth_after_100", wait_time=3) \
            .compare_photo("test_edit_facewidth_before", "test_edit_facewidth_after_-100",
                           "test_edit_facewidth_-100_diff", threshold=0.05) \
            .compare_photo("test_edit_facewidth_before", "test_edit_facewidth_after_100",
                           "test_edit_facewidth_100_diff", threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("test_edit_facewidth_100_save")

    @pytest.mark.Faces
    def test_edit_faceshaper_cheek(self):
        self.app.deeplink_to_faceshape() \
            .pick_photo("YMK_test_photos", 1) \
            .select_faceshape_function("Cheek") \
            .screenshot("test_edit_facecheek_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_facecheek_after", wait_time=3) \
            .compare_photo("test_edit_facecheek_before", "test_edit_facecheek_after",
                           "test_edit_facecheek_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_facecheek_save")

    @pytest.mark.Faces
    def test_edit_faceshaper_cheekbone(self):
        self.app.deeplink_to_faceshape() \
            .pick_photo("YMK_test_photos", 1) \
            .select_faceshape_function("Cheekbone") \
            .screenshot("test_edit_facecheekbone_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_facecheekbone_after", wait_time=3) \
            .compare_photo("test_edit_facecheekbone_before", "test_edit_facecheekbone_after",
                           "test_edit_facecheekbone_diff", threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("test_edit_facecheekbone_save")

    @pytest.mark.Faces
    def test_edit_faceshaper_jaw(self):
        self.app.deeplink_to_faceshape() \
            .pick_photo("YMK_test_photos", 1) \
            .select_faceshape_function("Jaw") \
            .screenshot("test_edit_facejaw_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_facejaw_after", wait_time=3) \
            .compare_photo("test_edit_facejaw_before", "test_edit_facejaw_after",
                           "test_edit_facejaw_diff", threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("test_edit_facejaw_save")

    @pytest.mark.Faces
    def test_edit_faceshaper_forehead(self):
        self.app.deeplink_to_faceshape() \
            .pick_photo("YMK_test_photos", 1) \
            .select_faceshape_function("Forehead") \
            .screenshot("test_edit_forehead_before", wait_time=3) \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_forehead_after_-100", wait_time=3) \
            .compare_photo("test_edit_forehead_before", "test_edit_forehead_after_-100",
                           "test_edit_forehead_diff_-100", threshold=0.05) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_forehead_after_100", wait_time=3) \
            .compare_photo("test_edit_forehead_before", "test_edit_forehead_after_100",
                           "test_edit_forehead_diff_100", threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("test_edit_forehead_save")

    @pytest.mark.Faces
    def test_edit_nose_noseenhance(self):
        self.app.deeplink_to_noseenhance()\
            .pick_photo("YMK_test_photos", 1)\
            .screenshot("test_edit_noseenhance_before", wait_time=3)\
            .adjust_intensity_to_right()\
            .screenshot("test_edit_noseenhance_after", wait_time=3)\
            .compare_photo("test_edit_noseenhance_before", "test_edit_noseenhance_after", "test_edit_noseenhance_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_noseenhance_save")


    @pytest.mark.Faces
    def test_edit_nose_nosesize(self):
        self.app.deeplink_to_noseenhance()\
            .pick_photo("YMK_test_photos", 1)\
            .select_noseenhance_function("Size") \
            .screenshot("test_edit_nosesize_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_nosesize_after_-100",wait_time=3)\
            .compare_photo("test_edit_nosesize_before", "test_edit_nosesize_after_-100", "test_edit_nosesize_diff_-100", threshold=0.05)\
            .adjust_intensity_to_right() \
            .screenshot("test_edit_nosesize_after_100", wait_time=3) \
            .compare_photo("test_edit_nosesize_before", "test_edit_nosesize_after_100", "test_edit_nosesize_diff_100", threshold=0.05)\
            .click_save()\
            .pull_photo_from_device("test_edit_nosesize_save")

    @pytest.mark.Faces
    def test_edit_nose_noselift(self):
        self.app.deeplink_to_noseenhance() \
            .pick_photo("YMK_test_photos", 1) \
            .select_noseenhance_function("Lift") \
            .screenshot("test_edit_noselift_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_noselift_after_-100", wait_time=3) \
            .compare_photo("test_edit_noselift_before", "test_edit_noselift_after_-100", "test_edit_noselift_diff_-100",
                           threshold=0.05) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_noselift_after_100", wait_time=3) \
            .compare_photo("test_edit_noselift_before", "test_edit_noselift_after_100", "test_edit_noselift_diff_100",
                           threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("test_edit_noselift_save")

    @pytest.mark.Faces
    def test_edit_nose_nosebridge(self):
        self.app.deeplink_to_noseenhance() \
            .pick_photo("YMK_test_photos", 1) \
            .select_noseenhance_function("Bridge") \
            .screenshot("test_edit_nosebridge_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_nosebridge_after_-100", wait_time=3) \
            .compare_photo("test_edit_nosebridge_before", "test_edit_nosebridge_after_-100", "test_edit_nosebridge_diff_-100",
                           threshold=0.05) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_nosebridge_after_100", wait_time=3) \
            .compare_photo("test_edit_nosebridge_before", "test_edit_nosebridge_after_100", "test_edit_nosebridge_diff_100",
                           threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("test_edit_nosebridge_save")

    @pytest.mark.Faces
    def test_edit_nose_nosetip(self):
        self.app.deeplink_to_noseenhance() \
            .pick_photo("YMK_test_photos", 1) \
            .select_noseenhance_function("Tip") \
            .screenshot("test_edit_nosetip_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_nosetip_after_-100", wait_time=3) \
            .compare_photo("test_edit_nosetip_before", "test_edit_nosetip_after_-100",
                           "test_edit_nosetip_diff_-100",
                           threshold=0.05) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_nosetip_after_100", wait_time=3) \
            .compare_photo("test_edit_nosetip_before", "test_edit_nosetip_after_100",
                           "test_edit_nosetip_diff_100",
                           threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("test_edit_nosetip_save")

    @pytest.mark.Faces
    def test_edit_nose_nosewing(self):
        self.app.deeplink_to_noseenhance() \
            .pick_photo("YMK_test_photos", 1) \
            .select_noseenhance_function("Wing") \
            .screenshot("test_edit_nosewing_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_nosewing_after_-100", wait_time=3) \
            .compare_photo("test_edit_nosewing_before", "test_edit_nosewing_after_-100",
                           "test_edit_nosewing_diff_-100",
                           threshold=0.05) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_nosewing_after_100", wait_time=3) \
            .compare_photo("test_edit_nosewing_before", "test_edit_nosewing_after_100",
                           "test_edit_nosewing_diff_100",
                           threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("test_edit_nosewing_save")

    @pytest.mark.Faces
    def test_edit_nose_nosewidth(self):
        self.app.deeplink_to_noseenhance() \
            .pick_photo("YMK_test_photos", 1) \
            .select_noseenhance_function("Width") \
            .screenshot("test_edit_nosewidth_before") \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_nosewidth_after_-100", wait_time=3) \
            .compare_photo("test_edit_nosewidth_before", "test_edit_nosewidth_after_-100",
                           "test_edit_nosewidth_diff_-100",
                           threshold=0.05) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_nosewidth_after_100", wait_time=3) \
            .compare_photo("test_edit_nosewidth_before", "test_edit_nosewidth_after_100",
                           "test_edit_nosewidth_diff_100",
                           threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("test_edit_nosewidth_save")

    @pytest.mark.animationfunctionhavebug
    def test_edit_wrinkle(self):
        self.app.deeplink_to_wrinkle()\
            .pick_photo("YMK_test_photos", 2)\
            .wait_animation()\
            .adjust_intensity_to_left()\
            .screenshot("test_edit_wrinkle_before", wait_time=3)\
            .adjust_intensity_to_right() \
            .screenshot("test_edit_wrinkle_after", wait_time=3) \
            .compare_photo("test_edit_wrinkle_before", "test_edit_wrinkle_after", "test_edit_wrinkle_diff") \
            .click_save()\
            .pull_photo_from_device("test_edit_wrinkle_save")

    @pytest.mark.animationfunctionhavebug
    def test_edit_uneven_skintone(self):
        self.app.deeplink_to_unevenskintone()\
            .pick_photo("YMK_test_photos",1)\
            .wait_animation()\
            .adjust_intensity_to_left() \
            .screenshot("test_edit_uneven_skintone_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_uneven_skintone_after", wait_time=3) \
            .compare_photo("test_edit_uneven_skintone_before", "test_edit_uneven_skintone_after", "test_edit_uneven_skintone_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_uneven_skintone_save")

    @pytest.mark.animationfunctionhavebug
    def test_edit_pores(self):
        self.app.deeplink_to_pores()\
            .pick_photo("YMK_test_photos", 1) \
            .wait_animation() \
            .adjust_intensity_to_left() \
            .screenshot("test_edit_pores_before", wait_time=3) \
            .adjust_intensity_to_right() \
            .screenshot("test_edit_pores_after", wait_time=3) \
            .compare_photo("test_edit_pores_before", "test_edit_pores_before",
                           "test_edit_pores_diff") \
            .click_save() \
            .pull_photo_from_device("test_edit_pores_save")

    @pytest.mark.cannotselectbrand
    def test_edit_foundation(self):
        self.app.deeplink_to_foundation()\
            .pick_photo("YMK_test_photos", 3)\
            .screenshot("test_edit_foundation_before", wait_time=2) \
            .select_color(1)\
            .adjust_intensity_to_top()\
            .screenshot("test_edit_foundation_after", wait_time=2) \
            .compare_photo("test_edit_foundation_before", "test_edit_foundation_after", "test_edit_foundation_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_foundation_save")

    @pytest.mark.animationfunctionhavebug
    def test_edit_concealer(self):
        self.app.deeplink_to_concealer()\
            .pick_photo("YMK_test_photos", 3)\
            .wait_animation()\
            .adjust_intensity_to_left()\
            .screenshot("test_edit_concealer_before", wait_time=2)\
            .adjust_intensity_to_right() \
            .screenshot("test_edit_concealer_after", wait_time=2)\
            .compare_photo("test_edit_concealer_before", "test_edit_concealer_after", "test_edit_concealer_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_concealer_save")

    @pytest.mark.cannotselectbrand
    def test_edit_blush(self):
        self.app.deeplink_to_blush()\
            .pick_photo("YMK_test_photos", 1)\
            .select_brand("PERFECT")\
            .screenshot("test_edit_blush_before", wait_time=2) \
            .select_color(5)\
            .screenshot("test_edit_blush_after", wait_time=2) \
            .compare_photo("test_edit_blush_before", "test_edit_blush_after",
                           "test_edit_blush_diff") \
            .click_save()\
            .pull_photo_from_device("test_edit_blush_save")

    @pytest.mark.cannotselectbrand
    def test_edit_contour(self):
        self.app.deeplink_to_contour()\
            .pick_photo("YMK_test_photos", 1)\
            .screenshot("test_edit_contour_before", wait_time=5)\
            .select_pattern(1)\
            .screenshot("test_edit_contour_after", wait_time=2)\
            .compare_photo("test_edit_contour_before", "test_edit_contour_after",
                           "test_edit_contour_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_contour_save")

    @pytest.mark.cannotselectbrand
    def test_edit_highlight(self):
        self.app.deeplink_to_highlight()\
            .pick_photo("YMK_test_photos", 1)\
            .select_brand("PERFECT")\
            .screenshot("test_edit_highlight_before", wait_time=2)\
            .select_pattern(1)\
            .screenshot("test_edit_highlight_after", wait_time=2)\
            .compare_photo("test_edit_highlight_before", "test_edit_highlight_after",
                           "test_edit_highlight_diff")\
            .click_save()\
            .pull_photo_from_device("test_edit_contour_save")

    @pytest.mark.Faces
    def test_edit_facepaint(self):
        self.app.deeplink_to_facepaint() \
            .pick_photo("YMK_test_photos", 1) \
            .screenshot("test_edit_facepaint_before", wait_time=2) \
            .select_pattern(2) \
            .screenshot("test_edit_facepaint_after", wait_time=2) \
            .compare_photo("test_edit_facepaint_before", "test_edit_facepaint_after",
                           "test_edit_facepaint_diff") \
            .click_save()\
            .pull_photo_from_device("test_edit_facepaint_save")

    @pytest.mark.Faces
    def test_edit_blemish(self):
        self.app.deeplink_to_blemish()\
            .pick_photo("YMK_test_photos", 1) \
            .screenshot("test_edit_blemish_before", wait_time=3) \
            .switch_onoff()\
            .screenshot("test_edit_blemish_after", wait_time=3) \
            .compare_photo("test_edit_blemish_before", "test_edit_blemish_after",
                           "test_edit_blemish_diff")\
            .click_save() \
            .pull_photo_from_device("test_edit_blemish_save")

    @pytest.mark.Faces
    def test_edit_shinremoval(self):
        self.app.deeplink_to_shineremoval()\
            .pick_photo("YMK_test_photos", 1) \
            .screenshot("test_edit_shinremoval_before", wait_time=3) \
            .adjust_intensity_to_right()\
            .screenshot("test_edit_shinremoval_after", wait_time=3) \
            .compare_photo("test_edit_shinremoval_before", "test_edit_shinremoval_after",
                           "test_edit_shinremoval_diff", threshold=0.05) \
            .click_save() \
            .pull_photo_from_device("test_edit_shinremoval_save")

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


"""if __name__ == '__main__':
    #pytest.main(['--html=face_result.html', '--disable-warnings', './tests/YMK/', '-rA', '-m=Faces'])
    t = TestFace()
    t.setup_method()
    t.test_edit_faceshaper_forehead()
    t.teardown_method()"""
    
