=============================================
Django Sites Microsoft Authentication Backend
=============================================


Simple app to enable Microsoft Account, Office 365 and Xbox Live authentcation
as a Django authentication backend that is compatible and configurable across multiple sites.


* Free software: MIT license
* Documentation: https://django-microsoft-auth.readthedocs.io.

Features
--------

* Provides Django authentication backend to do Microsoft authentication
  (including Microsoft accounts, Office 365 accounts and Azure AD accounts)
  and Xbox Live authentication.

* Provides Microsoft OAuth client to interfacing with Microsoft accounts

Python/Django support
---------------------

`django_sites_microsoft_auth` follows the same `support cycle as Django <https://www.djangoproject.com/download/#supported-versions>`_,
with one exception: no Python 2 support. If you absoutely need Python 2.7
support, everything should largely already work, but you may need to patch
`microsoft_auth.admin` and/or other files to get it to work.

Supported python versions:  3.5+

Supported Django version: 1.11 LTS, 2.1+

https://docs.djangoproject.com/en/stable/faq/install/#what-python-version-can-i-use-with-django

Note: Even though Django 1.11 LTS supports Python 3.4, I do not and you should
not either. Official support for 3.4 was dropped in March 2019.

Credits
-------

This package was created with Cookiecutter_ and the
`audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
