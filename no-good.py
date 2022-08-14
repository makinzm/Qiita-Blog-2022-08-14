from sys import argv
import time

import qiita

qiita.func.func(int(argv[1]))

### *** ###
from subprocess import run
run("pip install torch==1.0.0",shell=True)
import torch
print("torch.__version__: ",torch.__version__)
### *** ###

time.sleep(1)

qiita.func.makeDead()
