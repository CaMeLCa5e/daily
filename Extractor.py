#! /usr/bin/env python 

import sys 
import gc 
import getopt
import requests
import re
import bz2 
import os.path

prefix = None
keepLinks = False 
keepSections = False 

acceptedNamespaces = set(['w', 'wikitionary', 'wikt']) 