# GANDGA
Using Deep Learning To Implement Domain Generation Algorithm.

# Suggest Requirement
* Windows 10 x64
* Anaconda3 x64 (with Python 3.6)
* CUDA 8.0+
* cuDNN v5+

# Setting
## A. Create anaconda environment

Set up the environment you want by **`conda create --name [YOUR_ENVIRONMENT_NAME] python=[PYTHON_VERSION]`**

For example: 

1- Create Environment with python 2.7 :     **`conda create --name gandga27 python=2.7`**

2- Create Environment with python 3.5 :     **`conda create --name gandga35 python=3.5`**

3- Create Environment with python 3.6 :     **`conda create --name gandga36 python=3.6`**

* *But I test most of the tensorflow programs in the environment with python 3.5, so I suggust to choice the same version.*

## B. Install all of the following package

1- First input : *(just input one of them, don't input them at the same time)*

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
            
            (only use CPU)
            conda install tensorflow            (If failed, try: conda install -c conda-forge tensorflow )
            
            (use GPU on windows, reference: https://www.tensorflow.org/install/install_windows )
            pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-1.2.0-cp35-cp35m-win_amd64.whl
            
            (use GPU on linux, didn't test, reference: https://www.tensorflow.org/install/install_linux )
            pip3 install --upgrade tensorflow-gpu
            
            conda install theano
            conda install keras                 (If failed, try: conda install -c conda-forge keras 
                                                 or maybe you can try: pip install keras )
            pip install pydot-ng  
            pip install graphviz

3- Clone this repository to any place you want, Then input: **`jupyter notebook`** 

4- If you want to remove environment, input **`conda remove -n [ENVIRONMENT_NAME] --all`**

   Please replace **[ENVIRONMENT_NAME]** to the name of environment which you want to remove.

5- (option) If You want to switch the backend of keras on windows, You can go to **`C:\ProgramData\Anaconda3\envs\[YOUR_ENVIRONMENT_NAME]\etc\conda\activate.d`** and find out **`keras_activate.bat`** in this folder. Open the file, then you can change **`set "KERAS_BACKEND=theano"`** to **`set "KERAS_BACKEND=tensorflow"`** if you want.


#

This is a very early development project.
You can mail to s1036051@mail.yzu.edu.tw , if you want to discuss.
