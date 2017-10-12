#!bin/bash

sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com \     67265eb522bdd6b1c69e66ed7fb8bee0a1f196a8

echo deb http://ppa.launchpad.net/pidgin-developers/ppa/ubuntu \     `lsb_release --short --codename` main | \
    sudo tee /etc/apt/sources.list.d/pidgin-ppa.list

apt-get install evince bluefish evolution pulseaudio pidgin vlc vlc-plugin-* sshfs ktorrent openoffice.org-writer openoffice.org-calc openoffice.org-impress

apt-get install sun-java6-jre sun-java6-plugin sun-java6-fonts flashplugin-nonfree

apt-get install gdebi-core python-vte gdebi libstdc++5 libnotify-bin

dpkg -i "skype 2.1.0.47.deb"
dpkg -i "pidgin facebook 1.60.deb"
dpkg -i "ubuntuzilla 4.7.4.deb"

ubuntuzilla.py -a install -p firefox

rm -r ~/.mozilla_backup*

apt-get purge gdebi-core python-vte gdebi libstdc++5 libnotify-bin

apt-get purge ubuntuzilla
apt-get autoremove
