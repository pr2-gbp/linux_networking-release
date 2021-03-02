^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package multi_interface_roam
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.1.0 (2021-03-02)
------------------
* Merge pull request `#6 <https://github.com/pr2/linux_networking/issues/6>`_ from k-okada/add_noetic_travis
* fix explicit relative imports for both python2/3
* add more from __future_\_ import print_function
* add from __future_\_ import print_function for python3
* add import multi_interface_roam. fix by https://github.com/PR2/linux_networking/pull/5
* add from __future_\_ import print_function for python2
* python3 uses import _thread
* L suffix is not allowed in python3
* use 2to3 to convert print/except/raise/lambda for python3
* multi_interface_roam/package.xml: use format3 for python3
* Revert "build/testing fixes for noetic compatibility (`#5 <https://github.com/pr2/linux_networking/issues/5>`_)" (`#7 <https://github.com/pr2/linux_networking/issues/7>`_)
  This reverts commit a0282c1c0cc1ca883694c074c5daff832cc429b1.
* build/testing fixes for noetic compatibility (`#5 <https://github.com/pr2/linux_networking/issues/5>`_)
  * updated python scripts for python3 conventions (melodic/noetic compatibility)
  * added python-twisted-core as a test dependency
  * fixed python-twisted-core dependency for python3-twisted to make work with python3
  Co-authored-by: Michael Görner <me@v4hn.de>
* Contributors: Dave Feil-Seifer, Kei Okada

1.0.16 (2019-11-08)
-------------------
* Merge pull request `#4 <https://github.com/pr2/linux_networking/issues/4>`_ from k-okada/add_travis
  update travis.yml
* rm *.pyc
* add python-twisted-core to multi_interface_roam to pass the test
* Contributors: Kei Okada

1.0.15 (2019-03-19)
-------------------

1.0.13 (2019-03-18)
-------------------

1.0.12 (2019-02-26)
-------------------
* removed roslib declaration
* Contributors: TheDash

1.0.9 (2014-10-14)
------------------

1.0.8 (2014-10-10)
------------------
* Removed rosbuild files
* Contributors: TheDash

1.0.7 (2014-10-10)
------------------

1.0.6 (2014-10-10)
------------------

1.0.5 (2014-10-06)
------------------

1.0.4 (2014-10-03)
------------------

1.0.3 (2014-10-03)
------------------

1.0.2 (2014-10-03)
------------------
