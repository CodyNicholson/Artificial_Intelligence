#Creating a slideshow

Create slideshows from notebooks is one of my favorite features. You can see [an example of a slideshow here](http://nbviewer.jupyter.org/format/slides/github/jorisvandenbossche/2015-PyDataParis/blob/master/pandas_introduction.ipynb#/) introducing Pandas for working with data.

The slides are created in notebooks like normal, but you'll need to designate which cells are slides and the type of slide the cell will be. In the menu bar, click View > Cell Toolbar > Slideshow to bring up the slide cell menu on each cell.

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/58339359_slides-cell-toolbar-menu/slides-cell-toolbar-menu.png)

Turning on Slideshow toolbars for cells

This will show a menu dropdown on each cell that lets you choose how the cell shows up in the slideshow.

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5833938f_slides-choose-slide-type/slides-choose-slide-type.png)

Choose slide type

**Slides** are full slides that you move through left to right. **Sub-slides** show up in the slideshow by pressing up or down. **Fragments** are hidden at first, then appear with a button press. You can skip cells in the slideshow with **Skip** and **Notes** leaves the cell as speaker notes.

***

###Running the slideshow

To create the slideshow from the notebook file, you'll need to use **nbconvert**:

```
jupyter nbconvert notebook.ipynb --to slides
```

This just converts the notebook to the necessary files for the slideshow, but you need to serve it with an HTTP server to actually see the presentation.

To convert it and immediately see it, use

```
jupyter nbconvert notebook.ipynb --to slides --post serve
```

This will open up the slideshow in your browser so you can present it.
