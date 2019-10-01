from io import open
import os.path
import setuptools


here = os.path.abspath(os.path.dirname(__file__))


# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name='urgent11-detector',
    version='0.1.1',
    description='URGENT/11 detection tool by Armis',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ArmisSecurity/urgent11-detector',
    author='Armis Inc.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Topic :: Security',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='windriver vxworks rtos interpeak ipnet urgent/11 urgent11 armis',
    py_modules=['urgent11_detector'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['python-iptables', 'scapy'],
    entry_points={
        'console_scripts': [
            'urgent11-detector=urgent11_detector:main',
        ],
    },
    project_urls={
        'Armis': 'http://armis.com',
        'Bug Reports': 'https://github.com/ArmisSecurity/urgent11-detector/issues',
    },
)
