# you can make lists explicitly or use them as the input for other functions or operators
# e.g.
#   for drive in $(ls /dir | grep "sd").splitlines():

# The idea is that all commands within $() are commandline calls, unless it is prepended by another $, in which case it's a script variable
#   We need to seriously evaluate security implications. Maybe adding a .scope("/directory") function immediatly after the call it applies to?

attached_drives = $(ls "/dev" | grep "sd").splitlines()

mounted_drives = []
unmounted_drives = []
for drive in attached_drives:
  # The drive is mounted
  #   Note that if nothing is returned from a call it returns an empty list which evaluates to false
  if $(findmnt $drive):
    mounted_drives += drive
    
    # some administative output
    percent = $(df --output=pcent $drive).splitlines()[1][:-1]
    if int(percent) > 80:
      print("your drive is getting full!")
  
  # The drive is not mounted
  else:
    unmounted_drives += drive
    
    # some administrative output
    print("did you mean to mount " + drive + "?")
