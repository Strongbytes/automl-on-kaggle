Here's what you need in order to attend this workshop:

* Make sure you've registered for the [event](https://www.eventbrite.com/e/global-ai-bootcamp-2019-iasi-tickets-83532779793)
* Clone this repository somewhere nice
* Create a [Kaggle](https://www.kaggle.com) account, join the [Petfinder competition](https://www.kaggle.com/c/petfinder-adoption-prediction) competition, download its data files to the [data](./data) folder(s)
* Make sure you have an [Azure](https://azure.microsoft.com/en-us/) account with enough credits (~20 EUR should be fine). If that's not the case, contact [@vladiliescu](https://github.com/vladiliescu) for an [Azure Pass](https://www.microsoftazurepass.com)
* Install either [Miniconda](https://conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/downloads). The Python 3.7 version 🐍
* Run the following commands inside this directory

```shell
conda env create -f env.yml -n aibootcamp_2019
conda activate aibootcamp_2019
python -m ipykernel install --user --name=aibootcamp_2019

jupyter lab
```
* If something fails, let [@vladiliescu](https://github.com/vladiliescu) or [@dotnet18](https://github.com/dotnet18) know about it and they'll help you out

See you at the bootcamp! 
