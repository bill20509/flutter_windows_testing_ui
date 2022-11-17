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

    @pytest.mark.edit
    def test_edit_tools(self):  # Carolyn
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_edit")\
                .select_photo_item(0)\
                .click_tools()\
                .screenshot("test_edit_tools_enable")\
                .click_element_by_text("Tools")\
                .screenshot("test_edit_tools_disable")\


    @pytest.mark.edit
    def test_lobby_undo(self):  # Carolyn
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_edit")\
                .select_photo_item(1)\
                .screenshot("test_lobby_undo_before") \
                .click_instafit() \
                .click_apply() \
                .click_undo() \
                .screenshot("test_lobby_undo") \
                .compare_photo("test_lobby_undo_before", "test_lobby_undo", "test_lobby_undo_diff")\


    @pytest.mark.edit
    def test_lobby_redo(self):  # Carolyn
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_edit")\
                .select_photo_item(1)\
                .screenshot("test_lobby_redo_before",1) \
                .click_instafit() \
                .click_apply() \
                .click_undo() \
                .click_redo() \
                .screenshot("test_lobby_redo",1) \
                .compare_photo("test_lobby_redo_before", "test_lobby_redo", "test_lobby_redo_diff")\


    @pytest.mark.edit
    def test_lobby_save(self):  # Carolyn
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_edit")\
                .select_photo_item(0)\
                .click_save()\
                .pull_photo_from_device("test_lobby_save")


    @pytest.mark.edit
    def test_lobby_crown(self): # Carolyn
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_edit")\
                .select_photo_item(0)\
                .click_crown_icon()\
                .screenshot("test_lobby_crown") \

    @pytest.mark.edit
    def test_lobby_beautify_tab(self): # Carolyn
        self.app.deeplink_to_launcher()\
                .click_photo_edit()\
                .select_album_item("a_edit")\
                .select_photo_item(0)\
                .click_beautify_tab()\
                .screenshot("test_lobby_beautify_tab", 1) \

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    t = Test()
    t.setup_method()
    t.test_edit_tools()
    t.test_lobby_undo()
    t.test_lobby_redo()
    t.test_lobby_crown()
    t.test_lobby_beautify_tab()
    t.teardown_method()
