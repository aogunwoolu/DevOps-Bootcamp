# create employee class
# docstrings
# field called raise_amount & initialise to 1.05
# constructor: firstname, lastname, pay

# property called email: firstname.lastname@email.com
# property called fullname: firstname lastname

# method called apply_raise: calculate the pay with the raise amount multiplied to it

class Employee:
    """
    meant to store information about a companies employees

    properties/attributes:
        - firstname
        - lastname
        - pay
        - raise amount
        - email
        - full name

    methods:
        - apply raise
    """

    def __init__(self, firstname:str, lastname:str, pay:int) -> None:
        self._firstname = firstname
        self._lastname = lastname
        self._pay = pay
        self.raise_amount = 1.05
    
    @property
    def email(self):
        """returns email property (generated email)"""

        return f"{self._firstname}.{self._lastname}@email.com"

    @property
    def fullname(self):
        """returns full name of employee"""

        return f"{self._firstname} {self._lastname}"

    def apply_raise(self):
        """
        calculates pay based upon the raise amount

        <pay> * <raise_amount>
        """

        return int(self._pay) * self.raise_amount

