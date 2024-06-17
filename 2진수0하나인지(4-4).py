output = [i
          for i in range(1,101)
          if "{:b}".format(i).count("0")==1]

output = [i
          for i in range(1,101)
          if ("{:b}".format(i).find("0")=="{:b}".format(i).rfind("0")) and ("{:b}".format(i).find("0")!=-1)]

for i in output:
    print("{} : {}".format(i,"{:b}".format(i)))
print("합계:",sum(output))
