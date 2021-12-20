# Git Stalker

## Track and compare git histories of various window manager projects and their users

## Set up

I believe depending on your version of pip, you should be able to run one of the command
below and have all the necessary python packages installed.

```
# before 15.1.0
virtualenv --no-site-packages --distribute .env &&\
    source .env/bin/activate &&\
    pip install -r requirements.txt
```


```
# after deprecation of some arguments in 15.1.0
virtualenv .env && source .env/bin/activate && pip install -r requirements.txt
```

[source](https://stackoverflow.com/a/12657803)


## Motivation

I have been using window managers for nearly as long as I’ve been using Linux (just about 5 years now), and have recently renewed my interest in them.  I’ve been looking into either updating my current one or switching to a new one and I know most (if not all) of them are FOSS projects, and some of them influence each other.	

This made me wonder how much overlap there was between development on these projects.  Are there users contributing to multiple projects?  Which projects, which users, and which features?  This is mostly for my own curiosity at the moment, but I think it would be interesting to see this information because it could give insights into which window managers are familiar and which ones are different.


## Goals

In the final product I plan to be able to show commits of specific authors (the users can type in the email of the user, or the name, and filter the list by those commits).  I will provide the ability to map users to the projects they work on and visualize the git history of a project.  Both of these latter features will be programmed queries (i.e. not user input).


## Dataset

I plan to gather most of the data directly from the project repositories listed below (possibly more, but I’m not sure yet).  All but one of these projects are hosted on GitHub, and all are git repositories.  I will transfer the data to a csv file using git-log’s pretty printing functionality and a data parser.  I’ve limited my interest to tiling window managers (as opposed to compositing ones), and only ones that were written for the X-server (i.e. none of these would work on Windows, or on a Linux system that uses Wayland).

Specifically, I plan to gather the commit and parent hashes for each commit in the repo, the author names and emails, the time and dates of the commits, and the subject and body of each commit. I’ll also get the name of the window manager, and the name of it’s repository, but this information won’t be in the commit history so I’ll have to do that manually.

[AwesomeWM](https://github.com/awesomeWM/awesome) \
[DWM](https://git.suckless.org/dwm/) \
[Xmonad](https://github.com/xmonad/xmonad) \
[i3](https://github.com/i3/i3) \
[StumpWM](https://github.com/stumpwm/stumpwm) \
[Qtile](https://github.com/qtile/qtile) \
[Spectrwm](https://github.com/conformal/spectrwm)


## Tools

 - Language: I’m leaning toward Python for this project, though I might use Typescript instead to make an angular app for an easy gui.  I will also be relying on bash scripts to parse git-log’s output.
 - I’m hoping to find a 3rd party library that can visualize data like git histories.  I’d like to use that in my final project.  Preferably, I’d be able to display things using html, but maybe it might be more of a desktop app.  I still need to work this out.  
 - I will be using sqlite as my database because it is the only one I know and I think this project is small enough to work with it.


## Milestones
- [x] Week 1: download git histories, set up a database tables, parse git histories into database.
  - [x] Determine where pieces of information are stored in git objects
  - [x] Write (or find) scripts to parse git history
  - [x] Automate parsing of data and storing it in DB
- [ ] Week 2: Set up UI and be able to capture user input and display some basic information.
  - [x] Find a Python framework for GUIs
  - [ ] Set up a basic working gui
    - [ ] Display text
    - [ ] Output text
    - [ ] Take user input
- [ ] Week 3: Write sql queries and display them on UI
  - [ ] Display commit history of individual project
    - [ ] Visualize commit histories as a graph
    - [ ] Display info in table
  - [ ] Display commit history of individual user (across all projects)
    - [ ] Display info in table
  - [ ] Search for commits by commit message (user input)
  - [ ] Display who works on what projects (or, what users a project has)
- [ ] Week 4: Catch up on late work and add finishing touches to project
  - [ ] I assume I’ll be behind and will use this time to catch up
  - [ ] I also doubt my gui will look very good, so I’ll take this time to make it prettier