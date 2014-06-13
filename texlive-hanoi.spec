# revision 25019
# category Package
# catalog-ctan /macros/plain/contrib/hanoi/hanoi.tex
# catalog-date 2012-01-03 17:40:13 +0100
# catalog-license pd
# catalog-version 20120101
Name:		texlive-hanoi
Version:	20120101
Release:	6
Summary:	Tower of Hanoi in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/hanoi/hanoi.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hanoi.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120101-1
+ Revision: 758884
- texlive-hanoi
- texlive-hanoi

