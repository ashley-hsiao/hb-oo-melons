"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """AbstractMelonOrder"""

    def __init__(self, species, qty, country_code, tax, order_type):
        """Initialize our abstract melon order"""
        
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type
        self.country_code = country_code

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        # Call dunder init of the superclasses of the current class and pass in parameters
        super(DomesticMelonOrder, self).__init__(species, qty, "US", 0.08, "domestic")
        # self.order_type = "domestic"
        # self.tax = 0.08

    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        # Call dunder init of the superclasses of the current class and pass in parameters
        super(InternationalMelonOrder, self).__init__(species, qty, country_code, 0.17, "international")

        #self.country_code = country_code
        # self.order_type = "international"
        # self.tax = 0.17

    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code
