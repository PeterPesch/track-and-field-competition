"""Show the number_of_athletes functionality of the TF Competition package."""


from tfcompetition.competition_selector import CompetitionSelector
from tfcompetition.tfcompetition import TFCompetition
from tfcompetition.schedule_parser import ScheduleParser


def main():
    """Perform the demonstration."""
    # Let the user choose the competition.
    sel = CompetitionSelector(initialise=False)
    sel.select()
    print('Competition ID:', sel.competition)
    if sel.competition <= 0:
        print('No valid competition chosen!')
        return
    # Show (part of) the time schedule.
    competition = TFCompetition(sel.competition)
    print('Schedule Page:', competition.schedule_url)
    parser = ScheduleParser(competition.schedule_url)
    print('Schedule Name:', parser.name)
    print('Schedule Title:', parser.title)
    try:
        table = parser.get_table('chronoloogtabel')
    except IndexError as e:
        print(e.args[0])
        return
    for row in table.header.rows:
        print(row.string)
    for row in table.body.rows:
        print(row.string, row.link)


if __name__ == '__main__':
    main()
