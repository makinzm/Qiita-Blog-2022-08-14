from sys import argv
import time

import qiita

qiita.func.func(int(argv[1]))

time.sleep(1)

qiita.func.makeDead()
