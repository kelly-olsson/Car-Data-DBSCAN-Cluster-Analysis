# Car Data Analysis and Clustering

## Overview
This repository contains all the necessary components for conducting a thorough Exploratory Data Analysis (EDA) and running advanced clustering algorithms using DBSCAN. It includes Jupyter notebooks for visualizations, datasets for analysis, and the model itself.

## Data Usage
The data used in this project belongs to [Loja Contectada](https://www.lojaconectada.com.br/) and is not available for use without permission. To inquire about usage of the data, please contact Paulo Henrique [@phsantosjr ](https://github.com/phsantosjr).

## Code
The source code in this repository is open and freely available for use, modification, and distribution under the MIT License. See the `LICENSE` file for more details.

## Repository Structure
- **notebooks/**: Contains Jupyter notebooks used in the analysis.
  - `Exploratory_Data_Analysis.ipynb` - Visualizations and summaries of the dataset.
  - `Model_Training.ipynb` - Code for training the DBSCAN clustering algorithm.
- **data/**:
  - **raw/** - Original dataset.
    - `data.csv` - Original dataset used with Loja Conectada data.
  - **processed/** - Processed datasets including clustering results (see `Model_Training.ipynb` for detailed notes on each file).
  - **mock/** - Mock data and scripts for generating simulation data.
- **models/**:
  - `dbscan_model.pkl` - Serialized DBSCAN model ready for new data.

## Getting Started
### Prerequisites
- Python 3.8+
- Jupyter Notebook 
- Google Colab (strongly recommended for running `Model_training.ipynb`)
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scipy`
  - `sklearn`
  - `statsmodels` (for statistical models and tests)
  - `kneed` (for knee point detection in curves)
  - `gower` (for Gower distance computation)

### Installation
Clone this repository and install the required Python libraries (for Unix/MacOS operating systems, please consult your own OS's relevant documentation):
```bash
git clone [repository-url]
cd car-data-DBSCAN-Cluster-Analysis
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
NOTE: `requirements.txt` contains libraries for running `Exploratory_Data_Analysis.ipynb`. Please run `Model_Training.ipynb` remotely.

### Usage
Navigate to the notebooks/ directory and launch the Jupyter notebooks:
```bash
jupyter notebook Exploratory_Data_Analysis.ipynb
jupyter notebook Model_Training.ipynb
```
NOTE: It is strongly recommended that you run `Model_Training.ipynb` remotely (the file has been configured for Google Colab), but it can be viewed in the Jupyter Notebook interface.

### License
The code in this repository is released under the MIT License. See the `LICENSE` file for more details.

### Author
Kelly Olsson

### Acknowledgements
Data was sourced from [Loja Contectada](https://www.lojaconectada.com.br/) thanks to Paulo Henrique [@phsantosjr ](https://github.com/phsantosjr). All permissions to use this data belong to the original data owner.  
