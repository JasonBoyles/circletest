from distutils.core import setup

setup(name='circletest',
      description='a CLI CircleCI client to trigger tests and report status',
      version='0.1',
      author='Rackspace',
      author_email='jason@duncancreek.net',
      license='Apache License (2.0)',
      classifiers=["Programming Language :: Python"],
      url='https://github.com/JasonBoyles/circletest',
      scripts=['circletest'],
      install_requires=[
          'circleclient',
          'mock',
      ]
      )
