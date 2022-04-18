#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBE793007AD22DF7E (tsujan2000@gmail.com)
#
Name     : lxqt-session
Version  : 1.1.0
Release  : 14
URL      : https://github.com/lxqt/lxqt-session/releases/download/1.1.0/lxqt-session-1.1.0.tar.xz
Source0  : https://github.com/lxqt/lxqt-session/releases/download/1.1.0/lxqt-session-1.1.0.tar.xz
Source1  : https://github.com/lxqt/lxqt-session/releases/download/1.1.0/lxqt-session-1.1.0.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: lxqt-session-bin = %{version}-%{release}
Requires: lxqt-session-data = %{version}-%{release}
Requires: lxqt-session-license = %{version}-%{release}
Requires: lxqt-session-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kwindowsystem-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : liblxqt-dev
BuildRequires : lxqt-build-tools
BuildRequires : pkg-config
BuildRequires : pkgconfig(libprocps)
BuildRequires : pkgconfig(libudev)
BuildRequires : qtbase-dev
BuildRequires : qttools-dev
BuildRequires : qtx11extras-dev
BuildRequires : systemd-dev
BuildRequires : xdg-user-dirs

%description
# lxqt-session
## Overview
### General
Repository lxqt-session is providing tools to handle LXQt sessions.

%package bin
Summary: bin components for the lxqt-session package.
Group: Binaries
Requires: lxqt-session-data = %{version}-%{release}
Requires: lxqt-session-license = %{version}-%{release}

%description bin
bin components for the lxqt-session package.


%package data
Summary: data components for the lxqt-session package.
Group: Data

%description data
data components for the lxqt-session package.


%package license
Summary: license components for the lxqt-session package.
Group: Default

%description license
license components for the lxqt-session package.


%package man
Summary: man components for the lxqt-session package.
Group: Default

%description man
man components for the lxqt-session package.


%prep
%setup -q -n lxqt-session-1.1.0
cd %{_builddir}/lxqt-session-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650312881
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1650312881
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxqt-session
cp %{_builddir}/lxqt-session-1.1.0/LICENSE %{buildroot}/usr/share/package-licenses/lxqt-session/7fab4cd4eb7f499d60fe183607f046484acd6e2d
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lxqt-config-session
/usr/bin/lxqt-leave
/usr/bin/lxqt-session
/usr/bin/startlxqt

%files data
%defattr(-,root,root,-)
/usr/share/applications/lxqt-config-session.desktop
/usr/share/applications/lxqt-hibernate.desktop
/usr/share/applications/lxqt-leave.desktop
/usr/share/applications/lxqt-lockscreen.desktop
/usr/share/applications/lxqt-logout.desktop
/usr/share/applications/lxqt-reboot.desktop
/usr/share/applications/lxqt-shutdown.desktop
/usr/share/applications/lxqt-suspend.desktop
/usr/share/lxqt/lxqt.conf
/usr/share/lxqt/session.conf
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_ar.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_arn.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_ast.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_bg.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_ca.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_cs.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_cy.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_da.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_de.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_el.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_eo.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_es.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_es_UY.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_es_VE.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_et.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_eu.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_fi.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_fr.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_gl.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_he.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_hr.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_hu.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_ia.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_id.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_it.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_ja.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_ko.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_lt.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_nb_NO.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_nl.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_oc.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_pl.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_pt.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_pt_BR.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_ro_RO.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_ru.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_si.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_sk_SK.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_sl.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_sr@latin.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_sr_RS.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_th_TH.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_tr.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_uk.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_zh_CN.qm
/usr/share/lxqt/translations/lxqt-config-session/lxqt-config-session_zh_TW.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_ar.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_arn.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_ast.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_bg.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_ca.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_cs.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_cy.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_da.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_de.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_el.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_es.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_et.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_fi.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_fr.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_gl.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_he.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_hr.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_hu.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_id.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_it.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_ja.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_ko.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_lt.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_nb_NO.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_nl.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_pl.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_pt.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_pt_BR.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_ru.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_si.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_sk.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_sl.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_tr.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_uk.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_vi.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_zh_CN.qm
/usr/share/lxqt/translations/lxqt-leave/lxqt-leave_zh_TW.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_ar.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_arn.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_ast.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_bg.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_ca.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_cs.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_cy.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_da.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_de.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_el.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_eo.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_es.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_es_UY.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_es_VE.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_et.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_eu.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_fi.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_fr.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_gl.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_he.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_hr.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_hu.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_ia.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_id.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_it.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_ja.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_ko.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_lt.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_nb_NO.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_nl.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_or.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_pl.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_pt.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_pt_BR.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_ro_RO.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_ru.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_si.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_sk_SK.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_sl.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_sr@latin.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_sr_BA.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_sr_RS.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_th_TH.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_tr.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_uk.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_zh_CN.qm
/usr/share/lxqt/translations/lxqt-session/lxqt-session_zh_TW.qm
/usr/share/lxqt/windowmanagers.conf
/usr/share/xsessions/lxqt.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lxqt-session/7fab4cd4eb7f499d60fe183607f046484acd6e2d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lxqt-config-session.1
/usr/share/man/man1/lxqt-leave.1
/usr/share/man/man1/lxqt-session.1
/usr/share/man/man1/startlxqt.1
