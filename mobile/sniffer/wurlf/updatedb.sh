#!/bin/sh
#
# Unpack and update pywurfl database

wget http://downloads.sourceforge.net/project/wurfl/WURFL/latest/wurfl-latest.zip

unzip wurfl-latest.zip
../../../../../bin/zopepy  wurfl2python.py  wurfl.xml 

# File too big to commit
rm wurfl.xml
rm wurfl-latest.zip

