import pytest
from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
from pytest_html import extras
folder_name = "1.Makeup"
folder_name2 = "7.PNG"
folder_name3 = "8.HEIC"


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
    def test_download_looks(self, extra):
        self.app.deeplink_to_photomakeup()\
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks()\
            .click_store()\
            .wait_time(5)\
            .click_club_chic_look()\
            .screenshot('test_download_looks', 5)
        extra.append(extras.image('screenshot/test_download_looks.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_look_info_profile(self, extra):
        self.app.deeplink_to_photomakeup()\
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks()\
            .select_look_item("Alluring")\
            .click_look_info() \
            .click_element_by_text("View Profile")\
            .screenshot('test_look_info_profile', 2)
        extra.append(extras.image('screenshot/test_look_info_profile.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_look_info_learn_more(self, extra):
        self.app.deeplink_to_photomakeup()\
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks()\
            .select_look_item("Alluring")\
            .click_look_info() \
            .click_element_by_text("Learn More About This Look")\
            .screenshot('test_look_info_learn_more', 2)
        extra.append(extras.image('screenshot/test_look_info_learn_more.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_look_info_copy_link(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks() \
            .select_look_item("Alluring") \
            .click_look_info() \
            .click_element_by_text("Copy Link") \
            .screenshot('test_look_info_copy_link', 2)
        extra.append(extras.image('screenshot/test_look_info_copy_link.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_look_info_share_look(self, extra):
        self.app.deeplink_to_setting() \
            .login_bc_account("bb@bb.com", "bbbbbb")
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks() \
            .select_look_item("Alluring") \
            .click_look_info() \
            .click_element_by_text("Share Look") \
            .click_share_to_yc()\
            .share_look("test_look_info_share_look(auto test)")\
            .screenshot('test_look_info_share_look', 2)
        extra.append(extras.image('screenshot/test_look_info_share_look.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_look_info_see_more(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks() \
            .select_look_item("Alluring") \
            .click_look_info() \
            .click_element_by_text("See More Looks") \
            .screenshot('test_look_info_see_more', 2)
        extra.append(extras.image('screenshot/test_look_info_see_more.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_asia_model(self, extra):
        self.app.deeplink_to_me() \
            .click_setting() \
            .click_country() \
            .switch_country_to("Japan")\
            .deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks() \
            .select_look_item("Alluring") \
            .waiting_cursor() \
            .screenshot('test_asia_model_look', 2)\
            .deeplink_to_hairstyle() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .screenshot('test_asia_model_hair', 2)\
            .deeplink_to_facepaint() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .screenshot('test_asia_model_face_paint', 2)\
            .deeplink_to_me() \
            .click_setting() \
            .click_country() \
            .switch_country()
        extra.append(extras.image('screenshot/test_asia_model_look.png'))
        extra.append(extras.image('screenshot/test_asia_model_hair.png'))
        extra.append(extras.image('screenshot/test_asia_model_face_paint.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_import_png(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name2, 1) \
            .waiting_cursor() \
            .select_looks() \
            .select_look_item("Alluring") \
            .click_save() \
            .pull_photo_from_device("test_import_png")
        extra.append(extras.image('savephoto/test_import_png.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_import_heic(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name3, 1) \
            .waiting_cursor() \
            .select_looks() \
            .select_look_item("Alluring") \
            .click_save()\
            .pull_photo_from_device("test_import_heic")
        extra.append(extras.image('savephoto/test_import_heic.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_import_jpg(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks() \
            .select_look_item("Alluring") \
            .click_save()\
            .pull_photo_from_device("test_import_jpg")
        extra.append(extras.image('savephoto/test_import_jpg.jpg'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_add_favorite(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks() \
            .select_look_item("Alluring") \
            .add_look_to_favorite("Alluring")\
            .click_heart()\
            .screenshot("test_add_favorite", 2)\
            .remove_look_from_favorite("Alluring") \
            .screenshot("test_remove_favorite",2)
        extra.append(extras.image('screenshot/test_remove_favorite.png'))
        extra.append(extras.image('screenshot/test_add_favorite.png'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_adjust_look_intensity(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks() \
            .select_look_item("Alluring") \
            .waiting_cursor() \
            .screenshot("test_adjust_look_intensity_before", 2) \
            .adjust_intensity_to_down() \
            .waiting_cursor() \
            .screenshot("test_adjust_look_intensity_0", 2) \
            .adjust_intensity_to_top() \
            .waiting_cursor() \
            .screenshot("test_adjust_look_intensity_100", 2) \
            .compose_gif("test_adjust_look_intensity", "screenshot/test_adjust_look_intensity_before.png",
                         "screenshot/test_adjust_look_intensity_0.png",
                         "screenshot/test_adjust_look_intensity_100.png", speed=1)
        extra.append(extras.image('screenshot/test_adjust_look_intensity.gif'))

    @pytest.mark.B
    @pytest.mark.S1
    def test_inplace_download(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks() \
            .select_look_category("Background") \
            .screenshot("test_inplace_download_before", 3)\
            .select_look_by_number(1)\
            .screenshot("test_inplace_download_after", 10)
        extra.append(extras.image('screenshot/test_inplace_download_after.png'))
        extra.append(extras.image('screenshot/test_inplace_download_before.png'))

    @pytest.mark.B
    @pytest.mark.S2
    def test_share_premium_look(self, extra):
        self.app.deeplink_to_photomakeup() \
            .pick_photo(folder_name, 1) \
            .waiting_cursor() \
            .select_looks() \
            .click_crown()\
            .select_look_by_number(1)\
            .wait_download_pack()\
            .click_save() \
            .show_result_page() \
            .share_look("test_share_premium_look(auto test)") \
            .screenshot("share_premium_look", 3)
        extra.append(extras.image('screenshot/share_premium_look.png'))


    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()
