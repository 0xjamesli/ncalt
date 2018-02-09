from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()

# some more details
CLASSIFIERS = [
    'Development Status :: 1 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ]

# calling the setup function
setup(name='ncalt',
      version='1.0.0',
      description='A small ncat alternative',
      long_description=long_description,
      author='Hank Jack',
      author_email='hank@gmail.com',
      license='MIT',
      packages=['ncalt'],
      classifiers=CLASSIFIERS,
      keywords='remote netcat ncat'
      )
