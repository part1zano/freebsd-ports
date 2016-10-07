--- setup.py.orig	2016-10-06 17:02:45 UTC
+++ setup.py
@@ -43,8 +43,6 @@ setup(
     install_requires=requirements,
     extras_require=extra_requirements,
     tests_require=test_requirements,
-    setup_requires=['setuptools_scm'],  # not needed when using packages from PyPI
-    use_scm_version={'write_to': 'khal/version.py'},
     classifiers=[
         "Development Status :: 4 - Beta",
         "License :: OSI Approved :: MIT License",
