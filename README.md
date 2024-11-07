
This repository contains all the custom scripts and tools used in the study **"Functional Genomic Landscape of Photosynthetic Acclimation to Nitrogen Deprivation"**. These files were developed for digitizing and quantifying phenotypes in secondary screening experiments, including size and greenness measurements, as well as chlorophyll fluorescence parameters for each mutant colony.

All code was written by **Penghao Yang**.

---

## File information

1. **`RGB_score.xlsx`** - Excel file containing RGB score data used for training and validating the greenness prediction model.

2. **`model.svm.linear.pkl`** - Pre-trained SVM model file used by green_yellow_score_svm_v1.1.py for greenness prediction.

3. **`green_yellow_score_svm_v1.1.py`** - Python script to quantify the greenness of colony images using a pre-trained Support Vector Machine (SVM) model.

4. **`pam.ipynb`** - Jupyter notebook for quantifying chlorophyll fluorescence phenotypes (Fv/Fm and NPQ) from Imaging-PAM data.

5. **`size.ipynb`** - Jupyter notebook for quantifying colony size from plate images using pixel segmentation and RGB thresholding.

6. **`cluster_pheno.py`** - Python script for phenotypic clustering using secondary screening data.


## Dependencies

### Python 3.9.7 or above (http://www.python.org)
Python Packages <br>
**`OpenCV`** (https://github.com/opencv/opencv-python) <br>
**`scikit-learn`** (https://scikit-learn.org/stable/) <br>
**`Pillow`** (https://github.com/python-pillow/Pillow) <br>
**`Matplotlib`** (https://matplotlib.org) <br>
**`Seaborn`** (https://seaborn.pydata.org)

## License

This code is distributed under the GNU General Public License v3. See GPL-3.0 License for more details.

## Contact

For questions or issues regarding the code, please contact Penghao Yang at yangpenghao@westlake.edu.cn
