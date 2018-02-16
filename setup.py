from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()

# some more details
CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    ]

# calling the setup function
setup(name='ncalt',
      version='2.0.0',
      description='A small ncat alternative',
      long_description=long_description,
      author='Jackf',
      author_email='jackf@gmail.com',
      license='MIT',
      packages=['ncalt'],
      classifiers=CLASSIFIERS,
      keywords='remote netcat ncat'
      )
