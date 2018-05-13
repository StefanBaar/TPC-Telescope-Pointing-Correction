# TPC-Telescope-Pointing-Correction
Depends on:

- numpy
- pytorch
- matplotlib

Depending on mount, machanics and the overall telescope construction, the pointing accuracy and precission varries for each positon (Alt Az). For older telescopes, the pointing can varry quite strongly (>10'). We can create a set of pointing paramteres to roughly model the geometric misalignments from a set of coorinates and their offset.
Since most software approches for correcting telescope pointing are hidden behind relatively expensice paywalls,I have started a github repo for analyzing and applying pointing corrections. The code is written in python using numpy, matplotlib, pytoch etc. and contains functions for solving and applying correction equations. For more information see the following jupyter notebook:
https://github.com/shissler1987/TPC-Telescope-Pointing-Correction/blob/master/Pointing_Correction.ipynb

coming soon:
- temperature, pressure, etc. paramteres
- polar maps
- AI predictor
