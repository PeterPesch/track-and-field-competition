"""Defines a Track and Field Competition."""


from urllib.parse import urljoin


class TFCompetition(object):
    """Defines a Track and Field Competition."""

    base_url = 'https://www.atletiek.nu/wedstrijd/chronoloog/'

    def __init__(self, competition_id):
        """Initialise the object."""
        self.competition_id = competition_id

    @property
    def schedule_url(self):
        """Return the url of the 'Tijdschema' page on Atletiek.nu."""
        url = urljoin(TFCompetition.base_url, str(self.competition_id))
        return url
