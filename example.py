# this explitily makes a list, but you could use it directly as the parameter for a for loop:
# e.g.
#   for drive in $(ls /dir | grep "sd"):

attached_drives = $(ls /dir | grep "sd")

mounted_drives = ()
unmounted_drives = ()
for drive in attached_drives:
  if $(findmnt $drive):
    mounted_drives += drive
    
    # run some function or program
  else:
    unmounted_drives += drive
    # 
