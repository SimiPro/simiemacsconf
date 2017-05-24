# execute first: this will create this file on your system. then add these two lines
# ipython profile create dev 

# you can select a profile like this: ipython --profile=foo        # start IPython using the new profile
# so add it afterwards like this in your emacs file: 
#(setq
 #  python-shell-interpreter "ipython"
  # python-shell-interpreter-args "--profile=dev"
#)

c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
