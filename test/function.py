import os
import sys

cur=os.path.dirname(os.path.dirname(__file__))

filepath=os.path.join(cur,"filename","product.json")
print(cur)

def foo(arg1,arg2="OK",*tupleArg,**dictArg):
      print ("arg1=",arg1)
      print ("arg2=",arg2)
      for i,element in enumerate(tupleArg):
          print ("tupleArg %d-->%s" % (i,str(element)))
      for  key in dictArg:
          print ("dictArg %s-->%s" %(key,dictArg[key]))


myList=["my1","my2"]
myDict={"name":"Tom","age":22}

foo("formal_args",arg2="argSecond",a=1)
print ("*"*40)
foo(123,myList,myDict)
print ("*"*40)
foo(123,rt=123,*myList,**myDict)

li = [1,2,3,4,5,6,7,8,9]
enumerate
print(list(map((lambda x: x * x), li)))


# result=open(file=filepath,mode="r")
# print(result.read())
# result.close()

with open(file=filepath,mode="r") as result:
    print(result.read().)







