# CyMET 
Mass **Cy**tometry **Met**a Analysis Pipeline using deep learning

## Outline

This github repo includes `CyMET` which is a Python package for integrating mass cytometry data. The method is specifically trained for *whole blood* and *peripheral blood mononuclear cell* datasets. For detailed description on the algorithm, including the methods used, and both supervised (cell identification) and unsupervised (batch correction and clustering) biomedical applications, please refer to the [paper](https://www.biorxiv.org).

This work is developed by Hajar Saihi (PhD) based at the [Alazawi Lab](https://www.qmul.ac.uk/blizard/all-staff/profiles/william-alazawi.html) @BlizardInstitute and [Bessant Lab](https://bezzlab.github.io/) @DERI at Queen Mary University of London.

![alt text](https://github.com/startswithH/CyMET/blob/main/images/summary_figure.png)


### Full tutorial:
For step by step tutorials on how to use ```CyMET```, with fine-tuned parameters for optimal results and full functionality, please refer to the documents we provided here:

(1) The first notebook allows for fully automated identification of immune cells using Immunopred. This notebook takes pre-cleaned csv files with markers as the columns and events as the rows and outputs the identified cell type for each event.

[Python - Jupyter notebook: Identification of immune cells](https://github.com/startswithH/CyMET/blob/main/tutorials/Immunopred%20Prediction.ipynb)

(2) The notebook below integrates both batch correction and clustering methods for supervised and unsupervised identification of cells. The quality of the results depends on the overlap in markers between studies.

[Python - Jupyter notebook: CyMET on COVID-19 data](https://github.com/startswithH/CyMET/blob/main/tutorials/CyMET%20on%20COVID-19.ipynb)

## License and Citation

```CyMET``` is under the [Academic Software License Agreement](https://github.com/startswithH/CyMET/blob/main/LICENSE.md), please use accordingly.
