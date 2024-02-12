## jupyter
### links
```
[Udacity's home page](https://www.udacity.com)
```
### emphasis
```
**aardvark** or __aardvark__
```
### magic keywords
* interactive matplotlib
```
%matplotlib # valid for one line
%%matplotlib # valid for whole cell
%matplotlib inline #embedding visualization in notebookds
%config InlineBackend.figure_format = 'retina' # config figure in jupyter
```
* timing code
```
%%timeit
```
* load sql extension: ipython-sql
```
%load_ext sql
```

### debugging
```
%pdb
```
### convert
```
jupyter nbconvert --to FORMAT mynotebook.ipynb
jupyter nbconvert notebook.ipynb --to slides --post serve
```
### helper
```
h.simulate_data?
```
