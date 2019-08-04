# Luminoth_tests
Luminoth_tests
Luminoth is an open source toolkit for computer vision. Currently, we support object detection, but we are aiming for much more. It is built in Python, using TensorFlow and Sonnet.

Read the full documentation here.

Example of Object Detection with Faster R-CNN

DISCLAIMER: Luminoth is still alpha-quality release, which means the internal and external interfaces (such as command line) are very likely to change as the codebase matures.

Installation
Luminoth currently supports Python 2.7 and 3.4–3.6.

Pre-requisites
To use Luminoth, TensorFlow must be installed beforehand. If you want GPU support, you should install the GPU version of TensorFlow with pip install tensorflow-gpu, or else you can use the CPU version using pip install tensorflow.

Installing Luminoth
Just install from PyPI:

pip install luminoth
Optionally, Luminoth can also install TensorFlow for you if you install it with pip install luminoth[tf] or pip install luminoth[tf-gpu], depending on the version of TensorFlow you wish to use.

Google Cloud
If you wish to train using Google Cloud ML Engine, the optional dependencies must be installed:

pip install luminoth[gcloud]
Installing from source
First, clone the repo on your machine and then install with pip:

git clone https://github.com/tryolabs/luminoth.git
cd luminoth
pip install -e .
Check that the installation worked
Simply run lumi --help.

Supported models
Currently, we support the following models:

Object Detection
Faster R-CNN
SSD
We are planning on adding support for more models in the near future, such as RetinaNet and Mask R-CNN.

We also provide pre-trained checkpoints for the above models trained on popular datasets such as COCO and Pascal.

Usage
There is one main command line interface which you can use with the lumi command. Whenever you are confused on how you are supposed to do something just type:

lumi --help or lumi <subcommand> --help

and a list of available options with descriptions will show up.

Working with datasets
See Adapting a dataset.

Training
See Training your own model to learn how to train locally or in Google Cloud.

Visualizing results
We strive to get useful and understandable summary and graph visualizations. We consider them to be essential not only for monitoring (duh!), but for getting a broader understanding of what's going under the hood. The same way it is important for code to be understandable and easy to follow, the computation graph should be as well.

By default summary and graph logs are saved to jobs/ under the current directory. You can use TensorBoard by running:

tensorboard --logdir path/to/jobs
Why the name?
The Dark Visor is a Visor upgrade in Metroid Prime 2: Echoes. Designed by the Luminoth during the war, it was used by the Champion of Aether, A-Kul, to penetrate Dark Aether's haze in battle against the Ing.

-- Dark Visor - Wikitroid

License
Copyright © 2018, Tryolabs. Released under the BSD 3-Clause.
