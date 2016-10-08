--- khal/terminal.py.orig	2016-10-08 14:20:24 UTC
+++ khal/terminal.py
@@ -22,7 +22,7 @@
 """all functions related to terminal display are collected here"""
 
 from collections import namedtuple
-from itertools import zip_longest
+from itertools import izip_longest as zip_longest
 
 
 NamedColor = namedtuple('NamedColor', ['index', 'light'])
