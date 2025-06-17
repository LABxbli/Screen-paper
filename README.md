
This repository contains all the custom scripts and tools used in the study **"Functional-Genomic Landscape of Photosynthetic Acclimation to Nitrogen Deficiency"**, as well as two dataset files associated with this study. File 1 and File 2 present experimental details for genetic validation of genes identified from ARENA screens. Files labeled 'Pheno_XXX' contain scripts and machine learning models developed for digitizing and quantifying phenotypes in secondary screening experiments. Files labeled 'Geno_XXX' include scripts used for identification of insertion sites from deep-sequencing data.

All custom scripts were written by **Penghao Yang**, **Kangning Guo** and **Yanlei Feng**..

---

## File information

1. **`File 1`** - Summary of genetic complementation results of specific mutants.
   
2. **`File 2`** - Summary of genetic validation of specific genes' functions by generating and characterizing independent mutants from CRISPR–Cas9.
  
3. **`RGB_score.xlsx`** - Excel file containing RGB score data used for training and validating the greenness prediction model.
   
4. **`Pheno_greenness_training.py`** - Python script that trains a Support Vector Machine (SVM) classifier to predict greenness scores based on RGB_score.xlsx, and saves the trained model to a file as model.svm.linear.pkl.

5. **`model.svm.linear.pkl`** - Pre-trained SVM model file used by Pheno_greenness_scoring.py for greenness prediction.

6. **`Pheno_greenness_scoring.py`** - Python script to quantify the greenness of colony images using a pre-trained SVM model.

7. **`Pheno_pam.ipynb`** - Jupyter notebook for quantifying chlorophyll fluorescence phenotypes (Fv/Fm and NPQ) from Imaging-PAM data.

8. **`Pheno_size.ipynb`** - Jupyter notebook for quantifying colony size from plate images using pixel segmentation and RGB thresholding.

9. **`Pheno_cluster.py`** - Python script for phenotypic clustering using secondary screening data.

10. **`Geno_merge.py`** - Python script for merging paired sequencing data and generating new format combined files.
    
11. **`Geno_split.py`** - Python script for splitting barcode sequence files into upstream and downstream fragments in FASTA format.
    
12. **`Geno_cassetteID.py`** - Python script to identify and extract cassette flanking sequences from assembled or extracted sequence files and output them in a structured format.
    
13. **`Geno_extract.py`** - Python script for extracting specific genomic DNA sequences from assembled genomes and mapping files, with optional reverse-complement transformation.



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

For questions or issues regarding the code, please contact Penghao Yang at yangpenghao@westlake.edu.cn or Kangning Guo at guokangning@westlake.edu.cn.

