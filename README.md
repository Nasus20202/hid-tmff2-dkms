# Fedora COPR for [hid-tmff2](https://github.com/Kimplul/hid-tmff2)

[COPR repository](https://copr.fedorainfracloud.org/coprs/nasus/hid-tmff2-dkms/) the [hid-tmff2](https://github.com/Kimplul/hid-tmff2) kernel module with DKMS support.

[![Copr build status](https://copr.fedorainfracloud.org/coprs/nasus/hid-tmff2-dkms/package/hid-tmff2-dkms/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/nasus/hid-tmff2-dkms/package/hid-tmff2-dkms/)

## Installation

Enable this repository:

```bash
sudo dnf copr enable nasus/hid-tmff2-dkms
```

Install the DKMS module:

```bash
sudo dnf install hid-tmff2-dkms
```
Now the module should be register in DKMS. It will be automatically built for new current kernel.

_Optional:_ If you want to load the module automatically on boot, you can add it to the `systemd-modules-load` service. 

`/etc/modules-load.d/hid-tmff2.conf`
```
hid_tmff_new
hid_tminit_new
usb_tminit_new
```
