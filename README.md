Here's what you need in order to run this notebook:

* Clone this repository somewhere nice
* Create a [Kaggle](https://www.kaggle.com) account, join the [Titanic competition](https://www.kaggle.com/c/titanic/overview) competition, download its data files to the [data](./data) folder
* Make sure you have an [Azure](https://azure.microsoft.com/en-us/) account with enough credits (~20 EUR should be fine).
* Install either [Miniconda](https://conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/downloads). The Python 3.7 version 🐍
* Run the following commands inside this directory from the Conda prompt

```shell
conda env create -f env.yml -n automl_on_titanic
conda activate automl_on_titanic
pip install --user ipykernel

ipython kernel install --user --name=automl_on_titanic

jupyter notebook
```
* If everything runs fine and at the end you can open the `auto-ml-and-kaggle.ipynb` notebook then congrats, you've conquered this challenge 🥳
* If something fails, let [@vladiliescu](https://github.com/vladiliescu) or [@dotnet18](https://github.com/dotnet18) know about it and they'll help you out
