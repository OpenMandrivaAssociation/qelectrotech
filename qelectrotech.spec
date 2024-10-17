Summary:	A tool to design electric diagrams
Name:		qelectrotech
Epoch:		2
Version:	0.22
Release:	4
License:	GPLv2+
Group:		Sciences/Other
URL:		https://qelectrotech.tuxfamily.org/index.html
Source0:	%{name}-%{version}-src.tar.gz
Source1:	qelectrotech.xml
Patch0:		fix_qelectrotech_pro.patch
Patch1:		add_to_change_to_pro.patch
BuildRequires:	qt4-devel
BuildRequires:	desktop-file-utils

%description
%{name} is a tool to design electric diagrams.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1

%build
perl -i -pe "s|COMPIL_PREFIX_TO_CHANGE|/usr/|g" qelectrotech.pro
perl -i -pe "s|INSTALL_PREFIX_TO_CHANGE|%{buildroot}/usr/|g" qelectrotech.pro
qmake
make

%install
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
mkdir -p %{buildroot}%{_datadir}/mime/packages/
install %{SOURCE1} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

# remove useless file
rm -rf %{buildroot}/usr/doc
rm -rf %{buildroot}%{_datadir}/mime/application/x-qet-element.xml
rm -rf %{buildroot}%{_datadir}/mime/application/x-qet-project.xml
rm -rf %{buildroot}%{_datadir}/mimelnk/application/x-qet-element.desktop
rm -rf %{buildroot}%{_datadir}/mimelnk/application/x-qet-project.desktop

%files
%doc CREDIT ELEMENTS.LICENSE INSTALL LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/es/man1/%{name}.1.*
%{_mandir}/fr.ISO8859-1/man1/%{name}.1.*
%{_mandir}/fr.UTF-8/man1/%{name}.1.*
%{_mandir}/fr/man1/%{name}.1.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/pt/man1/%{name}.1.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/mimetypes/*.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/mimetypes/*.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/mimetypes/*.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/mimetypes/*.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/mimetypes/*.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/mimetypes/*.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/mimetypes/*.png

