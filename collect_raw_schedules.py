"""Collect raw time schedules from atletiek.nu."""


from tfcompetition.competition_selector import CompetitionSelector
from tfcompetition.tfcompetition import TFCompetition
from tfcompetition.schedule_parser import ScheduleParser


def main():
    """Perform the demonstration."""
    while True:
        # Let the user choose a competition.
        sel = CompetitionSelector(initialise=False)
        sel.select('Choose a competition (Enter to stop)')
        #print('Competition ID:', sel.competition)
        if sel.competition <= 0:
            print('Stopping collection of competitions.')
            return
        # Show the name of the competition.
        competition = TFCompetition(sel.competition)
        parser = ScheduleParser(competition.schedule_url)
        if parser.name:
            print('{}: {}'.format(sel.competition, parser.name))


if __name__ == '__main__':
    main()
