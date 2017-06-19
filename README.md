# GANDGA
Using Deep Learning To Implement Domain Generation Algorithm.

# Suggest Requirement
* Anaconda3 (with Python 3.6)
* Windows 10 x64
* CUDA 8.0.61
* cuDNN v5

# Setting
* A. In anaconda console
* 1. Create Eni with python 2.7 : conda create --name gandga27 python=2.7
* 2. Create Eni with python 3.5 : conda create --name gandga35 python=3.5
* 3. Create Eni with python 3.6 : conda create --name gandga36 python=3.6

* B. Install all of it in envir gandga27 and envir gandga35
* First input :
*       (1) activate gandga27 
*       (2) activate gandga35 
*       (3) . activate gandga27 
*       (4) . activate gandga35

* You can change the Channel name from "gandga" to "ANY_NAME_U_WANT" in the first line of "gandga_envir.yml"
* In anaconda console,input: 
*       conda env create -f gandga_envir.yml
* If you need to update, input: conda env update -f gandga_envir.yml
* Finally, 
* if you install this in linux, input: . activate gandga (or . activate  ANY_NAME_U_WANT) 
* if you install this in windows, input: activate gandga (or activate  ANY_NAME_U_WANT) 
* Then input: jupyter notebook 

This is a very early development project.
You can mail to s1036051@mail.yzu.edu.tw , if you want to discuss.
