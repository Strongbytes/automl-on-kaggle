Here's what you need in order to attend this workshop:

* Make sure you've registered for the [event](https://www.eventbrite.com/e/global-ai-nights-iasi-by-strongbytes-tickets-67751515607)
* Clone this repository somewhere nice
* Create a [Kaggle](https://www.kaggle.com) account, join the [Titanic competition](https://www.kaggle.com/c/titanic/overview) competition, download its data files to the [data](./data) folder
* Make sure you have an [Azure](https://azure.microsoft.com/en-us/) account with enough credits (~20 EUR should be fine). If that's not the case, contact @vladiliescu for an [Azure Pass](https://www.microsoftazurepass.com)
* Install either [Miniconda](https://conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/downloads). The Python 3.7 version 🐍.
* Run the following commands inside this directory

```console
conda env create -f env.yml -n ainights_sep_2019
conda activate ainights_sep_2019
ipython kernel install --user

jupyter notebook
```
* If everything runs fine and at the end you can open the `auto-ml-and-kaggle.ipynb` notebook then congrats, you've conquered this challenge 🥳
* If something fails,  let @vladiliescu or @dotnet18 know about it and they'll help you out

See you at the workshop! 
