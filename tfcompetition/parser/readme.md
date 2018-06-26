# Subpackage parser contains baseclasses for objects which parse HTML pages into some data structure.

These base objects are meant to extract data which exists in all (or many) different pages.

Also, if parsers need extra external packages for technical reasons, that part should be handled here (preferably in a new base class which should be a child of Parser).

> Parser

This is the generic base class for all parsers in this proect.