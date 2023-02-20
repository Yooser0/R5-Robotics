# R5 Robotics Spring 2023

If this is your first time cloning this repository, follow these steps to get started quickly.

1. Download python. This is the language the source code will be written in.
1. Download pip, a python package manager that will be used to install a library for the Tello drone.
1. Install djitellopy, a python package that makes it easier to code for the Tello drone.
1. If you don't have an IDE yet, it is highly recommended for a smoother coding experience.
1. Install git. This is needed to access this repository. In some cases, git can be installed alongside an IDE.

Do these steps in order as they depend on each other in most cases.

## Downloading Python
Open your respective operating system's terminal and enter `python3 --version` to check if you have python.
### Windows
Download the latest version of python via the Microsoft Store.
### MacOS
Download the latest version of python from their official website: https://www.python.org/downloads/macos/
### Linux
Use your distro-specific package manager to install python. For example: `sudo apt-get install python` or `sudo dnf install python`.

## Downloading pip
Open your respective operating system's terminal and enter `pip3 --version` to check if you have pip.
### Windows
Open the command prompt and navigate to the directory you want to use to install python in. To do this, use `dir` to list the folders and files in your current directory, and `cd <folder name>` to enter into a sub-folder. Now enter this command: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`. get-pip.py is now installed in your current directory. Now enter `python3 get-pip.py`. If you don't get an error, pip is succesfully installed.
### MacOS
Opne the command line and navigate to the directory you want to use to install python in. To do this, use `ls` to list the directories and files in your current directory, and `cd <directory name>` to enter into a sub-directory. Now enter this command: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`. get-pip.py is now installed in your current directory. Now enter `python3 get-pip.py`. If you don't get an error, pip is succesfully installed.
### Linux
Use your distro-specific package manager to install pip. For example: `sudo apt-get install pip` or `sudo dnf install pip`.

## Installing djitellopy
Open your respective operating system's terminal. Enter `pip3 install djitellopy`.

## Get an IDE
### Windows
VSCode is recommended for its versatility in all programming languages and its ability to easily download extensions that makes programming easier and more efficient. Go to VSCode's official webisite: https://code.visualstudio.com/. Click "Download for Windows", and run the executable. Click next until "Select Additional Tasks", where you should select everything in "Other". Skip through everything else and install.
### MacOS
MacOS contains a specialized IDE called "Xcode" that comes built-in with git. Just download Xcode off the Mac App Store.
### Linux
Use your distro-specific package manager to install VSCode. For example: `sudo apt-get install code` or `sudo dnf install code`.

## Installing git
Open your respective operating system's terminal and enter `git --version` to check if you have git. This may not apply for MacOS, as you may have it through Xcode.
### Windows
Go to the official git website: https://git-scm.com/download/win. Download a "Standalone Installer" version and run it. In the "Select Components" page, select at least "Add a Git Bash Profile to Windows Terminal". In "Choosing the default editor used by Git", choose Notepad if you're inexperienced using the command prompt. Skip through everything else and install.
### MacOS
Install git through Xcode, detailed in "Get an IDE", or use homebrew and enter in the terminal: `brew install git`. Homebrew is more general and can be used instead.
### Linux
Use your distro-specific package manager to install pip. For example: `sudo apt-get install pip` or `sudo dnf install pip`

## Cloning the repository
Create a new folder to clone this repository in and navigate to it through your respective operating system's terminal. Now enter `git clone https://github.com/Yooser0/R5-Robotics.git`. You can also get this link by clicking on the green button that says "Code" at the top right of this github page. You now have access to the code!
