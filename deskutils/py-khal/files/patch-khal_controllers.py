--- khal/controllers.py.orig	2016-10-08 14:12:08 UTC
+++ khal/controllers.py
@@ -24,7 +24,7 @@ import icalendar
 from click import confirm, echo, style, prompt
 from vdirsyncer.utils.vobject import Item
 
-from shutil import get_terminal_size
+from backports.shutil_get_terminal_size import get_terminal_size
 
 from datetime import date, datetime, timedelta
 import logging
