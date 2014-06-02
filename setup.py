from distutils.core import setup

setup(name='streetaddress',
      version='0.1.9',
      description='A Python port of the Perl address parser.',
      author='Mike Jensen, Ian Halpern',
      url='https://github.com/jjensenmike/python-streetaddress',
      keywords='streetaddress',
      packages=['streetaddress'],
      install_requires=['datadiff'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2',
          'Topic :: Security',
      ],
     )
