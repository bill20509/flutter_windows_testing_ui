from libs.YMK.locators import AccessoriesLocators, PhotoMakeupLocators
from libs.YMK import pages


class Accessories(pages.photomakeup_page.PhotoMakeup):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def click_store(self):
        self.click_element(AccessoriesLocators.store_button)
        return pages.store_page.Store

    def select_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, (number - 1))
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self

    def tap_central(self):
        self.tap_element_coordinates(AccessoriesLocators.editroom_view)
        return self

    def select_eyewear(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Eyewear")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Eyewear(self.driver)

    def select_headband(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Headband")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Headband(self.driver)

    def select_necklace(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Necklace")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Necklace(self.driver)

    def select_earrings(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Earrings")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Earrings(self.driver)

    def select_hat(self):
        for i in range(10):
            try:
                self.click_element_by_name(PhotoMakeupLocators.category, "Hat")
                break
            except (ValueError, Exception):
                self.scroll_horizontal(PhotoMakeupLocators.makeup_menu)
        return Hat(self.driver)


class Eyewear(Accessories):
    # X 215 Y 922
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_eyewear_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, number)
                break
            except (ValueError, Exception):
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self


class Headband(Accessories):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_headband_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, number)
                break
            except (ValueError, Exception):
                self.wait_element_visible(AccessoriesLocators.pattern_view)
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self


class Necklace(Accessories):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_necklace_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, number)
                break
            except (ValueError, Exception):
                self.wait_element_visible(AccessoriesLocators.pattern_view)
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self


class Earrings(Accessories):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_earring_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, number)
                break
            except (ValueError, Exception):
                self.wait_element_visible(AccessoriesLocators.pattern_view)
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self


class Hat(Accessories):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def select_hat_pattern(self, number):
        for i in range(10):
            try:
                self.select_element_by_number(AccessoriesLocators.pattern_item, number)
                break
            except (ValueError, Exception):
                self.wait_element_visible(AccessoriesLocators.pattern_view)
                self.scroll_horizontal(AccessoriesLocators.pattern_view)
        return self
