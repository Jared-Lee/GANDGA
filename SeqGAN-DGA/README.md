# SeqGAN-DGA
Using SeqGAN To Implement Domain Generation Algorithm.

# Reference
This code is based on https://github.com/LantaoYu/SeqGAN from **SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient** https://arxiv.org/abs/1609.05473 .

# Suggest Requirement
* Windows 10 x64

# Requirement
* Anaconda3 x64 (with Python 3.6)
* CUDA 8.0+
* cuDNN v5.1 (You may fail if you use a higher or lower version)
* NVIDIA Graphic Card (Like GTX 1060)
* TensorFlow r1.2.0

# Setting

## Anaconda environment

* Open the terminal on linux or **`Anaconda Prompt`** on Windows. 

* Create the environment by command: **`conda create --name [YOUR_ENVIRONMENT_NAME] python=[PYTHON_VERSION]`**

   * Create Tensorflow Environment with python 3.5 :     **`conda create --name py35_tf120 python=3.5`**


## B. Install packages in Tensorflow Environment

1. Active the enviroment by command: **`activae [YOUR_ENVIRONMENT_NAME]`**

            On Windows:
                        activate py35_tf120
            On Linux:
                        . activate py35_tf120
    
2. Input following command:

            conda install ipython
            conda install graphviz
            conda install matplotlib
            conda install notebook
            conda install scipy                 (If failed, try: conda install -c conda-forge scipy )
            conda install pillow
            conda install scikit-learn
            
            (option)
            conda install numpy                 (If you don't have numpy)
            conda install pip                   (If you don't have pip)
            
            (use GPU on windows, reference: https://www.tensorflow.org/install/install_windows )
            pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-1.2.0-cp35-cp35m-win_amd64.whl
            
            (use GPU on linux, didn't check, reference: https://www.tensorflow.org/install/install_linux )
            pip3 install --upgrade tensorflow-gpu
            (or)
            pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.2.0-cp35-cp35m-linux_x86_64.whl

            pip install pydot-ng  


3. If you want to use GPU-version TensorFlow (no matter what kind of OS), **`MAKE SURE YOU HAVE CUDA AND CuDNN 5.1`**, this is very important. **`Most of versions of TensorFlow only support CuDNN 5.1`**. Make sure you have it.

4. Clone these repositories to any place you want, Then input: **`jupyter notebook`** 

5. (option) If You want to switch the backend of keras on windows, You can go to **`C:\ProgramData\Anaconda3\envs\[YOUR_ENVIRONMENT_NAME]\etc\conda\activate.d`** and find out **`keras_activate.bat`** in this folder. Open the file, then you can change **`set "KERAS_BACKEND=theano"`** to **`set "KERAS_BACKEND=tensorflow"`** if you want.

## C. Remove Environments

* If you want to remove environment, input **`conda remove -n [ENVIRONMENT_NAME] --all`**

   * (Please replace **[ENVIRONMENT_NAME]** to the name of environment which you want to remove.)

-----

This is a very early development project. 

**I have not finished this project yet.**

You can mail to s1036051@mail.yzu.edu.tw , if you want to discuss.
