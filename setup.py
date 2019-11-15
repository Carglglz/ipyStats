from setuptools import setup

setup(name='ipyStats',
      version='0.0.1',
      description='Python bindings for iStats',
      url='http://github.com/cgglz/ipyStats',
      author='Carlos Gil Gonzalez',
      author_email='carlosgilglez@gmail.com',
      license='MIT',
      packages=['ipyStats'],
      zip_safe=False,
      include_package_data=True,
      scripts=['ipyStats_dir/bin/ipyStats'])
