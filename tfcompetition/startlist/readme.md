# Subpackage startlist

Subpackage Startlist handles track&field start lists.

It contains two modules:
- startlist
- startlist_parser

> startlist

This module implements track&field start lists.

It contains 2 main Objects:
- StartList: Implements a t&f start list, consiting of startlist items
- Item: Base object for implementing t&f startlist items. An Item might be a:
  - Athlete: Implements a line in a t&f time schedule describing an athlete in a scheduled event
  - EmptyLane: Implements a line in a t&f time schedule describing an empty lane in a heat of a scheduled running event
  - Heat: Implements a line in a t&f time schedule describing a heat of a scheduled running event

> startlist_parser

This module implements a parser which creates a t&f StartList object.

It contains 1 main object:
- StartlistParser(Parser): Extracts a t&f StartList object from a page on atletiek.nu