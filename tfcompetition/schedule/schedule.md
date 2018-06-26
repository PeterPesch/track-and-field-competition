# Subpackage schedule

Subpackage schedule handles track&field Time Schedules.

It contains two modules:
- schedule
- schedule_parser

> schedule

This module implements track&field Time Schedules.

It contains 2 main Objects:
- Schedule: Implements a t&f time Schedule, consisting of t&f time schedule Items
- Item: Implements an item on a t&f time schedule

> schedule_parser

This module implements a parser which creates a t&f time Schedule object.

It contains 1 main object:
- ScheduleParser(Parser): Extracts a t&f time Schedule object from a page on atletiek.nu