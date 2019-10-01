![urgent11-detector](https://github.com/ArmisSecurity/urgent11-detector/raw/master/docs/logo.png)

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

## Getting Started
Install the tool directly with pip (or pip3):
```
pip install urgent11-detector
```
And than run it like this:
```
urgent11-detector IP PORT
```

Alternatively, you can install the [dependencies](#dependencies) and run it manually
```
./urgent11-detector.py IP PORT
```


#### Dependencies
The only dependencies are scapy and python-iptables, install them using:
```
pip install scapy python-iptables
```
or on Python 3.X:
```
pip3 install scapy python-iptables
```
or advice the formal [scapy installation guide](https://scapy.readthedocs.io/en/latest/installation.html)
and the formal [python-iptables documentation](https://github.com/ldx/python-iptables#installing)

## License
Copyright 2019 Armis.

Licensed under the GNU Affero General Public License, Version 3.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[https://www.gnu.org/licenses/agpl-3.0.txt](https://www.gnu.org/licenses/agpl-3.0.txt)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.