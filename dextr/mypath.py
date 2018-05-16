import os
from os.path import join, abspath, dirname

class Path(object):
    @staticmethod
    def models_dir():
        return join(dirname(abspath(__file__)), 'models')
    
