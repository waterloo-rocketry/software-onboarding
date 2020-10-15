# Waterloo Rocketry Software Onboarding

Welcome to the Waterloo Rocketry Software Subteam!

This repository is intended to be a starting point for new team members
who aren't necessarily familiar with software tools and practices like
Git, GitHub, pull requests, and unit testing. If you're already familiar
with all of those concepts, it probably won't take too long for you to
work through this tutorial. If you haven't heard of or worked with one
or more of those, or you just need a refresher, take as much time as you
like! The purpose of this repository is to provide an environment where
you can experiment with and learn these tools without needing to learn
everything about our team and our rocket at the same time.

This tutorial is structured around a very small Python library called
`sandbox`. By the end of the tutorial, you'll have added a new feature
to `sandbox`, added a *unit test* to make sure that it works, and
contributed your changes with a *pull request*.

The Internet is full of great resources for learning all of these
concepts, and we won't try to replicate all of them - so, instead of
giving step-by-step instructions for each part of the tutorial, we
focus on sharing resources that are much more comprehensive and
in-depth. We want you to be able to pick and choose whichever resource
you prefer and learn however you learn best.

## Part I: Let's Git Started

**Objective**: Set up Git locally and clone this repository.

*Git* is a version control system (VCS) widely used for managing
software projects. Using Git, we can track the entire history of a
software project, easily integrate new changes, and restore old versions
of code if something goes wrong.

The goal of this stage is to install Git and get familiar with the basic
tools for inspecting a _repository_ ("repo" for short).

There are a lot of good resources available for learning Git. You might
find the following helpful:
- If you like learning interactively, try [Git-It](https://github.com/jlord/git-it-electron).
This interactive tutorial will take you through Git and GitHub basics;
it will teach you everything you need to know for parts
[I](#part-i-let's-git-started), [IV](#part-iv-commitment-issues), and
[V](#part-v-pulling-a-fast-one) of this tutorial.
- Another interactive option is [Learn Git Branching](https://learngitbranching.js.org).
It's not as comprehensive as Git-It, but it runs in your browser and
might be easier to get started with.
- If you're a bit more adventurous, you can refer directly to the Git
documentation. Chapter [1.5](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
will show you how to install Git, and Chapter [2.1](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
has information on how to "clone" an existing repository.

You'll also need to create a GitHub account and add it to the Waterloo
Rocketry GitHub organization. Send your GitHub username to us (Wendi,
Jacob, or Dawson) once you've created it and we'll make sure you get
added!

Move to Part II once:
- You have Git installed
- You have a local clone of this repository
- You've made a GitHub account and sent your username to an admin

## Part II: It's Testing Time

**Objective**: Install the `sandbox` dependencies and run the unit
tests.

`sandbox` is a tiny Python library that we've created as a testing
ground for this tutorial. In order to get started, you'll need to
install Python on your computer. If you already have Python installed,
great! Otherwise, you can get it [here](https://www.python.org/downloads/).
We recommend installing Python 3.7 or later to ensure compatibility with
all of our different projects.

In most cases, working on a Python project means installing dependencies
using `pip`. Pip is a tool for installing Python packages - software
libraries that other people have written and made available for you to
use. Pip already comes pre-installed with Python, so you don't need to
install anything extra.

For `sandbox`, we only have one dependency: `pytest`, the tool we
use to test the code. Run these two commands in your terminal while
inside this directory to complete the installation process:
```
pip install -U -r requirements.txt
pip install -U -e .
```
If you're using a Mac, run these commands instead:
```
pip3 install -U -r requirements.txt
pip3 install -U -e .
```
The first line installs all of the libraries from the `requirements.txt`
file; you can open that file and take a look to see what is being
installed. The second line installs `sandbox`, so that Python knows
where to look for the code.

Now that we have our library installed, let's run some tests to make
sure that it works. A _unit test_ is a small snippet of code that
_tests_ some other _unit_ of code - that is, it makes sure that your
code does what it's supposed to do. For example, a unit test for the
`square_root` function might confirm that `square_root(100)` returns
`10`. The `sandbox` unit tests can be found in the
`sandbox/tests/test_sandbox.py` file.

For now, start by running the `pytest` command in your terminal. You
should see pytest automatically detect and run all of the unit tests in
the repository, and they should all pass. If any of them fail, something
is very wrong and should be addressed before moving on - try
troubleshooting yourself, but let us know if you're not sure what the
issue is.

Move to Part III once:
- You have Python installed
- You've installed the `pytest` dependency
- You've installed `sandbox` as a local repository
- You've successfully run the `sandbox` unit tests (and they pass)

## Part III: Making a Change

**Objective**: Add a new feature to `sandbox` and a new test for the new
feature.

It's time to actually write some code! Start by adding a new function to
`sandbox.py`. You can take inspiration from the functions that are
already there, or get creative. Just make sure your function will be
easily unit-testable (it should have well-defined inputs and outputs).
Please also add a [docstring](https://www.datacamp.com/community/tutorials/docstrings-python)
to your function; this is a comment that provides useful information
about what your function does, what arguments it takes, and what values
it returns. All of the functions in `sandbox.py` should already have
docstrings, so you should be able to just follow the existing format.

Next, write a unit test for your new function and add it to
`test_sandbox.py`. Again, follow the examples that are already there.
Make sure that your function name starts with `test_`, or pytest won't
be able to detect it!

Finally, run the unit tests with `pytest` and make sure that your new
test both runs and passes. If it fails or doesn't run, you've done
something wrong; take another look at the code and try to troubleshoot.

Move to Part IV once:
- You've added a new function to `sandbox.py`
- You've added a new unit test for your function to `test_sandbox.py`
- The new unit test passes

## Part IV: Commitment Issues

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

If you've gone through the Git-It tutorial, you should already be
familiar with how to create a branch and make a commit. Chapters
[3.1](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) and
[2.2](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
of the Git book also have a more comprehensive overview.

Even though this is a small change, make sure you write a good commit
message! On this team, we try to follow the guidelines [here](https://chris.beams.io/posts/git-commit/).

Move to Part V once:
- You've created a new branch for your feature
- You've committed your code to the new branch

## Part V: Pulling a Fast One

**Objective**: Open a pull request and merge your changes to the main
repository.

By committing your change, you've stored it in the local history of the
repository on your feature branch, but you haven't yet uploaded the
change to GitHub or merged it to the `master` branch.

The first step is to _push_ a copy of your local branch up to GitHub.
You can do this very easily by running the following command, replacing
`branch_name` with the actual name of your branch:
```
git push -u origin branch_name
```
If you want to read more about Git pushing, checkout out Chapter
[3.5](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches) of
the Git book.

Now that GitHub has a copy of your branch, you can open a _pull request_
(PR), which is a way of proposing new changes for merging. Again, if
you've gone through the Git-It tutorials, you already know how to open a
PR; otherwise, you can follow the GitHub tutorial
[here](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

Once you've opened the PR, [request a review](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/requesting-a-pull-request-review)
from `OnboardingReviewers`. We'll take a look at the PR and let you know
if there's anything to change - and once we think it's ready, we'll
approve it and get your change merged into `master`.

You've completed this tutorial once:
- You've pushed your local changes to a remote branch and opened a pull
request
- You've had your pull request reviewed and have addressed any review
comments
- You've merged your pull request into the `master` branch

## What Now?

Once you've merged your pull request, you're officially done with
software onboarding! Whenever you're ready to get started, take a look
at our [good first issues](https://github.com/issues?q=is%3Aissue+user%3Awaterloo-rocketry+is%3Aopen+no%3Aassignee+label%3A"good+first+issue")
and let the software leads know that you're looking for work. Welcome to
the team!
