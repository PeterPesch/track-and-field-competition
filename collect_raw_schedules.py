"""Collect raw time schedules from atletiek.nu."""


import sqlite3

from tfcompetition.competition_selector import CompetitionSelector
from tfcompetition.tfcompetition import TFCompetition
from tfcompetition.schedule.schedule_parser import ScheduleParser


def main():
    """Collect schedule tables to investigate the contents."""
    # Make sure that base tables exist.
    conn = sqlite3.connect('raw_schedule.db')
    curs = conn.cursor()
    curs.execute(
        '''
            CREATE TABLE if not exists competitions (
                comp_id         INTEGER,
                comp_name       TEXT
            );
        ''')
    curs.execute(
        '''
            CREATE TABLE if not exists schedules (
                comp_id         INTEGER,
                start_time      TEXT,
                time_link       TEXT,
                start_group     TEXT,
                group_link      TEXT,
                event           TEXT,
                event_link      TEXT,
                final_column    TEXT,
                final_link      TEXT
            );
        ''')
    # Select competitions.
    while True:
        # Let the user choose a competition.
        sel = CompetitionSelector(initialise=False)
        sel.select('Choose a competition (Enter to stop)')
        if sel.competition <= 0:
            print('Stopping collection of competitions.')
            conn.commit()
            conn.close()
            return
        # Show the name of the competition.
        competition = TFCompetition(sel.competition)
        parser = ScheduleParser(competition.schedule_url)
        if not parser.tree:
            continue
        print('{}: {}'.format(sel.competition, parser.name))
        # Insert or Update into the competition tables

        def row_generator():
            table = None
            try:
                table = parser.get_table()
            except IndexError:
                return
            for row in table.body.rows:
                yield(
                    int(sel.competition),
                    row.cells[0].string, row.cells[0].link,
                    row.cells[1].string, row.cells[1].link,
                    row.cells[2].string, row.cells[2].link,
                    row.cells[3].string, row.cells[3].link
                )

        curs.execute(
            '''
                SELECT comp_id FROM competitions
                WHERE comp_id = ?;
            ''',
            (int(sel.competition),))
        if curs.fetchone():
            print('Updating competition ...')
            curs.execute(
                '''
                    UPDATE competitions
                    SET comp_name = ?
                    WHERE comp_id = ?;
                ''',
                (parser.name, int(sel.competition)))
            curs.execute(
                '''
                    DELETE FROM schedules
                    WHERE comp_id = ?
                ''',
                (int(sel.competition),))
            curs.executemany(
                '''
                    INSERT INTO schedules (
                        comp_id, start_time, time_link,
                        start_group, group_link, event,
                        event_link, final_column, final_link)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                row_generator())
        else:
            print('Inserting competition ...')
            curs.execute(
                '''
                    INSERT INTO competitions (comp_id, comp_name)
                    VALUES (?, ?)
                ''',
                (int(sel.competition), parser.name))
            curs.executemany(
                '''
                    INSERT INTO schedules (
                        comp_id, start_time, time_link,
                        start_group, group_link, event,
                        event_link, final_column, final_link)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                row_generator())


if __name__ == '__main__':
    main()
