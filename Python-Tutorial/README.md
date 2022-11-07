# Python Setup Tutorial

Python is a popular programming and scripting language widely used in a variety of different fields. It is also a major language used in Waterloo Rocketry.

This tutorial will teach you how to get started with setting up Python 3 in your local environment from a clean slate.
Specifically, the coverage includes the installation of `python` as well as the package manager `pip` and the environment.

This tutorial will cover Windows, MacOS, and Linux.

## Part I: Setup

### Windows

#### Preamble:
If you already have Python 2 installed, you will still need to follow this guide. You will, however, need to run `python3` and `pip3` in cmd, to differentiate from Python 2.

#### General Steps:
First, go to the [official python website](https://www.python.org/downloads/windows) to download the installer.

Then, run the installer with "Install Now" option to install the standard package of Python, including pip. Alternatively, you can also check out the customized options below.

Afterwards, add the path to your Python installation into Environment Variables. The default path, should you choose "Install Now", is inside
`C:\Users\<your_user>\AppData\Local\Programs\Python\<Python_version>`.

Finally, verify the installation by running `python` on cmd.

#### Customized Installer Options
You may choose to customize your install options such as documentation, customized PATH, etc.

We highly recommend that you install documentation and pip, as these tools will be quite useful.
![alt-text](https://journaldev.nyc3.digitaloceanspaces.com/2019/06/customize_installation.png)
![alt-text](https://journaldev.nyc3.digitaloceanspaces.com/2019/06/optional_features-1.png)
![alt-text](https://journaldev.nyc3.digitaloceanspaces.com/2019/06/advanced_options.png)

#### Environment Variables
In Windows, the `Path` variable is frequently used to find the location of language interpreters. This is no exception for python. Without setting up an Environment Variable, the OS would not know where Python is, thus unable to run Python.

If you have checked the Environment Variable box during installation, you can skip this step.

To set up your Environment Variable, simply search for `Environment Variables` in your Windows search bar. Select the system suggested option, and you should see a similar window as below.
![alt-text](https://journaldev.nyc3.digitaloceanspaces.com/2019/06/environmentalvar_to-path.png)

Edit the `Path` variable by adding the following. Change the added path shown in the picture below to your installation location and hit OK. Each entry is separated by a semicolon.
![alt-text](https://journaldev.nyc3.digitaloceanspaces.com/2019/06/config_envvar_new-1.png)

#### Verification
If you installed Python and set up the environment variable correctly, you should be able to run the command `python` on Command Prompt as below.
![alt-text](https://journaldev.nyc3.digitaloceanspaces.com/2019/06/verify-python-cmdpromt.png)

Additionally, you can also run `pip` to verify that the Python package manager Pip is also working.

### MacOS

#### Preamble
The existing Python installation on your Mac is likely Python 2.7, which means it is likely incompatible with newer Python 3 code, as Python 2 is now deprecated. Therefore, you will need to install Python 3.

While you can set up Python 3 by running the installer (similar to Windows, see above). However, we recommend you install by command line.

If you have homebrew set up already, you can follow this guide to setup Python 3 and Pip directly from homebrew [here](https://docs.python-guide.org/starting/install3/osx/).

#### Python Installation
You can check your python version by running `$ python --version` or `$ python3 --version` on Terminal. If either command shows a Python 3 installation, then you already have Python 3 installed. You can similarly check for `pip` and `pip3`.

Alernatively, if you are greeted with this message on Terminal, then click on the install button and follow the steps. It is recommended to install the command line developer tools alongside Python 3.

```xcode-select: note: no developer tools were found at '/Applications/Xcode.app', requesting install. Choose an option in the dialog to download the command line developer tools.```

After installing, you can rerun the command above to verify your installation.

#### Pip Installation

Simply run this command on your Terminal and swap `python` with `python3` if applicable:

`curl https://bootstrap.pypa.io/get-pip.py | python`

Your pip should be installed after this command is ran. You may call `pip` or `pip3` to verify it.

### Linux

You should be using command line to install Python. Similar to MacOS, `python3` and `pip3` may be used if you already have Python 2.

In addition, many distributions have Python 3 already installed. You can verify by running `$ python --version`.

In general, your installation command should be in the form of `$ sudo <package manager> install python3 `, e.g., for Ubuntu, `$ sudo apt-get install python3`.

Additionally, you can run `$ sudo <package manager> install python3-pip` to install pip.

# Part II: Package Installation and Virtual Environment
If you do not yet have `pip` or `pip3` as valid commands, please refer back to Part I to install Python3 and pip. Additonally, make sure you are calling Python3/Pip3 in your command. `python3` and `pip3` may be used instead where applicable.

In general, the command to install a python package globally via pip is as follows:

```$ pip install <pkg name>```

However, given the differences in packages used across projects, you should use a Virtual Environment if possible.

To set up a virtual environment, we need to first navigate to the project via `$ cd <project path>`. Then, under the main directory of the project, run `$ python -m venv venv` to generate a virtual environment.

Then, on Windows, run `$ venv\Scripts\activate`; on MacOS and Linux, run `$ source venv/bin/activate`. You should see `(venv)` on the left side of your command line if you succeeded.

Afterwards, you can install Python dependencies with `$ pip install -r requirements.txt`. If you get a permissions error, try `$ pip install --user -r requirements.txt` instead. Follow the README on your project for more specific setup details.
