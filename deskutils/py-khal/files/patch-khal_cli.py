--- khal/cli.py.orig	2016-10-08 14:08:51 UTC
+++ khal/cli.py
@@ -22,7 +22,7 @@
 import logging
 import sys
 import textwrap
-from shutil import get_terminal_size
+from backports.shutil_get_terminal_size import get_terminal_size
 
 try:
     from setproctitle import setproctitle
