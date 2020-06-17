A_SIDE = 3
SIZE = A_SIDE**2
HIDDEN = round(5/4 * SIZE)
with open("wasfile.txt") as f:
    WAS_FILE = f.readlines()[0]
    if WAS_FILE == "False":
        WAS_FILE = False
    else:
        WAS_FILE = True