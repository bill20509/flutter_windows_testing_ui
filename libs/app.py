# from importlib.util import set_package
from appium import webdriver
import subprocess


class App:

    def __init__(self):
        self.caps = {
            'udid': "",
            "platformName": "",
            "platformVersion": "",
            "appPackage": "",
            "appActivity": "",
            "ignoreHiddenApiPolicyError": True,
            "noReset": True,
            "autoGrantPermissions": True,
            "newCommandTimeout": 60,
            "autoLaunch": False,
            "disableWindowAnimation": False,
            "waitForIdleTimeout": 10000,
            "chromedriverExecutableDir": './PFQA_APP_UI/chromedriver',
            "chromedriverChromeMappingFile": './PFQA_APP_UI/chromedriver/chromedriver_support.json'
        }
        self.wait_time = 5

    def set_udid(self, udid):
        self.caps["udid"] = udid
        return self

    def set_auto_launch(self, bool):
        self.caps["autoLaunch"] = bool
        return self

    def set_auto(self):
        # set udid
        result = subprocess.run(
            ['adb', 'devices'], stdout=subprocess.PIPE, text=True)
        split_list = result.stdout.strip().split()
        index = split_list.index('device')
        self.caps['udid'] = split_list[index - 1]

        # set version
        result = subprocess.run(
            ['adb', 'shell', 'getprop', 'ro.build.version.release'], stdout=subprocess.PIPE, text=True)
        self.caps['platformVersion'] = str(result.stdout.strip())

        # set platform
        self.caps['platformName'] = 'Android'

        return self

    def set_platform(self, platform):
        self.caps["platformName"] = platform
        return self

    def set_version(self, version):
        self.caps["platformVersion"] = version
        return self

    def set_app(self, app_name):
        assert app_name in ["YCP", "YMK"]
        if app_name == "YCP":
            self.caps["appPackage"] = "com.cyberlink.youperfect"
            self.caps["appActivity"] = "com.cyberlink.youperfect.activity.SplashActivity"
        elif app_name == "YMK":
            self.caps["appPackage"] = "com.cyberlink.youcammakeup"
            self.caps["appActivity"] = "com.cyberlink.youcammakeup.activity.SplashActivity"
        return self

    def set_newcommand_timeout(self, timeout):
        self.caps["newCommandTimeout"] = timeout
        return self

    def set_noreset(self, bool):
        self.caps["noReset"] = bool
        return self

    def set_wait_time(self, wait_time):
        self.wait_time = wait_time
        return self

    def set_disable_animation(self):
        self.caps["waitForIdleTimeout"] = 1000
        self.caps["disableWindowAnimation"] = True
        return self

    def create(self):
        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        driver.implicitly_wait(self.wait_time)
        return driver

    # def close(self):
    #     self.driver.quit()
if __name__ == '__main__':
    app = App().set_auto()
    print(app.caps)
