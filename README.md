# Track and Field Competitions
> Temporary work-arounds for missing features in atletiek.nu

This project consists of tools that can be used to (temporarily) emulate features I need whcih have not (or not yet) been implemented into atletiek.nu.
Atletiek.nu is the site on which all track-and-field-competitions in The Netherlands are to be managed. (Competitions which are managed outside of this system are required to upload their results to this site.)

Over the past few years I have frequently run into missing features.
As a rule it's quite tricky to build temporary workarounds for using this site, and I found that I appear to be reusing (and rewriting) parts of code from previous workarounds.

In this project, I'm trying to make the software reusable.

> Number of Athletes

The first workaround I want to (re)create is a small tool which quickly shows me the number of athletes for each field event. I can use that information to make an educated guess of the time needed for that event. (For track events, the time needed usually depends on the number of series rather than the number of athletes.)

## Installing / Getting started

The project uses Python 3.

A list of External Packages used within this project is being maintained in document "External_Packages_Used.md".


```shell
pip install beautifulsoup4
```

After installing these external packages, all import statements in the project should be working.

### Initial Configuration

At this moment, no additional initial configuration is necessary.

## Developing

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
pip install beautifulsoup4

git clone https://github.com/PeterPesch/track-and-field-competition.git
cd track-and-field-competition/
```

Make sure you add a demo_*.py module to show what your addition does.

### Building

No additional steps are needed by the developer to build the
project.

### Deploying / Publishing

This project does not need to be published on a server.

