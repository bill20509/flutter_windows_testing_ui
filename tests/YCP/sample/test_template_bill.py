import subprocess
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
            .set_disable_animation()\
            .set_newcommand_timeout(9999)\
            .create()

        self.app = pages.launcher.LauncherPage(self.driver)

    @pytest.mark.camera
    def test_animation(self):
        self.app.deeplink_to_photo_edit()\
            .wait_loading_panel()\
            .click_effects()\
            .click_animation_tab()\
            .select_animation_category('Love')\
            .select_animation_item(1)\
            .click_erase()\
            .select_dot_item(4)\
            .set_hardness(10)

    @pytest.mark.camera
    def test_test(self):
        stage1 = self.app.deeplink_to_launcher()\
            .click_hot_feature_templates()

    def teardown_method(self):  # quit driver when test case done
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    path = '/sdcard/DCIM/YouCam\ Perfect/'
    cmd = ["adb", "shell", "ls", path + '*.jpg']
    print(path)
    print(cmd)
    res = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\
        .communicate()[0].decode("utf-8")\
        .replace(path, '').strip().split("\n")
    print(res)
    # .replace("", '').strip().split("\r\n")
    # print(res)
    # process1 = subprocess.Popen(
    # cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE).communicate()[0].decode("utf-8")
    # t = Test()
    # t.setup_method()
    # t.test_test()
