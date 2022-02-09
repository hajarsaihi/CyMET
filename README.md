# CyMET 
Mass **Cy**tometry **Met**a Analysis Pipeline

## Outline

This github repo includes `CyMET-py` which is a Python package for integrating mass cytometry data. The method is specifically trained for *whole blood* and *peripheral blood mononuclear cell* datasets. For detailed description on the algorithm, including the methods used, and both supervised (meta-prediction) and unsupervised (batch correction and clustering) biomedical applications, please refer to the [paper](https://www.biorxiv.org).

This work is developed by Hajar Saihi (PhD) based at the [Alazawi Lab](https://www.qmul.ac.uk/blizard/all-staff/profiles/william-alazawi.html) @BlizardInstitute and [Bessant Lab](https://bezzlab.github.io/) @DERI at Queen Mary University of London.

![alt text](https://github.com/startswithH/CyMET/blob/main/images/pipeline_outline.png)


## Getting Started
### Dependencies

For easy usage, we suggest builing a ```conda``` virtualenv with ```python = 3.8```.

```{bash}
conda create -n cymet python=3.8
```

### Installing

To install ```CyMET```, we can easily install it with ```pip``` function (package name ```pyCyMET```):

```{bash}
python -m pip install pyCyMET
```


### Full tutorial:
For step by step tutorials on how to use ```CyMET```, with fine-tuned parameters for optimal results and full functionality, please refer to the documents we provided here:

[Python - Jupyter notebook: Meta-prediction of immune cells](https://github.com/startswithH/CyMET/blob/main/tutorials/Immunopred%20Prediction.ipynb)

[Python - Jupyter notebook: CyMET on COVID-19 data](https://github.com/startswithH/CyMET/blob/main/tutorials/CyMET%20on%20COVID-19.ipynb)

## License and Citation

```CyMET``` is under the [Academic Software License Agreement](https://github.com/startswithH/CyMET/blob/main/LICENSE.md), please use accordingly.
