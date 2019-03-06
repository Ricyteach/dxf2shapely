from setuptools import setup

requirements = ['dxfgrabber']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    name='dxf2shapely',
    version='0.1',
    packages=['dxf2shapely'],
    url='https://github.com/Ricyteach/dxf2shapely',
    install_requires=requirements,
    license='MIT',
    author='Ricky L Teachey Jr',
    author_email='ricky@teachey.org',
    description='Very limited tool for grabbing line segments from pre-curated dxf files and turning them into shapely Polygons. ',
    test_suite = 'tests',
    tests_require = test_requirements,
)
