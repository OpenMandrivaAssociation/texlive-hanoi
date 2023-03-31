Name:		texlive-hanoi
Version:	25019
Release:	2
Summary:	Tower of Hanoi in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/hanoi/hanoi.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hanoi.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Plain TeX program (typed in the shape of the towers of
Hanoi) serves both as a game and as a TeX programming exercise.
As a game it will solve the towers with (up to) 15 discs (with
15 discs, 32767 moves are needed).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/hanoi/hanoi.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
