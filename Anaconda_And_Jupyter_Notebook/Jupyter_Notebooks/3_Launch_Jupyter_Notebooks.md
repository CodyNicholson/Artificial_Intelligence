#Launching the notebook server

To start a notebook server, enter **jupyter notebook** in your terminal or console. This will start the server in the directory you ran the command in. That means any notebook files will be saved in that directory. Typically you'd want to start the server in the directory where your notebooks live. However, you can navigate through your file system to where the notebooks are.

When you run the command (try it yourself!), the server home should open in your browser. By default, the notebook server runs at http://localhost:8888. If you aren't familiar with this, **localhost** means your computer and **8888** is the port the server is communicating on. As long as the server is still running, you can always come back to it by going to http://localhost:8888 in your browser.

If you start another server, it'll try to use port 8888, but since it is occupied, the new server will run on port 8889. Then, you'd connect to it at http://localhost:8889. Every additional notebook server will increment the port number like this.

If you tried starting your own server, it should look something like this:

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5818e181_notebook-server/notebook-server.png)

You might see some files and folders in the list here, it depends on where you started the server from.

Over on the right, you can click on "New" to create a new notebook, text file, folder, or terminal. The list under "Notebooks" shows the kernels you have installed. Here I'm running the server in a Python 3 environment, so I have a Python 3 kernel available. You might see Python 2 here. I've also installed kernels for Scala 2.10 and 2.11 which you see in the list.

If you run a Jupyter notebook server from a conda environment, you'll also be able to choose a kernel from any of the other environments (see below). To create a new notebook, click on the kernel you want to use.

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/584739ab_conda-environments/conda-environments.png)

conda environments in Jupyter

The tabs at the top show Files, Running, and Cluster. Files shows all the files and folders in the current directory. Clicking on the Running tab will list all the currently running notebooks. From there you can manage them.

Clusters previously was where you'd create multiple kernels for use in parallel computing. Now that's been taken over by ipyparallel (https://ipyparallel.readthedocs.io/en/latest/intro.html) so there isn't much to do there.

If you're running the notebook server from a conda environment, you'll also have access to a "Conda" tab shown below. Here you can manage your environments from within Jupyter. You can create new environments, install packages, update packages, export environments and more.

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58473bf5_conda-tab/conda-tab.png)

conda tab in Jupyter

***

###Shutting down Jupyter

You can shutdown individual notebooks by marking the checkbox next to the notebook on the server home and clicking "Shutdown." Make sure you've saved your work before you do this though! Any changes since the last time you saved will be lost. You'll also need to rerun the code the next time you run the notebook.

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58474142_notebook-shutdown/notebook-shutdown.png)

You can shutdown the entire server by pressing control + C twice in the terminal. Again, this will immediately shutdown all the running notebooks, so make sure your work is saved!

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58474185_server-shutdown/server-shutdown.png)
