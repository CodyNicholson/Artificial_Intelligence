#Managing Packages

Once you have Anaconda installed, managing packages is fairly straightforward. To install a package, type **conda install package_name** in your terminal. For example, to install numpy, type **conda install numpy**.

You can install multiple packages at the same time. Something like **conda install numpy scipy pandas** will install all those packages simultaneously. It's also possible to specify which version of a package you want by adding the version number such as **conda install numpy=1.10**.

Conda also automatically installs dependencies for you. For example scipy depends on numpy, it uses and requires numpy. If you install just scipy (conda install scipy), Conda will also install numpy if it isn't already installed.

Most of the commands are pretty intuitive. To uninstall, use **conda remove package_name**. To update a package **conda update package_name**. If you want to update all packages in an environment, which is often useful, use **conda update --all**. And finally, to list installed packages, it's **conda list** which you've seen before.

If you don't know the exact name of the package you're looking for, you can try searching with **conda search search_term**. For example, I know I want to install Beautiful Soup, but I'm not sure of the exact package name. So, I try **conda search beautifulsoup**.

It searches for beautifulsoup

It returns a list of the Beautiful Soup packages available with the appropriate package name, **beautifulsoup4**.
