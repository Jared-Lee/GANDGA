# GANDGA
Using Deep Learning To Implement Domain Generation Algorithm.

# Suggest Requirement
* Anaconda3 (with Python 3.6)
* Windows 10 x64
* CUDA 8.0.61
* cuDNN v5

# Setting
## A. Create anaconda environment

Chioce what environment you want (but I only test the environment with python 3.5) :

1- Create Environment with python 2.7 :     `conda create --name gandga27 python=2.7`

2- Create Environment with python 3.5 :     `conda create --name gandga35 python=3.5`

3- Create Environment with python 3.6 :     `conda create --name gandga36 python=3.6`

## B. Install all of the following package

1- First input :(just input one of them, don't input them at the same time)

            (in windows)
        activate gandga35
            (in linux)
        . activate gandga35
    
2- input following:

        conda install ipython
        conda install graphviz
        conda install matplotlib
        conda install notebook
        conda install scipy (if failed, try: conda install -c conda-forge scipy )
        conda install numpy 
        conda install pillow
        conda install pip
        conda install scikit-learn
        conda install tensorflow (if failed, try: conda install -c conda-forge tensorflow )
        
        conda install theano
        
        (only support python 3.5 in windows-64)
        conda install keras
        (Maybe you can try: pip install keras)
        
        conda install pydot-ng   

3- Then input: `jupyter notebook` 

4- If you want to remove environment, input `conda remove -n [ENVIRONMENT_NAME] --all`

   Please replace [ENVIRONMENT_NAME] to the name of environment which you want to remove.

This is a very early development project.
You can mail to s1036051@mail.yzu.edu.tw , if you want to discuss.
