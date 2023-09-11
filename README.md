# Waterloo Rocketry Software Onboarding

Welcome to the Waterloo Rocketry Software Subsystem!

This repository is intended as a guide to learning Git and GitHub for
new members who aren't familiar with these tools. It will be used as
part of the Git Tutorial and you can revisit it later if you forget
any steps of the process. After completing this onboarding task,
you'll have set up Git, created a commit and opened a PR!

## Part 1: Let's Git Started

**Objective**: Set up Git locally and clone this repository.

*Git* is a version control system (VCS) widely used for managing
software projects. Using Git, we can track the entire history of a
software project, easily integrate new changes, and restore old versions
of code if something goes wrong.

Of course to use Git, we first need to install Git. Head over to the
[Git website](https://git-scm.com/) and download the appropriate
installer for your operating system. Once the installer finishes
running, verify that everything worked by opening Git Bash (Windows)
or a terminal (macOS or Linux) and run the following command:
```
git --version
```
If you get a current version number (at the time of writing, 2.42) and
no errors, you're good to go!

You'll also need to create a GitHub account and add it to the Waterloo
Rocketry GitHub organization. Send your GitHub username to Ozayr, Kavin or 
Jack once you've created it and we'll make sure you get added!

Move to Part 2 once:
- You have Git installed
- You have a local clone of this repository
- You've made a GitHub account and sent your username to an admin

## Part 2: Install Dependencies

**Objective**: Install Python and the needed dependencies.

First, we need to install Python itself. Everyone can install from the 
[official website](https://www.python.org/downloads/) and this is the 
recommended way for Windows users. For macOS users, the recommended way 
is to install [Homebrew](https://brew.sh/) and then install Python using 
`brew install python`. If you use Linux, I'm assuming you already have 
Python or can figure out how to install it yourself. In all cases, we 
want to install the latest version (at the time of writing, *3.11*).

In most cases, working on a Python project means installing dependencies
using `pip`. Pip is a tool for installing Python packages - software
libraries that other people have written and made available for you to
use. Pip already comes pre-installed with Python, so you don't need to
install anything extra.

Before running any Python commands, we want to make sure we use the 
right major version of Python (Python 2 and Python 3 are very different
and not compatible with each other). Run the following command in your 
terminal/shell:
```
python --version
```
If the version is Python 3.XX, you're good to go. If it's Python 2.XX
or you get an error, all python commands you run must be in the format
`python3 some-command` and not `python some-command` as you will see
in the rest of this tutorial. This also goes for pip (use `pip3` rather
than `pip`).

To install the dependencies specified in `requirements.txt`, run the 
following command:
```
pip install -r requirements.txt
```

Move to Part 3 once:
- You have Python installed
- You have installed all dependencies

## Part 3: Making a Change

**Objective**: Add a new function to `functions.py`.

It's time to actually write some code! Start by adding a new function to
`functions.py`. You can take inspiration from the functions that are
already there, or get creative. Just make sure your function will be
easily unit-testable (it should have well-defined inputs and outputs).
Please also add a [docstring](https://www.datacamp.com/community/tutorials/docstrings-python)
to your function; this is a comment that provides useful information
about what your function does, what arguments it takes, and what values
it returns. All of the functions in `functions.py` should already have
docstrings, so you should be able to just follow the existing format.

This repository also has an automatic formatting script, located in the
`tools` folder. It uses autopep8 to deal with nitpicky formatting things
like extra newlines and whitespace floating around. To use it, run
`./format.sh` from the root of the repository - you'll generally want to 
do this before each commit, or at least before making pull requests.

Move to Part 4 once:
- You've added a new function to `functions.py`
- You've run the formatting script

## Part 4: Commitment Issues

**Objective**: Add your new changes to the repository history.

_Committing_ a change means saving it permanently in the history of the
repository. Once something's been committed, it's very hard to delete
accidentally - even if it changes further later on, we can almost always
go back in time and restore old versions if we need to.

In Git, a _branch_ represents a version of the repository that's
somehow different from the main `master` branch. Usually, new features
will be developed, committed to feature branches, and then _merged_
back into `master`. This keeps the history cleaner and makes it easier
to review changes before they're made.

The following command will show you all the branches in your local
repo and the asterisk shows which you're currently on:
```
git branch
```

Create a new branch and switch to it by running:
```
git branch <branch-name>
git checkout <branch-name>
```

This will carry over your changes to the new branch. Normally, you
would create and switch to the new branch before you start making changes.
A shorter way to create and switch is `git checkout -b <branch-name>`.

Once you're done making changes, you can _stage_ them by running:
```
git add .
```
Run this from the root directory of the repo and it will stage all files
that were added, modified or deleted. You can also add specific files 
by running `git add <filename>` if you don't want to stage all of them.

Once you've staged the files you want to commit, run the following 
command to commit them:
```
git commit -m "<commit-message>"
```

Even though this is a small change, make sure you write a good commit
message! On this team, we try to follow the guidelines [here](https://chris.beams.io/posts/git-commit/).

Move to Part 5 once:
- You've created a new branch for your feature
- You've committed your code to the new branch

## Part 5: Pulling a Fast One

**Objective**: Open a pull request and merge your changes to the main
repository.

By committing your change, you've stored it in the local history of the
repository on your feature branch, but you haven't yet uploaded the
change to GitHub or merged it to the `master` branch.

The first step is to _push_ a copy of your local branch up to GitHub.
You can do this very easily by running the following command, replacing
`branch_name` with the actual name of your branch:
```
git push -u origin <branch-name>
```

Once the first push has been made, Git maps your local branch to
the remote branch on GitHub and you can just use `git push`.

If you want to read more about Git pushing, checkout out Chapter
[3.5](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches) of
the Git book.

Now that GitHub has a copy of your branch, you can open a _pull request_
(PR), which is a way of proposing new changes for merging. The people
running the Git Tutorial wil walk you through the process of opening
a PR and requesting reviews. Other people on the team can then take a 
look at your code and request changes if they have any concerns. After
everyone is happy, your PR will be approved and you can merge it into
the _base_ branch (usually master).

You've completed this tutorial once:
- You've pushed your local changes to a remote branch and opened a pull
request
- You've had your pull request reviewed and have addressed any review
comments
- You've merged your pull request into the `master` branch

## What Now?

Once you've merged your pull request, you're officially done with
software onboarding. Welcome to the team!

Git is a very powerful and complicated software, and there are a lot of
things that weren't covered in this onboarding. If you need a refresher or
want to learn some more advanced features, the Internet is your friend. 
Here are some great resources that might help you get started:
- A great resource I used is this [lecture)](https://missing.csail.mit.edu/2020/version-control/) 
in MIT's Missing Semester class. It walks you through the underlying 
structure of Git and some basic commands.
- If you like learning interactively, try [Git-It](https://github.com/jlord/git-it-electron).
- Another interactive option is [Learn Git Branching](https://learngitbranching.js.org).
It's not as comprehensive as Git-It, but it runs in your browser and
might be easier to get started with.
- If you're a bit more adventurous, you can refer directly to the Git
documentation. Chapter [1.5](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
will show you how to install Git, and Chapter [2.1](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
has information on how to "clone" an existing repository.

