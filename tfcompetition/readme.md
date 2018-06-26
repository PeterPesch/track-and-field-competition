# Main folder of Package tfcompetition

This package handles information about Track and Field competitions, as read from the atletiek.nu site.

The package is meant as a base for building temporary workarounds for feautures which have not yet been implemented by atletiek.nu .

This folder contains 3 modules:
- tfcompetition
- competition_selector
- utils

> tfcompetition

This module handles t&f competitions.

It contains 1 object:
- TFCompetition: Implements a t&f competition

> competition_selector

This module handles user input for selecting a t&f competition.

It contains 1 object:
- CompetitionSelector: Lets the user input a link to a t&f competition on atletiek.nu (or a cmpetitionID)

> utils

This module contains several functions which are used within package tfcompetition.

It contains the following functions:

UI functions:
- int_from_prompt(prompt): Return an integer as answer to a prompt, or -1 if no input is given

HTML parsing functions:
- tag_has_class(tag, cls): Returns True if the tag has class cls.
- string_from_tag(tag): Returns a string representation from the tag.
- first_string_from_tag(tag): Returns the first string representation from the tag.
- combined_string_from_tag(tag): Retursn a combined string representation from the tag.
- combined_content_from_tag(tag): Returns the combined content from the tag.
- find_table(tree, classname=None, headerclass=None): Returns the tag from the first table which compies to the conditions.

Business rules for identification of t&f events:
- get_event(event): Isolate the name of the event from the full event string.
- is_relay_event(event): Returns True if event is a relay event.
- is_running_event(event): Returns True if event is a running event.
- is_jumping_event(event): Returns True if event is a jumping event.
- is_throwing_event(event): Returns True if event is a throwing event.

Functions for sorting:
- eventsort_key(eventname): Returns a sorting key for event names which makes sense in Track and Field.
- schedulesort_key(schedule_item): Return a sorting key for timeschedule items which makes sense in Track and Field.