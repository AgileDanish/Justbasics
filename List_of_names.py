#Checking if a particular name is present in a list of names or not
names=["danish", "rupesh", "saurabh", "aquib", "amit", "arif"]

def find(name,names):
    return (name in names)
print(find("danish",names))