# 👃🏾𝐏𝐂𝐊𝐓𝐒𝐍𝐈𝐅𝐅𝐘👃🏾
Packages sniffer, sites URL, login info and more!

<div align="center">
<a href="https://github.com/thepseudonym/pcktSniffy/" title="Go to GitHub repo">
  <img src="https://img.shields.io/static/v1?label=thepseudonym&message=pcktSniffy&color=purple&logo=github" alt="thepseudonym - pcktSniffy">
</a>
  <a href="https://discord.gg/VQUvAVpJPr" style="text-decoration: none;">
  <img src="https://discord.com/api/guilds/1336059889524670534/widget.png?style=shield" alt="Discord Shield"/>
</div>

![Screenshot_2025-03-28_15_02_55](https://github.com/user-attachments/assets/39d39f72-ec6a-4f34-b72c-39a00608e918)

# Requirements
1. [Python 3.13.0 or newer](https://www.python.org/downloads/)
2. [Scapy](https://pypi.org/project/scapy/)

# Usage
1. `cd pcktSniffy`
2. `sudo python3 pcktSniffy.py`
3. `And choose your interface fore example: eth0`

# HHTPS interception
1. `iptables -t nat -A PREROUTING -i eth0  -p tcp --destination-port 80 -j REDIRECT --to-port 10000`

# Works fine with
1. [arpSpoofy](https://github.com/thepseudonym/arpSpoofy/) `Must be already installed! for pcktSniffy😊`
2. [scanDetective](https://github.com/thepseudonym/scanDetective/)

# License
<a href="https://github.com/thepseudonym/pcktSniffy/blob/main/LICENSE" title="LICENSE">
  <img src="https://img.shields.io/static/v1?label=&message=LICENSE&color=blue&logo=github" alt="LICENSE"> 
</a>
