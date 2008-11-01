%define name    qelectrotech
%define version 0.11
#define rel     r398
%define release 8

Summary: A tool to design electric diagrams
Name: %{name}
Version: %{version}
Release: %mkrel %{release}
License: GPLv2+
Group: Sciences/Other
URL: http://qelectrotech.tuxfamily.org/index.html
Source0: %{name}-%{version}-src.tar.gz
Source1: man_fr_utf8.tar.bz2
Source2: qelectrotech.xml
Patch0: fix_qelectrotech_pro.patch
Patch1: fix_manpage.patch
Patch2: add_to_change_to_pro.patch
Patch3: fix_contextual_menu.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: qt4-devel
BuildRequires: desktop-file-utils

%description
%{name} is a tool to design electric diagrams.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

%build
tar xjf %{SOURCE1}
perl -i -pe "s|COMPIL_PREFIX_TO_CHANGE|/usr/|g" qelectrotech.pro
perl -i -pe "s|INSTALL_PREFIX_TO_CHANGE|$RPM_BUILD_ROOT/usr/|g" qelectrotech.pro
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

# add the association file
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mime/packages/
install %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/mime/packages/%{name}.xml

# remove useless file
rm -rf $RPM_BUILD_ROOT/usr/doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime/application/x-qet-element.xml
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime/application/x-qet-project.xml
rm -rf $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/x-qet-element.desktop
rm -rf $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/x-qet-project.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CREDIT LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/fr.ISO8859-1/man1/%{name}.1.lzma
%{_mandir}/fr.UTF-8/man1/%{name}.1.lzma
%{_mandir}/man1/%{name}.1.lzma
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/qet.png
