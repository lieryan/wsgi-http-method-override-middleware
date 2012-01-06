import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = []

classifiers = [
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Programming Language :: Python',
    ],

setup(name='wsgi-http-method-override-middleware',
      version='0.1',
      description='A WSGI middleware that overrides HTTP request methods to '
                  'enable RESTfull support.',
      long_description=README + '\n\n' + CHANGES,
      classifiers=classifiers,
      author='Antoine Cezar',
      author_email='antoine.cezar@gmail.com',
      url='https://github.com/AntoineCezar/'
          'wsgi-http-method-override-middleware',
      keywords='wsgi middleware',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite='wsgi-http-method-override-middleware',
      )
