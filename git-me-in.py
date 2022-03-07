import os
os.system("git add .")
commitNote = str(input("What's our -m comment?"))
os.system("git commit -m '%s'")