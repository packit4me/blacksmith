#!/usr/bin/python

from distutils.core import setup
#from setuptools import setup,find_packages

NAME = "blacksmith"
VERSION = "0.1"
SHORT_DESC = "%s tool for to build RPMs from Puppet Forge" % NAME
LONG_DESC = """
%s is a python application that downloads releases from Puppet Forge
and rolls them up into RPMs.  Then it will also generate a usable yum
repository for managing the version of  modules installed on a system
in the same way you can manage your regular software.
""" % NAME


if __name__ == "__main__":
 
#        manpath    = "share/man/man1/"
        setup(
                name = NAME,
                version = VERSION,
                author = "Greg Swift",
                author_email = "gregswift@gmail.com",
                url = "https://github.com/gregswift/%s" % NAME,
                license = "GPLv3",
                scripts = ["scripts/%s" % NAME],
                package_dir = {NAME: NAME},
                packages = [NAME],
                description = SHORT_DESC,
                long_description = LONG_DESC
        )

#                data_files = [(manpath,  ["docs/%s.1.gz" % NAME])],
