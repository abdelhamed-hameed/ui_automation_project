class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.product_title = page.locator(".title")
        self.add_to_cart_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_count = page.locator(".shopping_cart_badge")

    def is_loaded(self):
        self.page.wait_for_selector(".title")
        return True

    def add_backpack_to_cart(self):
        self.add_to_cart_button.click()

    def get_cart_count(self):
        return self.cart_count.text_content()