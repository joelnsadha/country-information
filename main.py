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


class DevelopedCountry(Country):
    """_Child Class of Country_

    Args:
        Country (_Object_): _Stores information about a country_
    """

    def __init__(self, name, capital, population, gdp):
        super().__init__(name, capital, population)
        self.gdp = gdp

    def get_info(self):
        info = super().get_info()
        info["gdp"] = self.gdp
        return info


class DevelopingCountry(Country):
    """_Child class of Country_

    Args:
        Country (_Object_): _Stores information about a country_
    """

    def __init__(self, name, capital, population, hdi):
        super().__init__(name, capital, population)
        self.hdi = hdi

    def get_info(self):
        info = super().get_info()
        info["hdi"] = self.hdi
        return info


# Test
country1 = DevelopedCountry(
    name="USA", capital="Washington", population=315000000, gdp=25000000000000
)

country2 = DevelopingCountry(
    name="Uganda", capital="Kampala", population=47000000, hdi=0.55
)
print(country2.get_info())
