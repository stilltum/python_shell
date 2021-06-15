# this explitily makes a list, but you could use it directly as the parameter for a for loop:
# e.g.
#   for drive in $(ls /dir | grep "sd"):

# The idea is that all commands within $() are commandline calls, unless it is prepended by another $, in which case it's a script variable

attached_drives = $(ls /dir | grep "sd").splitlines()

mounted_drives = {}
unmounted_drives = {}
for drive in attached_drives:
  if $(findmnt $drive):
    mounted_drives += drive
    
    # some administative output
    percent = $(df --output=pcent $drive).splitlines()[1][:-1]
    if percent > 80:
      print("your drive is getting full!")
  else:
    unmounted_drives += drive
    
    # some administrative output
    print("did you mean to mount " + drive + "?")
