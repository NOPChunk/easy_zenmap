#!usr/bin/env python3

import subprocess

subprocess.call(["pip", "install", "wget"])

import wget

# STEP [1] Install alien pkg .
subprocess.call(["apt", "install", "alien", "-y"])

# STEP [2] Download requirements .
# 2-A Download zenmap.rpm
url_zenmap = "https://nmap.org/dist/zenmap-7.80-1.noarch.rpm"
zenmap = wget.download(url_zenmap)

# 2-B download python-gtk2
url_gtk = "http://archive.ubuntu.com/ubuntu/pool/universe/p/pygtk/python-gtk2_2.24.0-5.1ubuntu2_amd64.deb"
gtk = wget.download(url_gtk)

# 2-C Download python-gobject
url_gobject = "http://azure.archive.ubuntu.com/ubuntu/pool/universe/p/pygobject-2/python-gobject-2_2.28.6-14ubuntu1_amd64.deb"
gobject = wget.download(url_gobject)

# 2-D Download python-cairo
url_cairo = "http://security.ubuntu.com/ubuntu/pool/universe/p/pycairo/python-cairo_1.16.2-2ubuntu2_amd64.deb"
cairo = wget.download(url_cairo)

# STEP [3] Use alien to convert zenmap.rpm to zenmap.deb .
subprocess.call(["alien", "zenmap-7.80-1.noarch.rpm"])
#
# # STEP [4] Use dpkg to install zenmap.deb .
subprocess.call(["dpkg", "-i", "zenmap_7.80-2_all.deb"])

# STEP [5] Install the requirements for zenmap GUI
subprocess.call(["dpkg", "-i", "python-cairo_1.16.2-2ubuntu2_amd64.deb"])
subprocess.call(["dpkg", "-i", "python-gobject-2_2.28.6-14ubuntu1_amd64.deb"])
subprocess.call(["dpkg", "-i", "python-gtk2_2.24.0-5.1ubuntu2_amd64.deb"])

# STEP [7] Remove installed pkgs
subprocess.call(["rm", "-rf", "zenmap-7.80-1.noarch.rpm"])
subprocess.call(["rm", "-rf", "zenmap_7.80-2_all.deb"])
subprocess.call(["rm", "-rf", "python-cairo_1.16.2-2ubuntu2_amd64.deb"])
subprocess.call(["rm", "-rf", "python-gobject-2_2.28.6-14ubuntu1_amd64.deb"])
subprocess.call(["rm", "-rf", "python-gtk2_2.24.0-5.1ubuntu2_amd64.deb"])

# STEP [8] RUN zenmap GUI .
subprocess.call(["zenmap"])











