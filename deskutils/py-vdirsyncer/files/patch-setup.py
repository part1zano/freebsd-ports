--- setup.py.orig	2016-02-09 21:31:12 UTC
+++ setup.py
@@ -17,10 +17,6 @@ from setuptools import find_packages, se
 
 setup(
     name='vdirsyncer',
-    use_scm_version={
-        'write_to': 'vdirsyncer/version.py',
-    },
-    setup_requires=['setuptools_scm'],
     author='Markus Unterwaditzer',
     author_email='markus@unterwaditzer.net',
     url='https://github.com/untitaker/vdirsyncer',
