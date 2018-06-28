
Debian
====================
This directory contains files used to package cubd/cub-qt
for Debian-based Linux systems. If you compile cubd/cub-qt yourself, there are some useful files here.

## cub: URI support ##


cub-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install cub-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your cubqt binary to `/usr/bin`
and the `../../share/pixmaps/cub128.png` to `/usr/share/pixmaps`

cub-qt.protocol (KDE)

