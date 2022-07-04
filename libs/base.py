# 工具包
import os
import re
import subprocess
import time
from pathlib import Path

from libs.element import Element
from appium import webdriver
from libs.exception import ElementMissingException
from wand.image import Image
from typing import Optional, Union
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction


class BasePage(object):
    DEBUG_PERFORMANCE = False

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    # Deep link
    def deeplink(self, page_link, package_name=""):
        """
        It is deeplink
        """
        if package_name == "":
            package_name = self.driver.caps["appPackage"]
        self.driver.execute_script(
            "mobile: deepLink",
            {
                "url": page_link,
                "package": package_name
            }
        )
        return self

    def screenshot(self, screen_shot_name: str, wait_time=0):
        """Take screenshot in current page and save to /screenshot folder
        Args:
            screenshotname (_type_, optional): Screen shot name, should be end with extension .png . Defaults to str.
            wait_time (_type_, optional): After [wait_time] seconds, then takes screen shot. Defaults to 0.
        Returns:
            _type_: _description_
            :param wait_time:
            :param screen_shot_name:
        """
        photopath = 'screenshot/'
        Path(photopath).mkdir(parents=True, exist_ok=True)
        screenshotName = screen_shot_name + '.png'
        time.sleep(wait_time)
        self.driver.save_screenshot(photopath + screenshotName)
        print("Save: ", screenshotName)
        return self

    def find_element(self, element):
        """Find element, if it misses, raise [ElementMissingException]
        :Args:
         - element: Element
        :Usage:
        `self.driver.find_element(Locator.xxx_button)`
        """
        try:
            self.driver.find_element(element.element_type, element.element_id)
        except:
            message = "Can't find " + element.element_desc
            print(message)
            raise ElementMissingException(message)
        return self

    def find_element_by_name(self, element: Element, name):
        el_id = "//*[@resource-id='{0}'][@text='{1}']".format(
            element.element_id, name)
        element = Element(el_id, element.element_type, element.element_desc)
        self.find_element(element)
        return self

    def find_element_by_text(self, text: str):
        """Find element by text, if it misses, raise [ElementMissingException]
        :Args:
         - text: the text you want to search
        :Usage:
        `self.driver.find_element_by_text("Tools")`
        """
        element = Element('//*[@text="{0}"]'.format(text), "xpath", text)
        self.find_element(element)
        return self

    def click_element(self, element: Element):
        """Click element by ID, if it misses, raise [ElementMissingException]
        Args:
        - element: the element ID you want to click
        Usage:
        - self.click_element(Locator.xxx_button)
        """
        try:
            if(element.element_type == 'text'):
                self.click_element_by_text(element.element_id)
            else:
                self.driver.find_element(
                    element.element_type, element.element_id).click()
        except:
            message = "Can't find " + element.element_desc
            print(message)
            raise ElementMissingException(message)
        return self

    # Click the element by name (resource-id and text)
    def click_element_by_name(self, element, name):
        el_id = "//*[@resource-id='{0}'][@text='{1}']".format(
            element.element_id, name)
        element = Element(el_id, element.element_type, element.element_desc)
        self.click_element(element)
        return self

    def click_element_by_text(self, text: str):
        """Click element by text, if it misses, raise [ElementMissingException]
        :Args:
         - text: the text you want to search
        :Usage:
        `self.driver.click_element_by_text("Tools")`
        """
        element = Element('//*[@text="{0}"]'.format(text), "xpath", text)
        self.click_element(element)
        return self

    # Select element by number (resource-id and index[])
    def select_element_by_number(self, element: Element, number: int):
        """ Click [number]'s element
        Args:
            element (Element): 
            number (int): index, start from 0
        Returns:
            return self
        """
        try:
            e = self.driver.find_elements(
                element.element_type, element.element_id)
            e[number].click()
        except:
            message = "Can't find " + element.element_desc
            print(message)
            raise ElementMissingException(message)
        return self

    # Send Value to element
    def send_keys_to_element(self, element: Element, value):
        """Send value to element, if it misses, raise [ElementMissingException]
        :Args:
         - : the value you want to set
        :Usage:
        `self.send_keys_to_element(Locator.xxx_button, value)`
        """
        try:
            el = self.driver.find_element(
                element.element_type, element.element_id).send_keys(str(value))
            print(el.get_attribute("text"))
        except:
            message = "Can't send value to " + element.element_desc
            print(message)
            raise ElementMissingException(message)
        return self

    def check_element_is_displayed(self, element):
        if self.driver.find_element(element.element_type, element.element_id).is_displayed():
            self.driver.find_element(
                element.element_type, element.element_id).click()
        return self

    def long_press_element(self, element: Element, name):
        el_id = "//*[@resource-id='{0}'][@text='{1}']".format(
            element.element_id, name)
        element = Element(el_id, element.element_type, element.element_desc)
        el = self.driver.find_element(element.element_type, element.element_id)
        actions = ActionChains(self.driver)
        actions.click_and_hold(el).perform()
        return self

    def drag_and_drop_element(self, element1, name, element2):
        actions = ActionChains(self.driver)
        el1_id = "//*[@resource-id='{0}'][@text='{1}']".format(
            element1.element_id, name)
        element1 = Element(el1_id, element1.element_type,
                           element1.element_desc)
        el1 = self.driver.find_element(
            element1.element_type, element1.element_id)
        actions.click_and_hold(el1).perform()
        el2 = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, element2.element_id)))
        actions.drag_and_drop(el1, el2).perform()
        return self

    def scroll_horizontal(self, element):
        el = self.driver.find_element(element.element_type, element.element_id)
        width = el.size["width"]
        height = el.size["height"]
        from_x = width * 0.8
        to_x = width * 0.2
        self.driver.execute_script("mobile:dragGesture",
                                   {"elementId": el,
                                    "startX": from_x, "startY": height * 0.5,
                                    "endX": to_x, "endY": height * 0.5})

    def scroll_vertical(self, element):
        el = self.driver.find_element(element.element_type, element.element_id)
        width = el.size["width"]
        height = el.size["height"]
        from_y = height * 0.8
        to_y = height * 0.2
        self.driver.execute_script("mobile:dragGesture",
                                   {"elementId": el,
                                    "startX": width * 0.5, "startY": from_y,
                                    "endX": width * 0.5, "endY": to_y})

    def slidebar_to_top(self, element: Element):
        e = self.driver.find_element(
            element.element_type, element.element_id)
        m_x = int(e.location["x"] + e.size["width"] / 2)
        m_y = int(e.location["y"] + e.size["height"] / 2)
        t_x = int(e.location["x"] + e.size["width"])
        t_y = int(e.location["y"])
        self.driver.swipe(m_x, m_y, t_x, t_y)
        return self

    def sliderbar_to_down(self, element: Element):
        e = self.driver.find_element(
            element.element_type, element.element_id)
        m_x = int(e.location["x"] + e.size["width"] / 2)
        m_y = int(e.location["y"] + e.size["height"] / 2)
        d_x = int(e.location["x"])
        d_y = int(e.location["y"] + e.size["height"])
        self.driver.swipe(m_x, m_y, d_x, d_y)
        return self

    def slidebar_to_right(self, element: Element):
        """Given a element, slide it to rightmost

        Args:
            element (Element): The element be slided.

        Returns:
            return self
        """
        e = self.driver.find_element(
            element.element_type, element.element_id)
        m_x = int(e.location["x"] + e.size["width"] / 2)
        m_y = int(e.location["y"] + e.size["height"] / 2)
        r_x = int(e.location["x"] + e.size["width"])
        r_y = int(e.location["y"] + e.size["height"] / 2)
        self.driver.swipe(m_x, m_y, r_x, r_y)
        return self

    def slidebar_to_left(self, element: Element):
        """Given a element, slide it to leftmost

        Args:
            element (Element): The element be slided.

        Returns:
            return self
        """
        e = self.driver.find_element(
            element.element_type, element.element_id)
        m_x = int(e.location["x"] + e.size["width"] / 2)
        m_y = int(e.location["y"] + e.size["height"] / 2)
        l_x = int(e.location["x"])
        l_y = int(e.location["y"])
        self.driver.swipe(m_x, m_y, l_x, l_y)
        return self

    def wait_element_visible(self, element, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located((By.ID, element.element_id)))
        except:
            message = "Can't find " + element.element_desc
            print(message)
            raise ElementMissingException(message)
        return self

    def wait_element_invisible(self, element, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.invisibility_of_element_located((By.ID, element.element_id)))
        except:
            message = "Can't find " + element.element_desc
            print(message)
            raise ElementMissingException(message)
        return self

    def click_element_in_list(self, element: Optional[Union[str, Element]], list: Element):
        """ Scroll to search an element in list, then click it.

        Args:
            element (Optional[Union[str, Element]]): Can be str or Element
            list (Element): list

        Returns:
            _type_: self
        """
        for i in range(5):
            try:
                if(isinstance(element, str)):
                    self.click_element_by_text(element)
                elif(isinstance(element, Element)):
                    self.click_element(element)
                break
            except:
                # TODO: need to implement scroll to left
                self.scroll_horizontal(list)
                time.sleep(1)
        return self

    def tap_element_coordinates(self, element, x=None, y=None):
        if element is None:
            m_x = x
            m_y = y
        else:
            e = self.driver.find_element(
                element.element_type, element.element_id)
            m_x = int(e.location["x"] + e.size["width"] / 2)
            m_y = int(e.location["y"] + e.size["height"] / 2)
            actions = TouchAction(self.driver)
            actions.tap(e, m_x, m_y).perform()
        return self

    def compare_photo(self, photo_a_name: str, photo_b_name: str, diff_photo_name="", result_match=0, threshold=0.0):
        """Compare two photo, if the diff value is bigger than result_match, then raise [AssertionError]
        Args:
            photo_a_name (str): photo a name. Defaults to str.
            photo_b_name (str): photo b name. Defaults to str.
            result_match (int, optional): The expected diff value . Defaults to 0.
            diff_photo_name (str, optional): The difference photo name, if == "", then would not save. Defaults to "".
            threshold (float, optional): Threshold. Defaults to 0.10.
        Returns:
            BasePage: self
        """
        photo_a = 'screenshot/' + photo_a_name + '.png'
        photo_b = 'screenshot/' + photo_b_name + '.png'
        diffresult = 'screenshot/' + diff_photo_name + '.png'
        with Image(filename=photo_a) as base:
            with Image(filename=photo_b) as img:
                base.fuzz = base.quantum_range * threshold
                result_image, result_metric = base.compare(img, 'absolute')
                if diff_photo_name != "":
                    with result_image:
                        result_image.save(filename=diffresult)
                # assert float(result_metric) <= result_match
        return self

    # TODO:change file path
    def pull_photo_from_device(self, rename):
        folder = 'savephoto/'
        Path(folder).mkdir(parents=True, exist_ok=True)
        device = self.driver.caps["udid"]
        cmd = 'adb -s {0} shell ls /sdcard/DCIM/YouCam\ Makeup/*.jpg'.format(
            device)
        process1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\
            .communicate()[0].decode("utf-8")\
            .replace('/sdcard/DCIM/YouCam Makeup/', '').strip().split("\r\n")
        last_photo = max(process1)
        pull = 'adb -s {0} pull "/sdcard/DCIM/YouCam Makeup/{1}" {2}'.format(
            device, last_photo, folder)
        subprocess.Popen(pull, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE).wait(5)
        rename = rename + '.jpg'
        # old_file = os.path.join(folder, last_photo)
        # new_file = os.path.join(folder, rename)
        old_file = Path(folder + last_photo)
        file_check = Path(folder + rename)
        if file_check.exists():
            os.remove(file_check)
            print("Delete old photo {0}".format(rename))
        old_file.rename(file_check)
        print("Rename {0} to {1}".format(last_photo, rename))
        return self

    # iOS only=====================================================================================================
    def adjust_slider_to_value(self, element, target_value):
        el = self.driver.find_element(element.element_type, element.element_id)
        is_vertical = el.size["height"] > el.size["width"]
        if is_vertical:
            self.__adjust_vertical_slider_to_value(el, target_value)
        else:
            self.__adjust_horizontal_slider_to_value(el, target_value)

    def __adjust_horizontal_slider_to_value(self, element, target_value):
        thumb_size = 18
        width = element.size["width"] - thumb_size
        height = element.size["height"]
        print("width %d, height %d" % (width, height))
        current_value = self.get_slider_value(element)
        target_value = float(target_value)
        print("current_value %f, target_value %f" %
              (current_value, target_value))

        if current_value == target_value:
            return

        start_x = thumb_size / 2
        from_x = start_x + width * current_value
        to_x = start_x + width * target_value
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.01, "element": element, "fromX": from_x,
                                    "fromY": height * 0.5, "toX": to_x, "toY": height * 0.5})
        current_value = self.get_slider_value(element)
        print("current_value %f, target_value %f" %
              (current_value, target_value))

        loop = 0
        while current_value != target_value and loop < 10:
            offset = 5
            from_x = start_x + width * current_value
            if current_value > target_value:
                to_x = to_x - offset
            else:
                to_x = to_x + offset
            self.driver.execute_script("mobile:dragFromToForDuration",
                                       {"duration": 0.01, "element": element, "fromX": from_x,
                                        "fromY": height * 0.5, "toX": to_x, "toY": height * 0.5})
            current_value = self.get_slider_value(element)
            print("current_value %f, target_value %f" %
                  (current_value, target_value))
            loop += 1

    def __adjust_vertical_slider_to_value(self, element, target_value):
        thumb_size = 18
        width = element.size["width"]
        height = element.size["height"] - thumb_size
        print("width %d, height %d" % (width, height))
        current_value = self.get_slider_value(element)
        target_value = float(target_value)
        print("current_value %f, target_value %f" %
              (current_value, target_value))

        if current_value == target_value:
            return

        start_y = height - thumb_size / 2
        from_y = start_y - height * current_value
        to_y = start_y - height * target_value
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.01, "element": element, "fromX": width * 0.5,
                                    "fromY": from_y, "toX": width * 0.5, "toY": to_y})
        current_value = self.get_slider_value(element)
        print("current_value %f, target_value %f" %
              (current_value, target_value))

        loop = 0
        while current_value != target_value and loop < 10:
            offset = 5
            from_y = start_y - height * current_value
            if current_value > target_value:
                to_y = to_y + offset
            else:
                to_y = to_y - offset
            self.driver.execute_script("mobile:dragFromToForDuration",
                                       {"duration": 0.01, "element": element, "fromX": width * 0.5,
                                        "fromY": from_y, "toX": width * 0.5, "toY": to_y})
            current_value = self.get_slider_value(element)
            print("current_value %f, target_value %f" %
                  (current_value, target_value))
            loop += 1

    def get_slider_value(self, element):
        return int(re.search(r'\d+', element.get_attribute("value")).group()) / 100

    def swipe_gesture(self, element, fromx=float, tox=float, fromy=float, toy=float, duration=int):
        width = element.size["width"]
        height = element.size["height"]
        print("width %d, height %d" % (width, height))

        from_x = width * fromx
        to_x = width * tox
        from_y = height * fromy
        to_y = height * toy
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": duration, "element": element, "fromX": from_x,
                                    "fromY": from_y, "toX": to_x, "toY": to_y})

    def __app_document_path(self):
        desired_caps = self.driver.session
        bundle_id = desired_caps["bundleId"]
        return "@" + bundle_id + ":documents/"

    def delete_folder_in_app_document(self, folder):
        current_time = time.time()
        path = self.__app_document_path() + folder
        try:
            self.driver.execute_script(
                "mobile:deleteFolder", {"remotePath": path})
        except:
            print("deleteFolder: Folder not exist: " + path)
        if self.DEBUG_PERFORMANCE:
            print("[%s] execution time = %s (s)" % (
                self.delete_folder_in_app_document.__name__, (time.time() - current_time)))

    def push_file_to_app_document(self, file_path):
        current_time = time.time()
        path = self.__app_document_path() + file_path
        self.driver.push_file(path, None, file_path)
        if self.DEBUG_PERFORMANCE:
            print("[%s] execution time = %s (s)" % (
                self.push_file_to_app_document.__name__, (time.time() - current_time)))

    def pull_file_from_app_document(self, file_path):
        current_time = time.time()
        path = self.__app_document_path() + file_path
        file = self.driver.pull_file(path)
        if self.DEBUG_PERFORMANCE:
            print("[%s] execution time = %s (s)" % (
                self.pull_file_from_app_document.__name__, (time.time() - current_time)))
        return file

    def pull_folder_from_app_document(self, file_path):
        current_time = time.time()
        path = self.__app_document_path() + file_path
        file = self.driver.pull_folder(path)
        if self.DEBUG_PERFORMANCE:
            print("[%s] execution time = %s (s)" % (
                self.pull_folder_from_app_document.__name__, (time.time() - current_time)))
        return file
