Scripts for the analysis of transcranial magnetic stimulation (TMS) motor maps obtained using the grid-based method. Sample dataset.

How to run:

1. Map coverage analysis

The first calculation concerns estimating the fractions of 121 muscle representations (mapped without grid) that would be covered by square grids of different sizes. The relevant data and scripts are in the folder 'Map coverage'. 'mappings.csv' contains the non-grid mapping results in the format (session_id;x;y;z;MEP_amplitude). The file 'desc.xlsx' contains information about subject id, handedness, studied hand, muscle and date of study. The scripts were tested under MATLAB R2017a. The script 'calculate_diameter.m' must be run to produce the file 'fractions.xlsx' containing the results, which will be used by the Python scripts in the parent folder for statistical analysis and visualization.

2. Analysis of grid-based TMS maps

The scripts were tested under Python 3.7.2. The script 'parseNexstimMaps.py' can be used for converting Nexstim text files with TMS mapping results into CSV-files used by the Python scripts. The sample data are in 'grid mappings.csv' (same format as above) and contain mapping results for 8 healthy subjects obtained in 3 sessions on consecutive days using a 7x7 square grid with a cell size of 7.63 mm at the peeling depth of 20 mm, with 10 stimuli per cell. The Jupyter notebook 'TMSmapsAnalysis.ipynb' must be run to read the data, perform the statistical analysis and save the picture files with visualizations (including the results of map covegage analysis).

Requirements:
Python libraries: numpy, matplotlib, sklearn, collections, xlrd, scipy, rpy2.
Some of the statistical tests require the R language and are interfaced from Python through rpy2.
Required R packages: base, crank, npsm.


Study contributors:

Dmitry O. Sinitsyn 1, Andrey Yu. Chernyavskiy 1,2, Alexandra G. Poydasheva 1, Ilya S. Bakulin 1, Natalia А. Suponeva 1, Michael A. Piradov 1
1 Research Center of Neurology, Moscow, Russia
2 Valiev Institute of Physics and Technology of Russian Academy of Sciences, Moscow, Russia
