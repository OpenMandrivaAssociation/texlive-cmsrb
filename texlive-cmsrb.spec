Name:		texlive-cmsrb
Version:	54706
Release:	2
Summary:	Computer Modern for Serbian and Macedonian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cmsrb
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmsrb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmsrb.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides provides Adobe Type 1 Computer Modern
fonts for the Serbian and Macedonian languages. Although the
cm-super package provides great support for cyrillic script in
various languages, there remains a problem with italic variants
of some letters for Serbian and Macedonian. This package
includes the correct shapes for italic letters \cyrb, \cyrg,
\cyrd, \cyrp, and \cyrt. It also offers some improvements in
letters and accents used in the Serbian language. Supported
encodings are: T1, T2A, TS1, X2 and OT2. The OT2 encoding is
modified so that it is now easy to transcribe Latin text to
Cyrillic.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cmsrb
%{_texmfdistdir}/fonts/vf/public/cmsrb
%{_texmfdistdir}/fonts/type1/public/cmsrb
%{_texmfdistdir}/fonts/tfm/public/cmsrb
%{_texmfdistdir}/fonts/map/dvips/cmsrb
%{_texmfdistdir}/fonts/enc/dvips/cmsrb
%{_texmfdistdir}/fonts/afm/public/cmsrb
%doc %{_texmfdistdir}/doc/fonts/cmsrb

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
