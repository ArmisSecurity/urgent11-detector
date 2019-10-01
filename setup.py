import os.path
import setuptools


here = os.path.abspath(os.path.dirname(__file__))

long_description = """
## urgent11-detector
urgent11-detector is a tool to detect whether a device is running the Interpeak IPnet TCP/IP stack, and is thus at risk from the URGENT/11 vulnerabilities.

## Motivation
In light of recent discoveries (see https://armis.com/urgent11), we decided to develop a tool designed to detect whether a device is using Interpeak's IPnet TCP/IP stack, regardless of the RTOS that powers it.
The IPnet TCP/IP stack is the native, built-in stack for VxWorks since version 6.5, but it has been also been supported by a wide array of RTOSs in the past.
Detecting the underlying TCP/IP stack used by a device is a non-trivial task, and so by using this tool one can identify devices that are vulnerable to URGENT/11 vulnerabilities.

## How does it work?
This tool implements 4 unique methods of detection in the form of a TCP and ICMP fingerprints to a target host.
By calculating the sum of all the methods scores, we can determine with high precision whether a device runs an OS that relies on the IPnet TCP/IP stack and whether this OS is VxWorks.
Moreover, we also test whether the host is vulnerable to CVE-2019-12258, which is one of the URGENT/11 vulnerabilities that affects all VxWorks versions that use IPnet.
If a device is detected as running IPnet on VxWorks, and is NOT vulnerable to this CVE, one can deduce this device has been patched against the URGENT/11 vulnerabilities.
"""

setuptools.setup(
    name='urgent11-detector',
    version='0.1.0',
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
