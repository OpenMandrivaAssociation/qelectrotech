%define name    qelectrotech
%define version 0.11
#define rel     r398
%define release 4

Summary: Tools to do electric scheme
Name: %{name}
Version: %{version}
Release: %mkrel %{release}
License: GPLv2+
Group: Graphical desktop/KDE
URL: http://qelectrotech.tuxfamily.org/index.html
Source0: %{name}-%{version}-src.tar.gz
Source1: man_fr_utf8.tar.bz2
Patch0: fix_qelectrotech_pro.patch
Patch1: fix_manpage.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: qt4-devel
BuildRequires: desktop-file-utils

%description
%{name} is a tool to do electrics scheme.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
tar xjf %{SOURCE1}
perl -i -pe "s|/usr/local/|$RPM_BUILD_ROOT/usr/|g" qelectrotech.pro
qmake
make

%install
rm -rf $RPM_BUILD_ROOT
make install

desktop-file-install \
  --remove-category="Office" \
  --remove-category="Qt" \
  --remove-category="VectorGraphics" \
  --remove-category="Science" \
  --remove-category="Electricity" \
  --remove-category="Engineering" \
  --add-category="X-MandrivaLinux-MoreApplications-Sciences-Electricity" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

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
%{_mandir}/fr.UTF-8/man1/%{name}.1.lzma
%{_mandir}/man1/%{name}.1.lzma
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/qet.png


