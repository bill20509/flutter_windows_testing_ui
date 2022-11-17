from libs.app import App
from libs.YMK.pages.YMK_base import YMKbase
import time
import pytest
from pytest_html import extras
from libs.YMK.locators import AgingLocators

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

    @pytest.mark.A
    @pytest.mark.N1
    def test_ad_aging_result_page(self, extra):
        result_ad = self.app.deeplink_to_launcher() \
            .click_aging_tile() \
            .click_tryit() \
            .choose_photo() \
            .click_bipa_agree() \
            .pick_photo(album_name1, 1) \
            .wait_animation() \
            .screenshot("test_ad_aging_result_page", wait_time=3) \
            .check_result_page_ad()

        extra.append(extras.image('screenshot/test_ad_aging_result_page.png'))

        if result_ad == 1:
            print("\nResult: PASS\n" + "Have AD in Time Machine result page")
        else:
            pytest.fail("No AD in Time Machine result page")

    @pytest.mark.A
    @pytest.mark.N1
    def test_ad_aging_save_page(self, extra):
        save_ad = self.app.deeplink_to_launcher() \
            .click_aging_tile() \
            .click_tryit() \
            .choose_photo() \
            .click_bipa_agree() \
            .pick_photo(album_name1, 1) \
            .wait_animation() \
            .click_save() \
            .screenshot("test_ad_aging_save_page", wait_time=3) \
            .check_save_page_ad()
        extra.append(extras.image('screenshot/test_ad_aging_save_page.png'))

        if save_ad == 1:
            print("\nResult: PASS\n" + "Have AD in Time Machine save page")
        else:
            pytest.fail("No AD in Time Machine result page")

    @pytest.mark.A
    @pytest.mark.N1
    def test_ad_launcher_banner(self, extra):
        ad_banner = self.app.deeplink_to_launcher().check_launcher_page_ad()
        self.app.screenshot("test_ad_launcher_banner", wait_time=3)
        extra.append(extras.image('screenshot/test_ad_launcher_banner.png'))

        if ad_banner == 1:
            print("\nResult: PASS\n" + "Have AD in Launcher Banner")
        else:
            pytest.fail("No AD in Launcher banner")

    @pytest.mark.A
    @pytest.mark.N1
    def test_ad_bc_trending(self, extra):
        ad_trending = self.app.deeplink_to_launcher() \
            .click_bc_button() \
            .check_trending_page_ad()
        self.app.screenshot("test_ad_bc_trending", wait_time=3)
        extra.append(extras.image('screenshot/test_ad_bc_trending.png'))

        if ad_trending == 1:
            print("\nResult: PASS\n" + "Have AD in Launcher Banner")
        else:
            pytest.fail("No AD in Launcher banner")

    @pytest.mark.A
    @pytest.mark.N1
    def test_ad_hw_back(self, extra):
        ad_hw_back = self.app.deeplink_to_launcher() \
            .check_hw_back_ad()
        self.app.screenshot("test_ad_hw_back", wait_time=3)
        extra.append(extras.image('screenshot/test_ad_hw_back.png'))

        if ad_hw_back == 1:
            print("\nResult: PASS\n" + "Have AD when press HW-Back")
        else:
            pytest.fail("No AD when press HW-Back")

    @pytest.mark.A
    @pytest.mark.N1
    def test_ad_photo_picker(self, extra):
        ad_photo_picker = self.app.deeplink_to_launcher() \
            .click_photomakeup_button() \
            .check_bipa_and_close() \
            .pick_album(album_name1) \
            .check_photo_picker_ad()
        self.app.screenshot("test_ad_photo_picker", wait_time=3)
        extra.append(extras.image('screenshot/test_ad_photo_picker.png'))

        if ad_photo_picker == 1:
            print("\nResult: PASS\n" + "Have AD in Photo Picker")
        else:
            pytest.fail("No AD in Photo Picker")

    @pytest.mark.A
    @pytest.mark.N1
    def test_ad_photo_result_page_interstitial(self, extra):
        interstitial_ad = self.app.deeplink_to_photomakeup() \
            .pick_photo(album_name1, 1) \
            .click_save() \
            .check_result_page_interstitial_ad()
        self.app.screenshot("test_ad_photo_result_page_interstitial", wait_time=3)
        extra.append(extras.image('screenshot/test_ad_photo_result_page_interstitial.png'))

        if interstitial_ad == 1:
            print("\nResult: PASS\n" + "Have interstitial AD in result page")
        else:
            pytest.fail("No interstitial AD in result page")

    @pytest.mark.A
    @pytest.mark.N1
    def test_ad_photo_result_page_banner(self, extra):
        result_ad_banner = self.app.deeplink_to_photomakeup() \
            .pick_photo(album_name1, 1) \
            .click_save() \
            .check_result_page_ad_banner()
        self.app.screenshot("test_ad_photo_result_page_banner", wait_time=3)
        extra.append(extras.image('screenshot/test_ad_photo_result_page_banner.png'))

        if result_ad_banner == 1:
            print("\nResult: PASS\n" + "Have AD Banner in result page")
        else:
            pytest.fail("No AD Banner in result page")

    @pytest.mark.A
    @pytest.mark.N1
    def test_ad_back_from_cam(self, extra):
        ad_back = self.app.deeplink_to_launcher() \
            .check_ad_back_from_cam()
        self.app.screenshot("test_ad_photo_result_page_banner", wait_time=3)
        extra.append(extras.image('screenshot/test_ad_photo_result_page_banner.png'))

        if ad_back == 1:
            print("\nResult: PASS\n" + "Have AD when back from cam")
        else:
            pytest.fail("No AD when back from cam")

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()

# if __name__ == '__main__':
#     #pytest.main(['--html=face_result.html', '--disable-warnings', './tests/YMK/', '-rA', '-m=Faces'])
#     t = Test()
#     t.setup_method()
#     t.test_aging_resultAD()
#     t.teardown_method()
