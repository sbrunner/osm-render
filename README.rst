OSM Render
==========

Build it
--------

.. code:: bash

    python bootstrap.py --distribute -v 1.7.1
    ./buildout/bin/buildout

Todo
----

- create postgis db
- download and import osm data (alps)
- download world boundaries
- build the styles
- create the tiles (EPSG 21781 and 2058)
- use the SRTM data
