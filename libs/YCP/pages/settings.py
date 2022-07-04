from libs.YCP import pages
from libs.YCP.locator import *


class SettingsPage(pages.YCP_base.YCPBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)
