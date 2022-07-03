# LINUX TASK 1
## The tasks are located in the separate file
### Task1

**cat /etc/group | cut -d : -f 1,3 | grep -w '[0-9]\|[0-9][0-9]\|[0-9][0-9][0-9]$' > linux01.txt**
**cat /etc/group | cut -d : -f 1,3 | egrep -w '[0-9]{1,3}$'**

root:0
daemon:1
bin:2
sys:3
adm:4
tty:5
disk:6
lp:7
mail:8
news:9
uucp:10
man:12
proxy:13
kmem:15
dialout:20
fax:21
voice:22
cdrom:24
floppy:25
tape:26
sudo:27
audio:29
dip:30
www-data:33
backup:34
operator:37
list:38
irc:39
src:40
gnats:41
shadow:42
utmp:43
video:44
sasl:45
plugdev:46
staff:50
games:60
users:100
systemd-journal:101
systemd-network:102
systemd-resolve:103
systemd-timesync:104
crontab:105
messagebus:106
input:107
kvm:108
render:109
syslog:110
tss:111
bluetooth:112
ssl-cert:113
uuidd:114
tcpdump:115
avahi-autoipd:116
rtkit:117
ssh:118
netdev:119
lpadmin:120
avahi:121
scanner:122
saned:123
nm-openvpn:124
whoopsie:125
colord:126
geoclue:127
pulse:128
pulse-access:129
gdm:130
sssd:131
lxd:132
sambashare:133
systemd-coredump:999
vboxsf:998

### Task2
**sudo find -group mike -type d > linux02.txt**
**sudo find -group mike -type f >> linux02.txt**
**sudo find -user mike -type d >> linux02.txt**
**sudo find -user mike -type f >> linux02.txt**

.
./.ssh
./Pictures
./Public
./snap
./snap/vlc
./snap/vlc/common
./snap/vlc/common/.cache
./snap/vlc/common/.cache/gio-modules
./snap/vlc/common/.cache/fontconfig
./snap/vlc/2344
./snap/vlc/2344/.config
./snap/vlc/2344/.config/gtk-2.0
./snap/vlc/2344/.config/vlc
./snap/vlc/2344/.config/gtk-3.0
./snap/vlc/2344/.config/dconf
./snap/vlc/2344/.config/ibus
./snap/vlc/2344/.config/fontconfig
./snap/vlc/2344/.local
...

### Task3
**sudo grep -rI "#\!/bin/bash" /home/mike/ > /tmp/linux03.txt**

/home/mike/script1.sh:#!/bin/bash
/home/mike/opswatclient_deb/setup.sh:#!/bin/bash
/home/mike/script2.sh:#!/bin/bash
/home/mike/script3.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/script1.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/opswatclient_deb/setup.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/script2.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/script3.sh:#!/bin/bash

### Task4
**find -user mike -type f -exec grep -I "#\!/bin/bash" {} \; > /tmp/linux04.txt**


/home/mike/script1.sh:#!/bin/bash
/home/mike/opswatclient_deb/setup.sh:#!/bin/bash
/home/mike/script2.sh:#!/bin/bash
/home/mike/script3.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/script1.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/opswatclient_deb/setup.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/script2.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/script3.sh:#!/bin/bash
/home/mike/script1.sh:#!/bin/bash
/home/mike/opswatclient_deb/setup.sh:#!/bin/bash
/home/mike/script2.sh:#!/bin/bash
/home/mike/script3.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/script1.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/opswatclient_deb/setup.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/script2.sh:#!/bin/bash
/home/mike/linux03.txt:/home/mike/script3.sh:#!/bin/bash

### Task5
**find . -type f -name "*.txt" | grep -Ir "world" > /tmp/linux05.txt**


snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "argos_pew.worldwidemann.com": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "chromium-freeworld.desktop": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "com.endlessm.world_literature.en": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "com.teeworlds.Teeworlds": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "com.teeworlds.Teeworlds.desktop": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "com.worldoftanks.Client": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "gworldclock.desktop": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "io.snapcraft.hello-world-buPKUD3TKqCOgLEjjHx5kSiCpIs5cMuQ": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "io.snapcraft.teeworlds-unofficial-E2WGh0ZW9IMUHwjpP1FJNMBwpNDucxtD": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "io.snapcraft.ultrastar-worldparty-PxAYy6svZQinPWNYheCyADRqYKNl6YHN": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "io.snapcraft.usdxworldparty-Xv3Wh1LJh8ImjuTH4td39IAooXac9Ns5": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "io.snapcraft.worldofpadman-iFCj1JUE6jFvzfQ5ejreTLapJO7KF0aH": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "org.kde.plasma.worldmap": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "teeworlds.desktop": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "tworld.desktop": {
snap/snap-store/common/.cache/gnome-software/odrs/ratings.json:    "worldofpadman.desktop": {
.cache/mozilla/firefox/sk1o1ewo.default-release/personality-provider/nb_model_build_attachment_health.json:{"classes": [{"log_prior": -0.688156083, "feature_log_probs": [-6.387406692, -5.667677268, -6.921182784, -6.480194674, -6.466815139, -6.826139528, -6.75603859, -6.785382671, ...

### Task6
**find . -type f -size 1M -print0 | xargs -0 md5sum | sort | uniq -w32 --all-repeated=separate > linux06.txt**


061d90de791cfe3be3ea8346980568b5  ./snap/snap-store/558/.config/user-dirs.dirs
061d90de791cfe3be3ea8346980568b5  ./snap/vlc/2344/.config/user-dirs.dirs

0bb40aa1f3103eccc8b75f5b2e59fe51  ./.cache/mesa_shader_cache/ab/f947e36025bce6235980cefc9b6e3fcb94da19
0bb40aa1f3103eccc8b75f5b2e59fe51  ./.cache/mesa_shader_cache/d5/b8a5d0c1fa969ca3f160212a4e72269cfa5757

2bf6ff815e43fff74544416742bbf888  ./.config/libreoffice/4/user/extensions/bundled/registry/com.sun.star.comp.deployment.configuration.PackageRegistryBackend/backenddb.xml
2bf6ff815e43fff74544416742bbf888  ./.config/libreoffice/4/user/extensions/shared/registry/com.sun.star.comp.deployment.configuration.PackageRegistryBackend/backenddb.xml
2bf6ff815e43fff74544416742bbf888  ./.config/libreoffice/4/user/extensions/tmp/registry/com.sun.star.comp.deployment.configuration.PackageRegistryBackend/backenddb.xml
2bf6ff815e43fff74544416742bbf888  ./.config/libreoffice/4/user/uno_packages/cache/registry/com.sun.star.comp.deployment.configuration.PackageRegistryBackend/backenddb.xml
...

### Task7
**find -L . -samefile /home/mike/linux01.txt > linux07.txt**

./linux01.txt

### Task8
**find . -samefile /home/mike/linux01.txt > linux08.txt**


./linux01.txt

### Task9
**find -L . -mount -inum 670957**

./love1.txt
./love.txt

### Task10
**find -L . -inum 670957**

./love1.txt
./love.txt

### Task11
**find -L . -samefile love.txt -exec rm {} \;**

### Task12
**find . -type f -print0 | xargs -0 chmod 644**

### Task13
**diff -r -u -q /home/mike /root**

### Task14
**ip link show**

### Task15
**who**

### Task16
**ss -atH | cut -d " " -f 1 | uniq -ci**

### Task17
**ln -sf new_file.txt my_link.txt**

### Task18
**cat test1 | xargs -n2 sh -c 'mkdir $1 2>/dev/null; ln -r -s $0 $1'**
$0 - target file 
$1 - name of the link

test1
./file1.txt ./test18/
./file2.txt ./test18/
./file3.txt ./test18/

### Task19
**rsync -a /home/mike/temporary/ /home/mike/testdir/**
**cp -an /home/mike/temporary/ /home/mike/testdir/**

##20 N/A

### Task21
**cp -pr  /home/mike/temporary/ /home/mike/testdir/**

### Task22
**find . -type l -exec bash -c 'realpath "{}" && ln -f "$(realpath "{}")" "{}"' \;**


### Task23
**find -type f -links +1 -print0 | xargs -I {} -0 ln -s {}**

### Task24 
**find . -xtype l -exec rm {} ;**

### Task25 
-j	 bzip2.
-v	Action protocol — displaying the list of objects for action
-x,     --extract, --get 
-f      From file

tar, gz ----- **tar -C /home/user -xvf archive.tar.gz**
bz2, ----- **tar -C /home/user -xvjf archive.tar.bz2**
lzma ----- **tar -C /home/user --lzma -xvf compressed-file-name.lzma**
lz -----   **tar -C /home/user -xf backup.tar.xz**
z -----    **uncompress file.Z**

### Task26
**tar -czvfp name-of-archive.tar.gz /path/to/directory-or-file**

Here’s what those switches actually mean:
-c: Create an archive.
-z: Compress the archive with gzip.
-v: Display progress in the terminal while creating the archive, also known as “verbose” mode. The v is always optional in these commands, but it’s helpful.
-f: Allows you to specify the filename of the archive.
-p:  --preserve-permissions
extract information about file permissions 

### Task27***
**cd $1/.. && name=`basename $1` find $name -type f > /tmp/excluded tar -c --exclude-from=/tmp/excluded $name | tar -C $2 -x rm /tmp/excluded**
$1 - sourse dirictory $2 - tination dirictory

### Task28
**less /etc/passwd | cut -d: -f1 /etc/passwd | sort**

### Task29
**getent passwd {0..1000} | cut -d: -f1,3 | sort -f2**

##Task30 N/A

### Task31
**cat /etc/passwd | grep -E 'nologin|false' | cut -d ":" -f 1**
**cat /etc/passwd | grep -v 'nologin'| grep -v 'false' | cut -d ":" -f 1**
grep:
-v, --invert-match, Invert the sense of matching, to select non-matching lines.
-E, --extended-regexp, Interpret PATTERNS as extended regular  expressions .


### Task32
Don't have terminal
**cat /etc/passwd | grep -E 'nologin|false' | cut -d ":" -f 1,7**
Have terminal:
**cat /etc/passwd | grep -v 'nologin'| grep -v 'false' | cut -d ":" -f 1,7**

### Task33
**curl -s https://www.ukr.net/ | grep -o -E 'href="(http[^"#]+)"'**
**wget https://www.ukr.net/  | grep -o -E 'href="(http[^"#]+)"'**
grep:
-o, --only-matching, Print  only  the  matched  (non-empty) parts of a matching line, with each such part on a separate output line.
curl:
-s, --silent, Silent  or  quiet  mode. Don't show progress meter or error messages.  Makes Curl mute.

### Task34***
**ps -A -o etime=, -o comm= | xargs -I {} if grep -Fq "string" {} ; then killall $1 ; fi  **

### Task35***
List of files: ~/task35/touch text1.txt,text2.txt,test2.txt,text1.jpeg,text2.jpeg,test3.jpeg
**for prefix in $(find ./ -type f | grep -o -P '(?<=\/)[^\/]+(?=\.(jpeg))'); do if ! [[ -n $(find ./ -type f -name "$prefix*.txt") ]]; then find ./ -type f -name "$prefix*.jpeg" | sudo xargs rm ; fi; done**

### Task36 
Find your IP address using the command line
**hostname -I **

hostname - show or set the system's host name
-I, --all-ip-addresses, Display  all  network addresses of the host. This option enumerates all configured addresses on  all  network  interfaces. 

### Task37 
**grep  -E "([0-9]+(\.[0-9]+){3})" access.txt **
**grep -E "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" access.txt**

### Task38***
**printf "List of all available hosts from file: \n$(for ip_address in $(cat host-server.txt | grep -oE '((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])' | sort | uniq ); do [ $(ping -qc 5 $ip_address | grep "packet loss" | cut -d'%' -f 1 | cut -d "," -f 3 | xargs) -lt '10' ] && echo $ip_address; done)\n"**

 ##Task39 N/A

### Task40 
**nmap --script ssl-cert -p 443 google.com | grep "Subject Alternative Name" | xargs -n1 | cut -d ":" -f 2**

--script filename|category|directory|expression[,...],    Runs a script scan using the comma-separated list of filenames, script categories, and directories. Each element in the list may also be a Boolean expression describing a more complex set of scripts. Each element is interpreted first as an expression, then as a category, and finally as a file or directory name.