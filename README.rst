sat-util
+++++++++++

.. image:: https://travis-ci.org/sat-utils/sat-util.svg?branch=develop
    :target: https://travis-ci.org/sat-utils/sat-util

Sat-util is a Python library for creating command line utilities for specific sensors, utilizing several sat-utils repositories.

- sat-query
- sat-download
- sat-process

Furthermore, sat-utils relies on a running sat-api that provides an API to the imagery metadata.

Sat-util data paths
-------------------

A sat-util (e.g., sentinel2-util, landsat8-util) defaults to downloading and storing processed data in sat-utils/ directory in their home directory. Within ~/sat-utils a directory will be created with the name of the sensor (e.g., ~/sat-utils/sentinel2), which contains two folders: download/ and processed/. Each of these directories will contain one directory for every "scene" of data, a scene being a single location (e.g., path/row of Landsat) for a specific time. The sat-util directory can be changed by setting the SATUTIL_DIR variable in a .sat-utils configuration file in the user's home directory.



