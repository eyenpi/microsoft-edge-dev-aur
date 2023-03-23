# microsoft-edge-dev-aur
As the microsoft edge dev package in the AUR is out of date, I write this workflow for myself to have the latest Edge browser on my Archlinux. It will automatically search for the newest package in micorosft repository and edit the PKGBUILD file every week at sunday.
## Download
clone the repository and then run the follwing comamnds:
```
cd microsoft-edge-dev-aur/microsoft-edge-dev-bin/
makepkg -si
```
## Update
```
cd microsoft-edge-dev-aur/microsoft-edge-dev-bin/
git pull
makepkg -si
```
