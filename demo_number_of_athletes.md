# Demo Number of Athletes

The first work-around that I needed was some tool to quickly see the number of athletes for each Field event, or the number of athletes for each Track Event.
I can use those numbers to make an educated guess of the time needed for that scheduled event.

To count the number of athletes, I would need to access either the startlist page or the results page (if they exist).

As my main purpose is estimation, I decided to implement the Startlist object (in the new startlist subpackage). Resulting counts should somehow be available in the schedule Item object (that is the Item object in the Schedule subpackage).

> Description of the demo

The demo lets the user choose a Track and Field competition:
- You can enter a link to a page on atletiek.nu which contains a specific t&f competition
- Alternatively, you could enter the cmpetition ID directly

The demo will try to load the time schedule of the competition.

The demo will try to find find out if the time schedule contains:
- relay events
- other running events
- jumping events
- throwing events

Please note that the demo will throw an exception whenever it encounters an event it doesn't understand!

The demo will let the user choose an event type.
- If the user chooses an event type:
  - The program will show the events of that type. and let the user choose
    - As long as the user chooses one of the events, the program will try to print the startlist of that event.

Finally, the program will show the items on the startlist for the chosen event type (or for all even types, in cade the user didn't choose a specific event type).
For each event, it will try to give an estimation of the size (number of athletes for fiels events, number of hetas for track events).