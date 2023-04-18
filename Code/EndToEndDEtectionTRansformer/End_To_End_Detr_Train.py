# -*- coding: utf-8 -*-
"""end to end DETR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oz3tqniAoRU0gGS2xFNNX-l9w-WVZLr7
"""

# Commented out IPython magic to ensure Python compatibility.
!sudo echo -ne '\n' | sudo add-apt-repository ppa:alessandro-strada/ppa >/dev/null 2>&1 # note: >/dev/null 2>&1 is used to supress printing
!sudo apt update >/dev/null 2>&1
!sudo apt install google-drive-ocamlfuse >/dev/null 2>&1
!google-drive-ocamlfuse
!sudo apt-get install w3m >/dev/null 2>&1 # to act as web browser 
!xdg-settings set default-web-browser w3m.desktop >/dev/null 2>&1 # to set default browser 
# %cd /content
!mkdir gdrive
# %cd gdrive
!mkdir "MyDrive"
!google-drive-ocamlfuse "/content/gdrive/MyDrive"

import os
os.chdir('/content')

# INSTALL CONDA ON GOOGLE COLAB
################################################################################
! wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.2-Linux-x86_64.sh
! chmod +x Miniconda3-py37_4.8.2-Linux-x86_64.sh
! bash ./Miniconda3-py37_4.8.2-Linux-x86_64.sh -b -f -p /usr/local
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages/')

#import os

#os.chdir('/content/gdrive/MyDrive')

#!git clone https://github.com/facebookresearch/detr.git

!conda install cython scipy
!pip install -U 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'

"""Dataset preparation"""

!conda install pytorch==1.5.1 torchvision==0.6.1 -c pytorch

"""Training"""

os.chdir('/content/gdrive/MyDrive/detr')

!python -m torch.distributed.launch --use_env main.py --coco_path '/content/gdrive/MyDrive/QueryDet-PyTorch/data/visdrone/coco_format' --epochs 3 --batch_size 3 --output_dir '/content/gdrive/MyDrive/saved_end2'



!python main.py --batch_size 2 --no_aux_loss --eval --resume /content/gdrive/MyDrive/saved_end1/checkpoint.pth --coco_path /content/gdrive/MyDrive/QueryDet-PyTorch/data/visdrone/coco_format











import torch
torch.cuda.is_available()

torch.cuda.device_count()

torch.cuda.current_device()

torch.cuda.device(0)

torch.cuda.get_device_name(0)

torch._C._cuda_setDevice(0)