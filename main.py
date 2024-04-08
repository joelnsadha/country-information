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


class World:
    def __init__(self):
        self.countries = []

    def add_country(self, country):
        self.countries.append(country)

    def get_counry_info(self, country):
        for c in self.countries:
            if c.name == country:
                return c.get_info()
        return None


################################################################
# Test
################################################################

# Create world instance to hold all countries
world1 = World()

# Create country instance
usa = DevelopedCountry(
    name="USA", capital="Washington", population=315000000, gdp=25000000000000
)

# Create country instance
uganda = DevelopingCountry(
    name="Uganda", capital="Kampala", population=47000000, hdi=0.55
)

# Add countries to world class
world1.add_country(usa)
world1.add_country(uganda)

# Search for country
country_info = world1.get_counry_info("USA")

if country_info:
    print({"Country Info": country_info})
    for key, value in country_info.items():
        print(f"{key}:{value}")
    else:
        print("Country not found")
