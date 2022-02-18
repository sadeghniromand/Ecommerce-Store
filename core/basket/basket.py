class Basket:
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty_item):
        """
        Adding and updating the users basket session data
        """
        product_id = product.id
        if str(product_id) not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty_item)}
            self.session.modified = True
        else:
            self.basket[str(product_id)]['qty'] = qty_item + self.basket[str(product_id)]['qty']
            self.session.modified = True

    def __len__(self):
        return len(self.basket)

    def a(self):
        print(self.basket)
        return self.basket
