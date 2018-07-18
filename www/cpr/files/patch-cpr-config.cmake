--- cpr-config.cmake.orig	2018-07-18 20:06:59 UTC
+++ cpr-config.cmake
@@ -11,11 +11,15 @@
 #                     file that uses this interface
 
 find_path(CPR_INCLUDE_DIR
-          NAMES cpr.h)
+          NAMES cpr/cpr.h
+		  PATHS
+		  /usr/local/include)
 
 find_library(CPR_LIBRARY
-             NAMES cpr
-             HINTS ${CPR_LIBRARY_ROOT})
+			 NAMES cpr
+			 PATHS
+			 /usr/local/lib
+			 )
 
 include(FindPackageHandleStandardArgs)
 find_package_handle_standard_args(CPR REQUIRED_VARS CPR_LIBRARY CPR_INCLUDE_DIR)
