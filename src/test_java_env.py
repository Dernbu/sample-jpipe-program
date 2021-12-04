
import os
import sys

path = os.path.dirname(__file__)
print( os.environ.get('JDK_HOME'))
print( os.environ.get('JRE_HOME'))
print( os.environ.get('JAVA_HOME'))

import jpype
print(jpype.getDefaultJVMPath())