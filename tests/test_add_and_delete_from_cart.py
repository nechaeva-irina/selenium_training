def test_add_and_delete_from_cart(app):
    app.main_page.open_main_page()
    for i in range(0,3):
        app.main_page.select_item()
        app.item_page.add_item()
    app.item_page.checkout()
    app.cart_page.remove_all_items()
    assert app.cart_page.final_message() == 'There are no items in your cart.'
