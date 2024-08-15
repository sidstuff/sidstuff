arch-chroot . << EOF
MYVAR="world"
. <(curl -s https://raw.githubusercontent.com/sidstuff/sidstuff/master/chroot.sh)
EOF
