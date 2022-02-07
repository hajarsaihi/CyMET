# CyMET: Mass Cytometry Meta Analysis Pipeline

## Outline

This github repo includes `CyMET-py` which is a Python package for integrating mass cytometry data. The method is specifically trained for *whole blood* and *peripheral blood mononuclear cell* datasets. For detailed description on the algorithm, including the methods used, and both supervised (meta-prediction) and unsupervised (batch correction and clustering) biomedical applications, please refer to the [paper](https://www.biorxiv.org/content/10.1101/2021.12.03.471185v1).

This work is developed by Hajar Saihi (PhD) from [Bessant Lab](https://bezzlab.github.io/) @DERI Institute, QMUL.


## Getting Started
### Dependencies

For easy usage, we suggest builing a ```conda``` virtualenv with ```python = 3.8```.

```{bash}
conda create -n mario python=3.8
```

### Installing

To install ```MARIO```, we can easily install it with ```pip``` function (package name ```pyMARIO```):

```{bash}
python -m pip install pyMARIO
```


### Full tutorial:
For step by step tutorials on how to use ```MARIO```, with fine-tuned parameters for optimal results and full functionality, please refer to the documents we provided here:

[Python - Jupyter notebook: Match and Integration of Human Bonemarrow datasets](https://github.com/shuxiaoc/mario-py/blob/main/tutorials/mario-py-tutorial-BM.ipynb)

[Python - Jupyter notebook: Match and Integration of multiple Xspecies datasets](https://github.com/shuxiaoc/mario-py/blob/main/tutorials/mario-py-multiple-Xspecies.ipynb)

[R - Rmarkdown: Match and Integration of Human Bonemarrow datasets](https://github.com/shuxiaoc/mario-py/blob/main/tutorials/mario-r-bk.md)


## <img src="https://github.com/shuxiaoc/mario-py/blob/main/media/yellow.png" width="25" height="25"> License and Citation

```MARIO``` is under the [Academic Software License Agreement](https://github.com/shuxiaoc/mario-py/blob/main/LICENSE.txt), please use accordingly.
