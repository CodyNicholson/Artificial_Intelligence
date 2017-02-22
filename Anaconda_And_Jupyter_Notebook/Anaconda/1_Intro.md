#Intro

Often you will be working with projects that require different dependencies/library versions, or even different versions of python

It's very difficult to get all of these versions to play nicely together on one computer

To solve this problem we use vitual environments to manage libraries, such as Virtualenv. Virtual environments let you separate libraries according to the project you are working on.

***

###Using Anaconda

Whenever you start a new project you should create a new anaconda environment using this command:

```
conda create -n envName python=3
```

This will create a development environment called "envName" (since we used the -n flag to name it)

To activate this environment in windows use the command:

```
source activate envName
```

This will load your development environment with all the dependencies you included within it

**To install new dependencies into your dev environment** make sure you have you are currently in the environment you wish to install dependencies for and then run the command:

```
conda install numpy pandas matplotlib
```

This will install those three dependencies into my current environment

**To view all of your dependencies** in your environment run the command:

```
conda list
```

***

###Anaconda Intro

Welcome to this lesson on using Anaconda to manage packages and environments for use with Python. With Anaconda, it's simple to install the packages you'll often use in data science work. You'll also use it to create virtual environments that make working on multiple projects much less mind-twisting. Anaconda has simplified my workflow and solved a lot of issues I had dealing with packages and multiple Python versions.

Anaconda is actually a distribution of software that comes with conda, Python, and over 150 scientific packages and their dependencies. The application conda is a package and environment manager. Anaconda is a fairly large download (~500 MB) because it comes with the most common data science packages in Python. If you don't need all the packages or need to conserve bandwidth or storage space, there is also Miniconda, a smaller distribution that includes only conda and Python. You can still install any of the available packages with conda, it just doesn't come with them.

Conda is a program you'll be using exclusively from the command line, so if you aren't comfortable using it, check out this command prompt tutorial for Windows or our Linux Command Line Basics course for OSX/Linux.

You probably already have Python installed and wonder why you need this at all. Firstly, since Anaconda comes with a bunch of data science packages, you'll be all set to start working with data. Secondly, using conda to manage your packages and environments will reduce future issues dealing with the various libraries you'll be using.

-

###Managing Packages

Package managers are used to install libraries and other software on your computer. You’re probably already familiar with pip, it’s the default package manager for Python libraries. Conda is similar to pip except that the available packages are focused around data science while pip is for general use. However, conda is not Python specific like pip is, it can also install non-Python packages. It is a package manager for any software stack. That being said, not all Python libraries are available from the Anaconda distribution and conda. You can (and will) still use pip alongside conda to install packages.

Conda installs precompiled packages. For example, the Anaconda distribution comes with Numpy, Scipy and Scikit-learn compiled with the MKL library, speeding up various math operations. The packages are maintained by contributors to the distribution which means they usually lag behind new releases. But because someone needed to build the packages for many systems, they tend to be more stable (and more convenient for you).

-

###Environments

Along with managing packages, Conda is also a virtual environment manager. It's similar to virtualenv and pyenv, other popular environment managers.

Environments allow you to separate and isolate the packages you are using for different projects. Often you’ll be working with code that depends on different versions of some library. For example, you could have code that uses new features in Numpy, or code that uses old features that have been removed. It’s practically impossible to have two versions of Numpy installed at once. Instead, you should make an environment for each version of Numpy then work in the appropriate environment for the project.

This issue also happens a lot when dealing with Python 2 and Python 3. You might be working with old code that doesn’t run in Python 3 and new code that doesn’t run in Python 2. Having both installed can lead to a lot of confusion and bugs. It’s much better to have separate environments.

You can also export the list of packages in an environment to a file, then include that file with your code. This allows other people to easily load all the dependencies for your code. Pip has similar functionality with **pip freeze > requirements.txt**.

***

###Making Sure Your Anaconda Is Updated

To get the latest updates in Anaconda run these commands:

```
conda upgrade conda
conda upgrade --all
```
