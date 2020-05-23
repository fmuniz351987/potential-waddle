'''
I found this code online on stackoverflow, but I don't really remember the link 
to it. Please contact me if you find the real author to give him proper credits.

It's a simple script to upgrade all libs installed by pip. Just run 
$ python pip-update-all.py
On this folder in order to trigger updates. This is probably going to become
obsolete once pip's authors figure out their default behavior for upgrading all
pip packages.
'''

import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)
