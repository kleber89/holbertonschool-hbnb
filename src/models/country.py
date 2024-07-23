"""
Country class
"""


class Country:
    """
    Country, This class does not inherit.

    Created to list and create the countries
    """

    name: str
    code: str

    def __init__(self, name: str, code: str, **kwargs) -> None:
        """
        Initializes a Country instance.
        """
        self.name = name
        self.code = code

    def __repr__(self) -> str:
        """
        String representation of the Country instance.
        """
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self) -> dict:
        """
        Dictionary representation of the Country instance.
        """
        return {
            "name": self.name,
            "code": self.code,
        }

    @staticmethod
    def get_all() -> list["Country"]:
        """
        Get all countries.
        """
        from src.persistence import repo

        return repo.get_all("country")

    @staticmethod
    def get(code: str) -> "Country | None":
        """
        Get a country by its code.
        """
        for country in Country.get_all():
            if country.code == code:
                return country
        return None

    @staticmethod
    def create(name: str, code: str) -> "Country":
        """
        Create a new country.
        """
        from src.persistence import repo

        country = Country(name, code)
        repo.save(country)
        return country
