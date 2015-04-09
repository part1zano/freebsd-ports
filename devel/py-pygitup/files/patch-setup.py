--- setup.py.orig	2015-04-10 00:05:34.000000000 +0300
+++ setup.py	2015-04-10 00:06:01.000000000 +0300
@@ -6,8 +6,8 @@
     version="1.2.2",
     packages=find_packages(exclude=["tests"]),
     scripts=['PyGitUp/gitup.py'],
-    install_requires=['GitPython==0.3.2.1', 'colorama==0.3.2',
-                      'termcolor==1.1.0', 'docopt==0.6.1'],
+    install_requires=['GitPython>=0.3.2.1', 'colorama>=0.3.2',
+                      'termcolor>=1.1.0', 'docopt>=0.6.1'],
 
     # Tests
     test_suite="nose.collector",
