import shutil
countup = 0
import random
while True:
    countup +=random.randrange(0,2048)
    print(countup)
    shutil.copyfile("G:\Computing Group\Oliver\SMILE.jpg",(str("H:"+(str(countup)+str(random.rnd())+".jpg"))))
