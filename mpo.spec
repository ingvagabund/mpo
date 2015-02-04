%global commit		1f8da0e97ccb6b31b01b0ccf356f6ea4c138b681
%global shortcommit	%(c=%{commit}; echo ${c:0:7})

Name:		mpo
Version:	0
Release:	1%{?dist}
Summary:	Tool for packaging of man-pages-overrides
License:	GPLv2+
URL:		https://github.com/ingvagabund/mpo
Source0:	https://github.com/ingvagabund/mpo/archive/%{commit}/mpo-%{shortcommit}.tar.gz

%description
Tool to automize packaging of man-pages-overrides.

%prep
%setup -q -n mpo-%{commit}

%build

%install
# copy bash completition
#mkdir -p %{buildroot}/etc/bash_completion.d/
#cp completions/bash/mpo %{buildroot}/etc/bash_completion.d/.
# copy man page
#mkdir -p %{buildroot}/usr/share/man/man1
#cp man/mpo.1 %{buildroot}/usr/share/man/man1/man.1.gz
# copy scripts
mkdir -p %{buildroot}/usr/share/mpo
cp *.sh %{buildroot}/usr/share/mpo/.
cp *.py %{buildroot}/usr/share/mpo/.
# copy config
#mkdir -p %{buildroot}/usr/share/mpo/config
#cp config/mpo.conf %{buildroot}/usr/share/mpo/config/.
# copy the tool script
cp mpo %{buildroot}/usr/share/mpo/.

%post
# make a symlink to mpo
ln -s /usr/share/mpo/mpo /usr/bin/mpo

%preun
rm /usr/bin/mpo

%files
%doc README.md LICENSE
#/etc/bash_completion.d/mpo
%dir /usr/share/mpo
/usr/share/mpo/*
#%config /usr/share/mpo/config
#/usr/share/man/man1/mpo.1.gz

%changelog
* Wed Feb 04 2015 Jan Chaloupka <jchaloup@redhat.com> - 0-1
- Initial commit of the package



