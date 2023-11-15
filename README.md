
## Project: Upper limb position-invariant EMG signal classification

The classification of Electromyogram (EMG) signal is an important task for various applications such as clinical diagnosis, Human-Computer Interaction (HCI) systems for prosthetic devices,myoelectric controllers used in wireless controlling devices such as video game controller and security check-in for authorized access. The vital research aspects in this field mainly focus on data acquisition, pre-processing, feature extraction and classifica-tion along with their feasibility in practical scenarios regarding implementation and reliability. We developed multiclass classification system for EMG signal using standard classifiers (Logistic Regression, SVM, Random Forrest, Extra Tree classifier) and also using their different ensembles . In our analysis, we have used a dataset consisting of the sEMG signals collected from eleven subjects at five different upper limb positions. [reference link][paper1].


<img src="/images/emg1.png" width="800" />



## Dataset: 

* For this study, we have used the dataset consisting of the myoelectric signal obtained from the upper limb of different subjects using multi-electrode channels at five different limb positions, which were recorded by Khushaba et al. [reference Link][paper2].


* Feature set used for the classification task: correlated time domain descriptors (cTDD).


## Preprocessed data folders:

* The data taken from a particular subject is taken into consideration. The extracted features and class labels (ranging from 0 to 7, total 8 classes) are stored in different subfolders within '../data/' folder. Individual subfolders are available for train, test and dev set.  


* There are two test sets:

  1. Set1: containing test instances from only 2 and 4 positions (to evaluate posiition invariant learning in true sense)

  2. Set2: containing test instances from all the possible positions in realtime scenario


* Feature dimesion of each datapoint is 42 D (CTTD feature set)


* Class labels: 0 to 7 (total 8 classes)



## Stored models and their performance:

* 4 machine learning classifiers are trained and fine tuned using gridSearchCV (k=5). 

* These baseline models are stored in ../models/ folder

   1. LR_emg_clf.pkl -- Logistic Regression model (multinomial mode)
   
   2. SVM_emg_clf.pkl -- SVM model (ovr mode)
   
   3. RF_emg_clf.pkl  -- Random Forrest model (bagging of Decision trees)
   
   4. ET_emg_clf.pkl  -- Extra-Trees model
   
   
* Furthermore, a soft voting classifier has been developed by combining (ensembling) these four models.   


### The performance of these models on test-set1 and test-set2 are as follows:

<img src="/images/emg2.png" width="600" />



## Want to install this project on your own machine?


Next, clone this project by opening a terminal and typing the following commands (do not type the first `$` signs on each line, they just indicate that these are terminal commands):

    $ git clone https://github.com/sumansamui/EMG_Signal_Classification.git
    
    $ cd EMG_Signal_Classification

    $ conda env create -f environment_EMG.yaml (optional step on Windows) (you may use your own python setup)
------------------------------------------------------

## References:

1. Mukhopadhyay, Anand Kumar, and Suman Samui. "An experimental study on upper limb position invariant EMG signal classification based on deep neural network." Biomedical Signal Processing and Control 55 (2020): 101669

[paper1]:https://www.sciencedirect.com/science/article/abs/pii/S1746809419302502


2. R.N. Khushaba, M. Takruri, J.V. Miro, S. Kodagoda, Towards limb positioninvariant myoelectric pattern recognition using time-dependent spectral features, Neural Netw. 55 (2014) 42–58.

[paper2]:https://www.sciencedirect.com/science/article/abs/pii/S0893608014000732

### For queries and further information:

please contact: samuisuman@gmail.com
 
### © 2020 Suman Samui All Rights Reserved 