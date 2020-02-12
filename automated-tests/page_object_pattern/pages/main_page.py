class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = '.search_query'
        self.product_faded_short_tshirt = 'Faded Short Sleeve T-shirts'

    def action_on_page(self):
        self.driver.find_element_by_link_text(self.product_faded_short_tshirt).click()
