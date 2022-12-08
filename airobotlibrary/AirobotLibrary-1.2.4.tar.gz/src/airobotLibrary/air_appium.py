from AppiumLibrary import AppiumLibrary
from airobots.core.settings import ST
from airtest import aircv
from airobots.core.api import G
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import allure
import traceback
import base64
import time


class AirAppium(AppiumLibrary):
    def __init__(self, timeout=5):
        super(AirAppium, self).__init__(timeout=timeout)

    @allure.step
    def open_application(self, remote_url=ST.REMOTE_URL, alias=None, platformName=ST.PLATFORM_NAME, **kwargs):
        kwargs['platformName'] = platformName
        desired_caps = kwargs
        application = webdriver.Remote(str(remote_url), desired_caps)

        self._debug('Opened application with session id %s' % application.session_id)

        self.driver = application
        self.driver.home = self.home
        self.driver.snapshot = self.snapshot
        self.driver.text = self.text
        self.driver.air_keyevent = self.driver.keyevent
        self.driver.keyevent = self.air_keyevent
        self.driver.double_click = self.double_click
        self.driver.click = self.touch
        self.driver.touch = self.touch
        self.driver.wake = self.wake
        self.driver.uninstall_app = self.uninstall_app
        self.driver.clear_app = self.clear_app
        self.driver.stop_app = self.stop_app
        self.driver.start_app = self.start_app
        self.driver.shell = self.shell
        self.driver.air_swipe = self.driver.swipe
        self.driver.pinch = self.air_pinch
        self.driver.zoom = self.air_zoom
        self.driver.swipe = self.air_swipe
        self.driver.get_current_resolution = self.get_current_resolution
        G.add_device(self.driver)
        return self._cache.register(application, alias)

    @allure.step
    def close_application(self):
        return super(AirAppium, self).close_application()

    @allure.step
    def close_all_applications(self):
        return super(AirAppium, self).close_all_applications()

    @allure.step
    def switch_application(self, index_or_alias):
        return super(AirAppium, self).switch_application(index_or_alias=index_or_alias)

    @allure.step
    def switch_to_context(self, context_name):
        return super(AirAppium, self).switch_to_context(context_name=context_name)

    @allure.step
    def go_back(self):
        return super(AirAppium, self).go_back()

    @allure.step
    def press_keycode(self, keycode, metastate=None):
        return super(AirAppium, self).press_keycode(keycode=keycode, metastate=metastate)

    @allure.step
    def scroll(self, start_locator, end_locator):
        return super(AirAppium, self).scroll(start_locator=start_locator, end_locator=end_locator)
    
    @allure.step
    def scroll_down(self, locator):
        return super(AirAppium, self).scroll_down(locator=locator)

    @allure.step
    def scroll_up(self, locator):
        return super(AirAppium, self).scroll_up(locator=locator)

    @allure.step
    def click_a_point(self, x=0, y=0, duration=100):
        return super(AirAppium, self).click_a_point(x=x, y=y, duration=duration)

    @allure.step
    def click_element(self, locator):
        return super(AirAppium, self).click_element(locator=locator)

    @allure.step
    def click_button(self, index_or_name):
        return super(AirAppium, self).click_button(index_or_name=index_or_name)

    @allure.step
    def click_text(self, text, exact_match=False):
        return super(AirAppium, self).click_text(text=text, exact_match=exact_match)

    @allure.step
    def long_press(self, locator, duration=1000):
        return super(AirAppium, self).long_press(locator=locator, duration=duration)

    @allure.step
    def long_press_keycode(self, keycode, metastate=None):
        return super(AirAppium, self).long_press_keycode(keycode=keycode, metastate=metastate)

    @allure.step
    def input_text(self, locator, text):
        return super(AirAppium, self).input_text(locator=locator, text=text)

    @allure.step
    def input_password(self, locator, text):
        return super(AirAppium, self).input_password(locator=locator, text=text)

    @allure.step
    def input_value(self, locator, text):
        return super(AirAppium, self).input_value(locator=locator, text=text)

    @allure.step
    def install_app(self, app_path, app_package):
        return super(AirAppium, self).install_app(app_path=app_path, app_package=app_package)

    @allure.step
    def shake(self):
        return super(AirAppium, self).shake()

    @allure.step
    def swipe(self, start_x, start_y, offset_x, offset_y, duration=1000):
        return super(AirAppium, self).swipe(start_x=start_x, start_y=start_y, offset_x=offset_x, offset_y=offset_y, duration=duration)

    @allure.step
    def tap(self, locator, x_offset=None, y_offset=None, count=1):
        return super(AirAppium, self).tap(locator=locator, x_offset=x_offset, y_offset=y_offset, count=count)

    @allure.step
    def touch_id(self, match=True):
        return super(AirAppium, self).touch_id(match=match)

    @allure.step
    def pinch(self, locator, percent="200%", steps=1):
        return super(AirAppium, self).pinch(locator=locator, percent=percent, steps=steps)

    @allure.step
    def zoom(self, locator, percent="200%", steps=1):
        return super(AirAppium, self).zoom(locator=locator, percent=percent, steps=steps)

    @allure.step
    def page_should_contain_text(self, text, loglevel='INFO'):
        return super(AirAppium, self).page_should_contain_text(text=text, loglevel=loglevel)

    @allure.step
    def page_should_contain_element(self, locator, loglevel='INFO'):
        return super(AirAppium, self).page_should_contain_element(locator=locator, loglevel=loglevel)

    @allure.step
    def page_should_not_contain_element(self, locator, loglevel='INFO'):
        return super(AirAppium, self).page_should_not_contain_element(locator=locator, loglevel=loglevel)
    
    @allure.step
    def page_should_not_contain_text(self, text, loglevel='INFO'):
        return super(AirAppium, self).page_should_not_contain_text(text=text, loglevel=loglevel)

    @allure.step
    def text_should_be_visible(self, text, exact_match=False, loglevel='INFO'):
        return super(AirAppium, self).text_should_be_visible(text=text, exact_match=exact_match, loglevel=loglevel)

    @allure.step
    def element_text_should_be(self, locator, expected, message=''):
        return super(AirAppium, self).element_text_should_be(locator=locator, expected=expected, message=message)

    @allure.step
    def element_value_should_be(self, locator, expected):
        return super(AirAppium, self).element_value_should_be(locator=locator, expected=expected)

    @allure.step
    def element_should_be_visible(self, locator, loglevel='INFO'):
        return super(AirAppium, self).element_should_be_visible(locator=locator, loglevel=loglevel)

    @allure.step
    def element_should_be_enabled(self, locator, loglevel='INFO'):
        return super(AirAppium, self).element_should_be_enabled(locator=locator, loglevel=loglevel)

    @allure.step
    def element_should_be_disabled(self, locator, loglevel='INFO'):
        return super(AirAppium, self).element_should_be_disabled(locator=locator, loglevel=loglevel)

    @allure.step
    def element_should_not_contain_text(self, locator, expected, message=''):
        return super(AirAppium, self).element_should_not_contain_text(locator=locator, expected=expected, message=message)

    @allure.step
    def element_should_contain_text(self, locator, expected, message=''):
        return super(AirAppium, self).element_should_contain_text(locator=locator, expected=expected, message=message)

    @allure.step
    def capture_page_screenshot(self, filename=None):
        file = super(AirAppium, self).capture_page_screenshot(filename=filename)
        with open(file, 'rb') as fp:
            allure.attach(fp.read(), '截图{}'.format(filename or ''), allure.attachment_type.PNG)
        return file

    def _get_log_dir(self):
        return ST.LOG_DIR

    def _run_on_failure(self):
        if self._run_on_failure_keyword is None:
            return
        if self._running_on_failure_routine:
            return
        self._running_on_failure_routine = True
        try:
            file = self.driver.get_screenshot_as_base64()
            allure.attach(base64.b64decode(file), '异常截图', allure.attachment_type.PNG)
        except Exception as err:
            self._run_on_failure_error(err)
        finally:
            self._running_on_failure_routine = False

    def _click_element_by_name(self, name):
        driver = self._current_application()
        try:
            element = driver.find_element_by_name(name)
        except Exception as e:
            raise e

        try:
            element.click()
        except Exception as e:
            raise Exception('Cannot click the element with name "%s"' % name)

    def _find_element_by_class_name(self, class_name, index_or_name):
        elements = self._find_elements_by_class_name(class_name)

        if self._is_index(index_or_name):
            try:
                index = int(index_or_name.split('=')[-1])
                element = elements[index]
            except (IndexError, TypeError):
                raise Exception('Cannot find the element with index "%s"' % index_or_name)
        else:
            found = False
            for element in elements:
                self._info("'%s'." % element.text)
                if element.text == index_or_name:
                    found = True
                    break
            if not found:
                raise Exception('Cannot find the element with name "%s"' % index_or_name)

        return element

    def _click_element_by_class_name(self, class_name, index_or_name):
        element = self._find_element_by_class_name(class_name, index_or_name)
        self._info("Clicking element '%s'." % element.text)
        try:
            element.click()
        except Exception as e:
            raise Exception('Cannot click the %s element "%s"' % (class_name, index_or_name))

    def _element_input_text_by_class_name(self, class_name, index_or_name, text):
        try:
            element = self._find_element_by_class_name(class_name, index_or_name)
        except Exception as e:
            raise e

        self._info("input text in element as '%s'." % element.text)
        try:
            element.send_keys(text)
        except Exception as e:
            raise Exception('Cannot input text "%s" for the %s element "%s"' % (text, class_name, index_or_name))

    def home(self):
        if self._is_ios():
            return self.driver.press_button("home")
        elif self._is_android():
            return self.driver.press_keycode(3)
        else:
            raise Exception('Unsupport this keyword')

    def snapshot(self, filename=None, strType=False, quality=10, max_size=None, **kwargs):
        if self._is_ios() or self._is_android():
            value = self.driver.get_screenshot_as_base64()
            data = base64.b64decode(value)
            if strType:
                if filename:
                    with open(filename, 'wb') as f:
                        f.write(data)
                return data
            # output cv2 object
            try:
                screen = aircv.utils.string_2_img(data)
            except:
                # may be black/locked screen or other reason, print exc for debugging
                traceback.print_exc()
                return None

            # save as file if needed
            if filename:
                aircv.imwrite(filename, screen, quality, max_size=max_size)
            return screen
        else:
            raise Exception('Unsupport this keyword')

    def text(self, text, enter=True, locator=None, **kwargs):
        if locator is not None:
            if enter:
                text += '\n'
            element = self._element_find(locator, True, True)
            ActionChains(self.driver).send_keys_to_element(element, text).perform()
        else:
            raise Exception('Unsupport this keyword')

    def air_keyevent(self, keyname, **kwargs):
        if self._is_ios():
            return self.driver.press_button(keyname)
        elif self._is_android():
            self.shell("input keyevent {}".format(keyname.upper()))
        else:
            raise Exception('Unsupport this keyword')

    def double_click(self, pos):
        if self._is_ios() or self._is_android():
            self.touch(pos)
            time.sleep(0.05)
            self.touch(pos)
        else:
            raise Exception('Unsupport this keyword')

    def touch(self, pos, duration=0, **kwargs):
        if not isinstance(pos, (list, tuple)):
            raise Exception('params pos is must be tuple or list, but pos is {}'.format(type(pos)))
        if self._is_ios() or self._is_android():
            self.click_a_point(x=pos[0], y=pos[1], duration=duration*1000)
        else:
            raise Exception('Unsupport this keyword')

    def wake(self):
        if self._is_ios() or self._is_android():
            self.home()
        else:
            raise Exception('Unsupport this keyword')

    def uninstall_app(self, package):
        if self._is_ios() or self._is_android():
            self.driver.remove_app(package)
        else:
            raise Exception('Unsupport this keyword')

    def clear_app(self, package):
        if self._is_ios() or self._is_android():
            self.stop_app(package)
            self.start_app(package)
        else:
            raise Exception('Unsupport this keyword')

    def stop_app(self, package):
        if self._is_ios() or self._is_android():
            self.driver.terminate_app(package)
        else:
            raise Exception('Unsupport this keyword')

    def start_app(self, package, activity=None):
        if self._is_ios() or self._is_android():
            self.driver.activate_app(package)
        else:
            raise Exception('Unsupport this keyword')

    def shell(self, cmd):
        if self._is_android():
            self.execute_adb_shell(cmd)
        else:
            raise Exception('Unsupport this keyword')

    def air_pinch(self, center=None, percent=0.5, duration=0.05, steps=1, in_or_out='in', element=None, **kwargs):
        x, y = cx, cy = (0, 0)
        if element:
            element_location = element.location
            x, y = element_location.get('x'), element_location.get('y')
        if isinstance(center, (list, tuple)): cx, cy = center 
        width, height = self.get_current_resolution()
        if x == y == cx == cy == 0: x, y = width/2, height/2
        elif cx and cy: x, y = cx, cy
        p1x, p1y = width*0.2, y
        p2x, p2y = width*0.8, y
        p1 = TouchAction(self.driver)
        p2 = TouchAction(self.driver)
        if in_or_out == 'out':
            p1.press(x=x, y=y).wait(500).move_to(x=p1x, y=p1y).wait(duration*1000).release()
            p2.press(x=x, y=y).wait(500).move_to(x=p2x, y=p2y).wait(duration*1000).release()
        else:
            p1.press(x=p1x, y=p1y).wait(500).move_to(x=x, y=y).wait(duration*1000).release()
            p2.press(x=p2x, y=p2y).wait(500).move_to(x=x, y=y).wait(duration*1000).release()
        for _ in range(steps):
            ma = MultiAction(self.driver)
            ma.add(p1, p2)
            ma.perform()

    def air_zoom(self, element, percent="200%", steps=1):
        element_location = element.location
        x, y = element_location.get('x'), element_location.get('y')
        width, height = self.get_current_resolution()
        if x == y == 0: x, y = width/2, height/2
        p1x, p1y = width*0.2, y
        p2x, p2y = width*0.8, y
        p1 = TouchAction(self.driver)
        p2 = TouchAction(self.driver)
        p1.press(x=x, y=y).wait(500).move_to(x=p1x, y=p1y).wait(50).release()
        p2.press(x=x, y=y).wait(500).move_to(x=p2x, y=p2y).wait(50).release()
        for _ in range(steps):
            ma = MultiAction(self.driver)
            ma.add(p1, p2)
            ma.perform()

    def air_swipe(self, start_x=None, start_y=None, offset_x=None, offset_y=None, duration=0.1, **kwargs):
        if self._is_ios() or self._is_android():
            if isinstance(start_x, (list, tuple)):
                duration = float(duration) * 1000
                offset_x = start_y and start_y[0]
                offset_y = start_y and start_y[1]
                start_y = start_x[1]
                start_x = start_x[0]
            self.driver.air_swipe(start_x=start_x, start_y=start_y, end_x=offset_x, end_y=offset_y, duration=duration, **kwargs)
        else:
            raise Exception('Unsupport this keyword')

    def get_current_resolution(self):
        size = self.driver.get_window_size()
        return size.get('width'), size.get('height')
