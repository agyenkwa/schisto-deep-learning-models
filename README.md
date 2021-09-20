# deep-learning-resources
This page shows the python code and trained models of the paper 'Deep Neural Networks predict inhibitors of Schistosoma mansoni thioredoxin glutathione reductase (SmTGR)'. These are the five best performing models out of 30 trained hence the nomenclature of 'DNN_number'.


The code in this page is for combining files, pre-processing, data splitting, training, and loading and testing. To implement the code, kindly change the filepaths in the .py files for each task.

To reproduce the experiment follow these main steps:

1. Download the data (active and inactive separately) from PubChem in the SDF formats.
2. Feed the two files to the descriptor calculator (preferably Mold2 on KNIME) to obtain two .csv files with calculated descriptors.
3. Run the Combining files.py to join the two .csv files into one.
4. Run the Pre-processing.py on the resulting file.
5. Run the data Data splitting.py on the pre-processed data.
6. Finally, run the Training.py. The trained model will be saved at the working directory.
7. To load and use for prediction or re-training, run the Loading and testing.py file.


Running Environment

Operating System: Windows 10;


Deep learning framework: Keras with Tensorflow backend in Python 3.6.0 onwards;
Requirements:

KNIME

ANACONDA

Scipy 1.1.0;

Numpy 1.17.4;
