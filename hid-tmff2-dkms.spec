%global commit 11cca6d4e9b49ec3779573f68917e362e4d65d36
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_number 276
%global git_date 20241218T201126Z

Name:            hid-tmff2-dkms
Version:         r%{commit_number}.%{shortcommit}
Release:         %autorelease
Summary:         Linux kernel module (DKMS) for Thrustmaster T300RS, T248, TX, and TS-XW
License:         GPL-3.0
URL:             https://github.com/Kimplul/hid-tmff2
Source0:         %{url}/archive/%{commit}.tar.gz
Source1:         https://github.com/Kimplul/hid-tminit/archive/usb.tar.gz
BuildArch:       noarch

BuildRequires:   git
BuildRequires:   make
Requires(post):  dkms
Requires(preun): dkms
Requires:        kernel-devel-matched

Provides:       hid-tmff2-dkms = %{version}-%{release}
Conflicts:      hid-tmff2

%description
Linux kernel module for Thrustmaster T300RS, T248, TX, and TS-XW using DKMS.

%prep
%autosetup -n hid-tmff2-%{commit} -a 1
mv hid-tminit-usb/* deps/hid-tminit

%build
# No build step necessary for DKMS modules

%install
cd %{_builddir}/hid-tmff2-%{commit}/
mkdir -p %{buildroot}/usr/src/hid-tmff2-%{version}
cp -r dkms/dkms.conf %{buildroot}/usr/src/hid-tmff2-%{version}/dkms.conf

# Replace version in dkms.conf
sed -e "s/0.8/%{version}/" -i %{buildroot}/usr/src/hid-tmff2-%{version}/dkms.conf

cp -r * %{buildroot}/usr/src/hid-tmff2-%{version}/

%post
dkms add -m hid-tmff2 -v %{version}
dkms build -m hid-tmff2 -v %{version}
dkms install -m hid-tmff2 -v %{version}

%preun
dkms remove -m hid-tmff2 -v %{version} --all

%files
%dir /usr/src/hid-tmff2-%{version}/
/usr/src/hid-tmff2-%{version}/*

%changelog
* Sun Dec 15 2024 Krzysztof Nasuta <krzysztof@nasuta.dev> - 0-1
- Initial package for Fedora.
