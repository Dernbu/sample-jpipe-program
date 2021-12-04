from jpype import *
from jpype.types import *

startJVM(getDefaultJVMPath(), '-ea', '-Djava.class.path=src\\')
# java.lang.System.out.println("JVM Started!")

Testclass = JClass("opt.TestClass")

java.lang.System.out.println(Testclass.next())

shutdownJVM()