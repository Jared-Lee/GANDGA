# GANDGA
Using Deep Learning To Implement Domain Generation Algorithm.

# Suggest Requirement
* Anaconda3 (with Python 3.6)
* Windows 10 x64
* CUDA 8.0.61
* cuDNN v5

# Setting
## A. Create anaconda environment

Set up the environment you want by `conda create --name [YOUR_ENVIRONMENT_NAME] python=[PYTHON_VERSION]`

For example: 

1- Create Environment with python 2.7 :     `conda create --name gandga27 python=2.7`

2- Create Environment with python 3.5 :     `conda create --name gandga35 python=3.5`

3- Create Environment with python 3.6 :     `conda create --name gandga36 python=3.6`

* But I test most of the programs in the environment with python 3.5, so I suggust to choice the same version.

## B. Install all of the following package

1- First input :(just input one of them, don't input them at the same time)

            In windows:
                        activate gandga35
            In linux:
                        . activate gandga35
    
2- input following:

            conda install ipython
            conda install graphviz
            conda install matplotlib
            conda install notebook
            conda install scipy                 (If failed, try: conda install -c conda-forge scipy )
            conda install numpy 
            conda install pillow
            conda install pip
            conda install scikit-learn
            conda install tensorflow            (If failed, try: conda install -c conda-forge tensorflow )
            conda install theano
            conda install keras                 (If failed, try: conda install -c conda-forge keras 
                                                 or maybe you can try: pip install keras )
            pip install pydot-ng  
            pip install graphviz

3- Then input: `jupyter notebook` 

4- If you want to remove environment, input `conda remove -n [ENVIRONMENT_NAME] --all`

   Please replace [ENVIRONMENT_NAME] to the name of environment which you want to remove.

5- (option) If You want to switch the backend of keras, You can go to `C:\ProgramData\Anaconda3\envs\[YOUR_ENVIRONMENT_NAME]\etc\conda\activate.d` and find `keras_activate.bat`. 

   Then you can change `set "KERAS_BACKEND=theano"` to `set "KERAS_BACKEND=tensorflow"` if you want.


This is a very early development project.
You can mail to s1036051@mail.yzu.edu.tw , if you want to discuss.
