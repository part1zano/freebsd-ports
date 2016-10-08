--- khal/cli.py.orig	2016-10-06 17:02:45 UTC
+++ khal/cli.py
@@ -22,7 +22,7 @@
 import logging
 import sys
 import textwrap
-from shutil import get_terminal_size
+from backports.shutil_get_terminal_size import get_terminal_size
 
 try:
     from setproctitle import setproctitle
