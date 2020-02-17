from selenium.webdriver.common.by import By


class CommonPageLocators:
    PAGE_LOGO = (By.CSS_SELECTOR, '#header_logo')
    SEARCH_BAR = (By.CSS_SELECTOR, '#search_query_top')
    SEARCH_GO_BUTTON = (By.CSS_SELECTOR, 'button[name="submit_search"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[name="Submit"]')
    PRODUCT_FADED_TSHIRTS = (By.CSS_SELECTOR, '#homefeatured .product-container a[title="Faded Short Sleeve T-shirts"]')
    PRODUCT_QUICKVIEW = (By.CSS_SELECTOR, '.fancybox-iframe')
    PRODUCT_QUICKVIEW_CART_BUTTON = (By.CSS_SELECTOR, '#add_to_cart button[type="submit"]')
    PRODUCT_QUICKVIEW_ADD_QTY = (By.CSS_SELECTOR, '.icon-plus')
    PRODUCT_QUICKVIEW_SIZE_DROPX_L = (By.XPATH, '//select[@name="group_1"]/option[text()="L"]')
    PRODUCT_QUICKVIEW_COLOR_BLUE = (By.CSS_SELECTOR, 'a[name="Blue"]')
    CART_LAYER_PROCEED_BUTTON = (By.CSS_SELECTOR, 'a[title="Proceed to checkout"]')
    CART_LAYER_CONTINUE_BUTTON = (By.CSS_SELECTOR, '.continue')

