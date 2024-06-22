import firelink

# List functions and strings from firelink
l = list(filter(lambda x: not x.startswith("__"),dir(firelink)))

# Get strings only (variables)
var = []
flag:bool
for x in l:
    exec("flag = type(firelink.{}) is str".format(x))
    if flag:
        var.append(x)

# Get user input
for x,y in enumerate(var):
    print(f"{x}){y}")

no = int(input("Choose the number of the website you want to open: "))

# Open the browser 
exec("firelink.firefox(firelink.{})".format(var[no]))
