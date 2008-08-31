%define name    qelectrotech
%define version 0.11
#define rel     r392
%define release 1

Summary: Tools to do electric scheme
Name: %{name}
Version: %{version}
Release: %mkrel %{release}
License: GPLv2+
Group: Graphical desktop/KDE
URL: http://qelectrotech.tuxfamily.org/index.html
Source0: %{name}-%{version}.tar.bz2
Patch0: fix_qelectrotech_pro.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: qt4-devel

%description
%{name} is a tool to do electrics scheme.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
perl -i -pe "s|/usr/local/|$RPM_BUILD_ROOT/usr/|g" qelectrotech.pro
qmake
make

%install
rm -rf $RPM_BUILD_ROOT
make install

# remove useless file
rm -rf $RPM_BUILD_ROOT/usr/doc

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CREDIT LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/mime/application/x-qet-element.xml
%{_datadir}/mime/application/x-qet-project.xml
%{_datadir}/mimelnk/application/x-qet-element.desktop
%{_datadir}/mimelnk/application/x-qet-project.desktop
%{_mandir}/fr.ISO8859-1/man1/%{name}.1.lzma
%{_mandir}/man1/%{name}.1.lzma
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/qet.png


