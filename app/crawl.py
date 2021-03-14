from selenium import webdriver
import time


class Crawl:
    def __init__(self):
        self.site = "https://rewordify.com/"
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(-10000, 0)

    def get_simplified_text(self, text):
        self.driver.get(self.site)
        inputElement = self.driver.find_element_by_id("wtext")
        inputElement.send_keys(text)
        inputElement.submit()
        time.sleep(1)

        output = self.driver.find_elements_by_id("tab1content")
        result = output[0].text.split("\n")[0]
        return result


# if __name__ == "__main__":
#     test = Crawl()
#     print(test.get_simplified_text(
#         "Large areas of landscape can be covered many metres deep in peat"))
