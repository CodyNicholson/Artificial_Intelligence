#Converting notebooks

Notebooks are just big [JSON](http://www.json.org/) files with the extension **.ipynb**.

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5833887b_notebook-json/notebook-json.png)

Notebook file opened in a text editor shows JSON data

Since notebooks are JSON, it is simple to convert them to other formats. Jupyter comes with a utility called **nbconvert** for converting to HTML, Markdown, slideshows, etc.

For example, to convert a notebook to an HTML file, in your terminal use

```
jupyter nbconvert --to html notebook.ipynb
```

Converting to HTML is useful for sharing your notebooks with others who aren't using notebooks. Markdown is great for including a notebook in blogs and other text editors that accept Markdown formatting.

![alt tag](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/58338a48_nbconvert-example/nbconvert-example.png)

As always, learn more about **nbconvert** from the [documentation](https://nbconvert.readthedocs.io/en/latest/usage.html).
