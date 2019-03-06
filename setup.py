from setuptools import setup

requirements = ['dxfgrabber', 'shapely']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest']

setup(
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    name='dxf2shapely',
    version='1.0',
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
