########
mcs-docs
########

Create pot files from rst
=========================

.. code-block:: bash

    sphinx-build -b gettext doc locale/ru

Create/update po from pot files
===============================

.. code-block:: bash

    sphinx-intl update -p locale/ru -d locale -l en

Build documentation to output
=============================

.. code-block:: bash

    python -m sphinx doc output -c .
