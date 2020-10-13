"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def __init__(self, name, flavor, price, qty):
        
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0
        self.cache[name] = self # need to confirm 
    
    
    
    def add_stock(self,amount): # should we initialize amount with init? 
        self.qty += amount
    

    def sell(self,amount):
        # qty-amount= qty
        # if qty=0: print (" sorry , these cupcakes are sold out")
        # if qty<0 , qty=0
        
        #hey !!! do u want to continue working here along with class?

        self.qty -= amount
        if self.qty==0:
            print("sorry , these cupcakes are sold out")
        if self.qty<0:
            self.qty=0

    def scale_recipe(ingredients,amount):
        @staticmethod
        for i_name, qty in ingredients:
            return [(i_name,qty*amount)]
            
    
    def get(cls,name):
        @classmethod
        if name in cache:
            return cls.cache[name]
        else:
            print("sorry,that cupcake doesn't exist")

   


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
