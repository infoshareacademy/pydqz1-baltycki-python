from selenium.webdriver.common.by import By


class CommonPageLocators:
    PAGE_LOGO = (By.CSS_SELECTOR, '#header_logo')
    SEARCH_BAR = (By.CSS_SELECTOR, '#search_query_top')
    SEARCH_GO_BUTTON = (By.CSS_SELECTOR, 'button[name="submit_search"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[name="Submit"]')
    CART_AJAX_EMPTY = (By.CSS_SELECTOR, '.ajax_cart_no_product')
    PRODUCT_FADED_TSHIRTS = (By.CSS_SELECTOR, '#homefeatured .product-container a[title="Faded Short Sleeve T-shirts"]')
    PRODUCT_PRINTED_DRESS = (By.CSS_SELECTOR, '#homefeatured .product-container a[title="Printed Chiffon Dress"]')
    PRODUCT_SUMMER_DRESS = (By.CSS_SELECTOR, '.product-image-container a[title="Printed Summer Dress"]')
    PRODUCT_BLOUSE = (By.CSS_SELECTOR, '.product-container a[title="Blouse"]')
    PRODUCT_QUICKVIEW = (By.CSS_SELECTOR, '.fancybox-iframe')
    PRODUCT_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add_to_cart button[type="submit"]')
    PRODUCT_QUICKVIEW_ADD_QTY = (By.CSS_SELECTOR, '.icon-plus')
    PRODUCT_SIZE_DROPX_L = (By.XPATH, '//select[@name="group_1"]/option[text()="L"]')
    PRODUCT_COLOR_BLUE = (By.CSS_SELECTOR, 'a[name="Blue"]')
    PRODUCT_COLOR_ORANGE = (By.CSS_SELECTOR, 'a[name="Orange"]')
    PRODUCT_COLOR_WHITE = (By.CSS_SELECTOR, 'a[name="White"]')
    CART_LAYER_PROCEED_BUTTON = (By.CSS_SELECTOR, 'a[title="Proceed to checkout"]')
    CART_LAYER_CONTINUE_BUTTON = (By.CSS_SELECTOR, '.continue')
    CART_LAYER_TOTAL_PRODUCTS = (By.CSS_SELECTOR, '.ajax_block_products_total')
    PRODUCT_HOVER_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#homefeatured a[data-id-product="7"]')
    PRODUCT_HOVER_MORE_BUTTON = (By.CSS_SELECTOR, '.button-container \
    a[href="http://automationpractice.com/index.php?id_product=5&controller=product"]')
    MENU_WOMEN = (By.CSS_SELECTOR, 'a[title="Women"]')
    MENU_WOMEN_DRESSES = (By.CSS_SELECTOR, '.submenu-container a[title="Dresses"]')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '#quantity_wanted')

