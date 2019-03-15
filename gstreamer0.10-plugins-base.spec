#
# Conditional build:
%bcond_with	apidocs		# disable gtk-doc
%bcond_without	gnomevfs	# don't build gnome-vfs plugin
%bcond_without	gnome		# disable gnome-vfs (alias)
%bcond_without	libvisual	# don't build libvisual plugin
%bcond_with	v4l1		# Video4Linux 1 plugin (for Linux < 2.6.35 or so)

%define		gstname		gst-plugins-base
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.36

%if %{without gnome}
%undefine	with_gnomevfs
%endif

%define		__gst_inspect /usr/bin/gst-inspect-0.10

Summary:	GStreamer Streaming-media framework base plugins
Summary(pl.UTF-8):	Podstawowe wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer0.10-plugins-base
Version:	0.10.36
Release:	8
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-base/%{gstname}-%{version}.tar.xz
# Source0-md5:	3d2337841b132fe996e5eb2396ac9438
Patch0:		sse-sse2-check.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
%{?with_apidocs:BuildRequires:	docbook-dtd412-xml}
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.24
BuildRequires:	glibc-misc
BuildRequires:	gobject-introspection-devel >= 0.9.12
BuildRequires:	gstreamer0.10-devel >= %{gst_req_ver}
BuildRequires:	gtk+2-devel >= 2:2.14.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.6}
BuildRequires:	iso-codes
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	orc-devel >= 0.4.11
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.1
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
##
## plugins
##
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	cdparanoia-III-devel >= 2:10.2
BuildRequires:	freetype-devel >= 2.1.2
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.15.3}
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libtheora-devel >= 1.1
%{?with_libvisual:BuildRequires:	libvisual-devel >= 0.4.0}
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	pango-devel >= 1:1.16.0
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	udev-glib-devel >= 143
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	zlib-devel
# old GIR format
BuildConflicts:	gstreamer-plugins-base-devel < 0.10.30
# breaks OGG/Vorbis plugin
BuildConflicts:	tremor-devel
Requires:	glib2 >= 1:2.24
Requires:	gstreamer0.10 >= %{gst_req_ver}
Suggests:	iso-codes
Obsoletes:	gstreamer-artsd
Obsoletes:	gstreamer-audio-effects
Obsoletes:	gstreamer-audiofile
Obsoletes:	gstreamer-avi
Obsoletes:	gstreamer-cdplayer
Obsoletes:	gstreamer-colorspace
Obsoletes:	gstreamer-festival
Obsoletes:	gstreamer-interfaces
Obsoletes:	gstreamer-interleave
Obsoletes:	gstreamer-kio
Obsoletes:	gstreamer-libdvdnav
Obsoletes:	gstreamer-libfame
Obsoletes:	gstreamer-media-info
Obsoletes:	gstreamer-mikmod
Obsoletes:	gstreamer-misc
Obsoletes:	gstreamer-oneton
Obsoletes:	gstreamer-play
Obsoletes:	gstreamer-plugins
Obsoletes:	gstreamer-qcam
Obsoletes:	gstreamer-snapshot
Obsoletes:	gstreamer-tcp
Obsoletes:	gstreamer-tuner
Obsoletes:	gstreamer-v4l
Obsoletes:	gstreamer-vbidec
Obsoletes:	gstreamer-videosink-xv
Obsoletes:	gstreamer-videotest
Obsoletes:	gstreamer-xine
Obsoletes:	gstreamer-xoverlay
Obsoletes:	gstreamer-yuv4mjpeg
Obsoletes:	gtk-loaders-gstreamer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}
%define		gstincludedir	%{_includedir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%description -l pl.UTF-8
GStreamer to środowisko obróbki danych strumieniowych, bazujące na
grafie filtrów operujących na danych medialnych. Aplikacje używające
tej biblioteki mogą robić wszystko od przetwarzania dźwięku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego związego z
mediami. Architektura bazująca na wtyczkach pozwala na łatwe dodawanie
nowych typów danych lub możliwości obróbki.

%package devel
Summary:	Include files for GStreamer streaming-media framework plugins
Summary(pl.UTF-8):	Pliki nagłówkowe do wtyczek środowiska obróbki strumieni GStreamer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.24
Requires:	gstreamer0.10-devel >= %{gst_req_ver}
Obsoletes:	gstreamer-interfaces-devel
Obsoletes:	gstreamer-media-info-devel
Obsoletes:	gstreamer-mixer-devel
Obsoletes:	gstreamer-navigation-devel
Obsoletes:	gstreamer-play-devel
Obsoletes:	gstreamer-plugins-devel
Obsoletes:	gstreamer-tuner-devel
Obsoletes:	gstreamer-xoverlay-devel

%description devel
Include files for GStreamer streaming-media framework plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do wtyczek środowiska obróbki strumieni GStreamer.

%package apidocs
Summary:	GStreamer streaming-media framework plugins API documentation
Summary(pl.UTF-8):	Dokumentacja API wtyczek środowiska obróbki strumieni GStreamer
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GStreamer streaming-media framework plugins API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API wtyczek środowiska obróbki strumieni GStreamer.

##
## Plugins
##

%package -n gstreamer0.10-audiosink-alsa
Summary:	GStreamer plugins for the ALSA sound architecture
Summary(pl.UTF-8):	Wtyczki GStreamera do obsługi architektury ALSA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer0.10-audiosink = %{version}
Obsoletes:	gstreamer-alsa
Obsoletes:	gstreamer-audiosink-alsa < 1.0
Obsoletes:	gstreamer-audiosink-alsaspdif

%description -n gstreamer0.10-audiosink-alsa
Input and output plugin for the ALSA soundcard driver architecture.

%description -n gstreamer0.10-audiosink-alsa -l pl.UTF-8
Wtyczka wejścia i wyjścia ze sterowników dźwiękowych architektury ALSA
do GStreamera.

%package -n gstreamer0.10-audio-effects-base
Summary:	GStreamer base audio effects plugins
Summary(pl.UTF-8):	Podstawowe wtyczki efektów dźwiękowych do GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	orc >= 0.4.11
Obsoletes:	gstreamer-audio-effects
Obsoletes:	gstreamer-audio-effects-base < 1.0

%description -n gstreamer0.10-audio-effects-base
GStreamer base audio effects plugins.

%description -n gstreamer0.10-audio-effects-base -l pl.UTF-8
Podstawowe wtyczki efektów dźwiękowych do GStreamera.

%package -n gstreamer0.10-cdparanoia
Summary:	GStreamer plugin for CD audio input using CDParanoia IV
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca płyty CD-Audio przy użyciu CDParanoia IV
Group:		Libraries
#Requires:	gstreamer >= %{gst_req_ver}
# for locales
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gstreamer-cdparanoia < 1.0

%description -n gstreamer0.10-cdparanoia
Plugin for ripping audio tracks using cdparanoia under GStreamer.

%description -n gstreamer0.10-cdparanoia -l pl.UTF-8
Wtyczka do ripowania ścieżek dźwiękowych pod GStreamerem za pomocą
cdparanoia.

%package -n gstreamer0.10-gnomevfs
Summary:	GStreamer plugins for GNOME VFS input and output
Summary(pl.UTF-8):	Wtyczki wejścia i wyjścia GNOME VFS do GStreamera
Group:		Libraries
#Requires:	gstreamer >= %{gst_req_ver}
# for locales
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gstreamer-gnomevfs < 1.0

%description -n gstreamer0.10-gnomevfs
Plugins for reading and writing through GNOME VFS.

%description -n gstreamer0.10-gnomevfs -l pl.UTF-8
Wtyczki do czytania i zapisywania poprzez GNOME VFS.

%package -n gstreamer0.10-libvisual
Summary:	GStreamer libvisual plugin
Summary(pl.UTF-8):	Wtyczka libvisual do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-libvisual < 1.0

%description -n gstreamer0.10-libvisual
GStreamer libvisual plugin.

%description -n gstreamer0.10-libvisual -l pl.UTF-8
Wtyczka libvisual do GStreamera.

%package -n gstreamer0.10-pango
Summary:	GStreamer pango plugins
Summary(pl.UTF-8):	Wtyczki pango do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-pango < 1.0

%description -n gstreamer0.10-pango
This package contains textoverlay and timeoverlay GStreamer plugins.

%description -n gstreamer0.10-pango -l pl.UTF-8
Ten pakiet zawiera wtyczki textoverlay i timeoverlay do GStreamera.

%package -n gstreamer0.10-theora
Summary:	GStreamer Ogg Theora plugin
Summary(pl.UTF-8):	Wtyczka Ogg Theora do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	libtheora >= 1.1
Obsoletes:	gstreamer-theora < 1.0

%description -n gstreamer0.10-theora
GStreamer Ogg Theora plugin.

%description -n gstreamer0.10-theora -l pl.UTF-8
Wtyczka Ogg Theora do GStreamera.

%package -n gstreamer0.10-video4linux
Summary:	GStreamer plugin for Video 4 Linux source
Summary(pl.UTF-8):	Wtyczka GStreamera dla źródła Video 4 Linux
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	udev-glib >= 143
Obsoletes:	gstreamer-video4linux < 1.0

%description -n gstreamer0.10-video4linux
GStreamer plugin for Video 4 Linux source.

%description -n gstreamer0.10-video4linux -l pl.UTF-8
Wtyczka GStreamera dla źródła Video 4 Linux.

%package -n gstreamer0.10-vorbis
Summary:	GStreamer plugin for encoding and decoding Ogg Vorbis audio files
Summary(pl.UTF-8):	Wtyczki do GStreamera kodujące i dekodujące pliki dźwiękowe Ogg Vorbis
Group:		Libraries
#Requires:	gstreamer >= %{gst_req_ver}
# for locales in ogg module
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gstreamer-vorbis < 1.0

%description -n gstreamer0.10-vorbis
Plugins for creating and playing Ogg Vorbis audio files.

%description -n gstreamer0.10-vorbis -l pl.UTF-8
Wtyczki do tworzenia i odtwarzania plików dźwiękowych Ogg Vorbis.

%package -n gstreamer0.10-imagesink-x
Summary:	GStreamer XFree86/X.org output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu XFree86/X.org dla GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer0.10-videosink = %{version}
Obsoletes:	gstreamer-imagesink-x < 1.0

%description -n gstreamer0.10-imagesink-x
Standard XFree86/X.org image sink.

%description -n gstreamer0.10-imagesink-x -l pl.UTF-8
Standardowa wtyczka wyjścia obrazu XFree86/X.org dla GStreamera.

%package -n gstreamer0.10-imagesink-xv
Summary:	GStreamer Xvideo output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu Xvideo dla GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gstreamer0.10-videosink = %{version}
Obsoletes:	gstreamer-imagesink-xv < 1.0

%description -n gstreamer0.10-imagesink-xv
XFree86/X.org image sink via Xvideo extension.

%description -n gstreamer0.10-imagesink-xv -l pl.UTF-8
Wtyczka wyjścia obrazu Xvideo dla GStreamera.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_gnomevfs:--disable-gnome_vfs} \
	%{!?with_libvisual:--disable-libvisual} \
	--disable-examples \
	--disable-silent-rules \
	--disable-static \
	--enable-experimental \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	--enable-orc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
%{__rm} $RPM_BUILD_ROOT%{gstlibdir}/*.la
# *.la for libs kept - no .private dependencies in *.pc

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_bindir}/gst-discoverer-0.10
%attr(755,root,root) %{_bindir}/gst-visualise-0.10
%attr(755,root,root) %{_libdir}/libgstapp-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstapp-0.10.so.0
%attr(755,root,root) %{_libdir}/libgstaudio-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstaudio-*.so.0
%attr(755,root,root) %{_libdir}/libgstcdda-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstcdda-*.so.0
%attr(755,root,root) %{_libdir}/libgstfft-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstfft-*.so.0
%attr(755,root,root) %{_libdir}/libgstinterfaces-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstinterfaces-*.so.0
%attr(755,root,root) %{_libdir}/libgstnetbuffer-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstnetbuffer-*.so.0
%attr(755,root,root) %{_libdir}/libgstpbutils-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstpbutils-*.so.0
%attr(755,root,root) %{_libdir}/libgstriff-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstriff-*.so.0
%attr(755,root,root) %{_libdir}/libgstrtp-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstrtp-*.so.0
%attr(755,root,root) %{_libdir}/libgstrtsp-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstrtsp-*.so.0
%attr(755,root,root) %{_libdir}/libgstsdp-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstsdp-*.so.0
%attr(755,root,root) %{_libdir}/libgsttag-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsttag-*.so.0
%attr(755,root,root) %{_libdir}/libgstvideo-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvideo-*.so.0
%{_mandir}/man1/gst-visualise-*.1*
# plugins with no external dependencies
%attr(755,root,root) %{gstlibdir}/libgstapp.so
%attr(755,root,root) %{gstlibdir}/libgstaudioconvert.so
%attr(755,root,root) %{gstlibdir}/libgstaudiorate.so
%attr(755,root,root) %{gstlibdir}/libgstaudiotestsrc.so
%attr(755,root,root) %{gstlibdir}/libgstdecodebin2.so
%attr(755,root,root) %{gstlibdir}/libgstdecodebin.so
%attr(755,root,root) %{gstlibdir}/libgstencodebin.so
%attr(755,root,root) %{gstlibdir}/libgstffmpegcolorspace.so
%attr(755,root,root) %{gstlibdir}/libgstgdp.so
%attr(755,root,root) %{gstlibdir}/libgstgio.so
%attr(755,root,root) %{gstlibdir}/libgstplaybin.so
%attr(755,root,root) %{gstlibdir}/libgstsubparse.so
%attr(755,root,root) %{gstlibdir}/libgsttcp.so
%attr(755,root,root) %{gstlibdir}/libgsttypefindfunctions.so
%attr(755,root,root) %{gstlibdir}/libgstvideorate.so
%attr(755,root,root) %{gstlibdir}/libgstvideoscale.so
%attr(755,root,root) %{gstlibdir}/libgstvideotestsrc.so
%{_libdir}/girepository-1.0/GstApp-0.10.typelib
%{_libdir}/girepository-1.0/GstAudio-0.10.typelib
%{_libdir}/girepository-1.0/GstFft-0.10.typelib
%{_libdir}/girepository-1.0/GstInterfaces-0.10.typelib
%{_libdir}/girepository-1.0/GstNetbuffer-0.10.typelib
%{_libdir}/girepository-1.0/GstPbutils-0.10.typelib
%{_libdir}/girepository-1.0/GstRiff-0.10.typelib
%{_libdir}/girepository-1.0/GstRtp-0.10.typelib
%{_libdir}/girepository-1.0/GstRtsp-0.10.typelib
%{_libdir}/girepository-1.0/GstSdp-0.10.typelib
%{_libdir}/girepository-1.0/GstTag-0.10.typelib
%{_libdir}/girepository-1.0/GstVideo-0.10.typelib
%{_datadir}/gst-plugins-base

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstapp-*.so
%attr(755,root,root) %{_libdir}/libgstaudio-*.so
%attr(755,root,root) %{_libdir}/libgstcdda-*.so
%attr(755,root,root) %{_libdir}/libgstfft-*.so
%attr(755,root,root) %{_libdir}/libgstinterfaces-*.so
%attr(755,root,root) %{_libdir}/libgstnetbuffer-*.so
%attr(755,root,root) %{_libdir}/libgstpbutils-*.so
%attr(755,root,root) %{_libdir}/libgstriff-*.so
%attr(755,root,root) %{_libdir}/libgstrtp-*.so
%attr(755,root,root) %{_libdir}/libgstrtsp-*.so
%attr(755,root,root) %{_libdir}/libgstsdp-*.so
%attr(755,root,root) %{_libdir}/libgsttag-*.so
%attr(755,root,root) %{_libdir}/libgstvideo-*.so
%{_libdir}/libgstapp-*.la
%{_libdir}/libgstaudio-*.la
%{_libdir}/libgstcdda-*.la
%{_libdir}/libgstfft-*.la
%{_libdir}/libgstinterfaces-*.la
%{_libdir}/libgstnetbuffer-*.la
%{_libdir}/libgstpbutils-*.la
%{_libdir}/libgstriff-*.la
%{_libdir}/libgstrtp-*.la
%{_libdir}/libgstrtsp-*.la
%{_libdir}/libgstsdp-*.la
%{_libdir}/libgsttag-*.la
%{_libdir}/libgstvideo-*.la
%{gstincludedir}/gst/app
%{gstincludedir}/gst/audio
%{gstincludedir}/gst/cdda
%{gstincludedir}/gst/fft
%{gstincludedir}/gst/floatcast
%{gstincludedir}/gst/interfaces
%{gstincludedir}/gst/netbuffer
%{gstincludedir}/gst/pbutils
%{gstincludedir}/gst/riff
%{gstincludedir}/gst/rtp
%{gstincludedir}/gst/rtsp
%{gstincludedir}/gst/sdp
%{gstincludedir}/gst/tag
%{gstincludedir}/gst/video
%{_pkgconfigdir}/gstreamer-app-0.10.pc
%{_pkgconfigdir}/gstreamer-audio-0.10.pc
%{_pkgconfigdir}/gstreamer-cdda-0.10.pc
%{_pkgconfigdir}/gstreamer-fft-0.10.pc
%{_pkgconfigdir}/gstreamer-floatcast-0.10.pc
%{_pkgconfigdir}/gstreamer-interfaces-0.10.pc
%{_pkgconfigdir}/gstreamer-netbuffer-0.10.pc
%{_pkgconfigdir}/gstreamer-pbutils-0.10.pc
%{_pkgconfigdir}/gstreamer-plugins-base-0.10.pc
%{_pkgconfigdir}/gstreamer-riff-0.10.pc
%{_pkgconfigdir}/gstreamer-rtp-0.10.pc
%{_pkgconfigdir}/gstreamer-rtsp-0.10.pc
%{_pkgconfigdir}/gstreamer-sdp-0.10.pc
%{_pkgconfigdir}/gstreamer-tag-0.10.pc
%{_pkgconfigdir}/gstreamer-video-0.10.pc
%{_datadir}/gir-1.0/GstApp-0.10.gir
%{_datadir}/gir-1.0/GstAudio-0.10.gir
%{_datadir}/gir-1.0/GstFft-0.10.gir
%{_datadir}/gir-1.0/GstInterfaces-0.10.gir
%{_datadir}/gir-1.0/GstNetbuffer-0.10.gir
%{_datadir}/gir-1.0/GstPbutils-0.10.gir
%{_datadir}/gir-1.0/GstRiff-0.10.gir
%{_datadir}/gir-1.0/GstRtp-0.10.gir
%{_datadir}/gir-1.0/GstRtsp-0.10.gir
%{_datadir}/gir-1.0/GstSdp-0.10.gir
%{_datadir}/gir-1.0/GstTag-0.10.gir
%{_datadir}/gir-1.0/GstVideo-0.10.gir

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gst-plugins-base-libs-*
%{_gtkdocdir}/gst-plugins-base-plugins-*
%endif

##
## Plugins
##

%files -n gstreamer0.10-audiosink-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstalsa.so

%files -n gstreamer0.10-audio-effects-base
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstadder.so
%attr(755,root,root) %{gstlibdir}/libgstaudioresample.so
%attr(755,root,root) %{gstlibdir}/libgstvolume.so

%files -n gstreamer0.10-cdparanoia
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcdparanoia.so

%if %{with gnomevfs}
%files -n gstreamer0.10-gnomevfs
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgnomevfs.so
%endif

%if %{with libvisual}
%files -n gstreamer0.10-libvisual
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstlibvisual.so
%endif

%files -n gstreamer0.10-pango
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstpango.so

%files -n gstreamer0.10-theora
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsttheora.so

%if %{with v4l1}
%files -n gstreamer0.10-video4linux
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvideo4linux.so
%endif

%files -n gstreamer0.10-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvorbis.so
%attr(755,root,root) %{gstlibdir}/libgstogg.so

%files -n gstreamer0.10-imagesink-x
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstximagesink.so

%files -n gstreamer0.10-imagesink-xv
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstxvimagesink.so
