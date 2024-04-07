class Country:
    """
    Base Class
    """

    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population

    def get_info(self):
        info = {
            "name": self.name,
            "capital": self.capital,
            "population": self.population,
        }

        return info


# Test
country1 = Country(name="Jamaica", capital="Kingston", population=2800000)
print(country1.get_info())
