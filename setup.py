from setuptools import setup, find_packages
import sys, os

version = '0.9.3'

setup(name='mobile.sniffer',
      version=version,
      description="Mobile browser feature detection using multiple backends",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='mobile django plone user-agent http sniffer',
      author='mFabrik Research Oy',
      author_email='research@mfabrik.com',
      url='http://mfabrik.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['mobile'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'setuptools',
          'python-Levenshtein'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
