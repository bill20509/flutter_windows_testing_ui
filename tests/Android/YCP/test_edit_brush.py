import pytest
from libs.app import App
from libs.YCP import pages
import time


class Test(object):

    def setup_method(self):  # run before every test
        self.driver = App().set_auto()\
            .set_app("YCP")\
            .set_auto_launch(True)\
            .set_wait_time(5)\
            .set_newcommand_timeout(9999)\
            .create()

        self.app = pages.launcher.LauncherPage(self.driver)

    @pytest.mark.camera
    def test_edit_brush_apply(self): 
        # Riley 1.apply brush
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_samples")\
                .select_photo_item(6)\
                .click_brush()\
                .screenshot("edit_brush_apply_before",3)\
                .click_style_tab()\
                .select_style_item(2)\
                .draw_on_photo(0.3, 0.3, 0.6, 0.2)\
                .click_color_tab()\
                .select_color_item(2)\
                .draw_on_photo(0.1, 0.5, 0.8, 0.5)\
                .screenshot("edit_brush_apply_after",3)\
                .compare_photo("edit_brush_apply_before", "edit_brush_apply_after", "edit_brush_apply_diff")\
                .click_apply()\
                .screenshot("edit_brush_apply_lobby",3)\
                .click_save()\
                .pull_photo_from_device("edit_brush_apply_save")
                

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_brush_apply()
    t.teardown_method()
