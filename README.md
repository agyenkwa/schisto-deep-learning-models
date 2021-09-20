# deep-learning-resources
This page shows the python code and trained models of the paper 'Deep Neural Networks predict inhibitors of Schistosoma mansoni thioredoxin glutathione reductase (SmTGR).


The code in this page is for combining files, pre-processing, data splitting, training, and loading and testing. To implement the code, kindly change the filepaths in the .py files for each task.

To reproduce the experiment follow these main steps:

Download the data (active and inactive separately) from PubChem in the SDF formats.
Feed the two files to the descriptor calculator (preferably Mold2 on KNIME) to obtain two .csv files with calculated descriptors.
Run the combining files.py to join the two .csv files into one.
Run the pre-processing.py on the resulting file.
Run the data splitting.py on the pre-processed data.
Finally, run the training.py. The trained model will be saved at the working directory.
To load and use for prediction or re-training, run the loading and testing.py file.


Running Environment

Operating System: Windows 10;


Deep learning framework: Keras with Tensorflow backend in Python 3.6.0 onwards;
Requirements:

KNIME

ANACONDA

Scipy 1.1.0;

Numpy 1.17.4;
