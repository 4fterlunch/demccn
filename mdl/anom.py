import os
import shutil
import numpy as np
import urllib.request

class anom:
    def __init__(self, name):
        self.name = name

    def mkdir(self, working_dir):
        if not os.path.exists(os.path.join(working_dir, self.name)):
            self.path = os.path.join(working_dir, self.name)
            os.makedirs(self.path)
            os.makedirs(os.path.join(self.path, 'neg'))
            os.makedirs(os.path.join(self.path, 'pos'))
            print('created model dir at: ', self.path)
        else:
            print('model name already exists')

    def rmdir(self):
        assert self.path is not None
        if os.path.exists(self.path):
            shutil.rmtree(self.path)
            print(self.path, 'removed')
        else:
            print('nothing to delete!')

    def load_images_from_file(self, path):
        pass

def main():
    test = anom('test')
    test.mkdir(os.path.dirname(__file__))
    test.rmdir()
if __name__ == "__main__":
    main()
