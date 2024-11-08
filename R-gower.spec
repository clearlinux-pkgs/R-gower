#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gower
Version  : 1.0.1
Release  : 56
URL      : https://cran.r-project.org/src/contrib/gower_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gower_1.0.1.tar.gz
Summary  : Gower's Distance
Group    : Development/Tools
License  : GPL-3.0
Requires: R-gower-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
the top-n matches between records. Core algorithms are executed in parallel on systems
    supporting OpenMP.

%package lib
Summary: lib components for the R-gower package.
Group: Libraries

%description lib
lib components for the R-gower package.


%prep
%setup -q -n gower
cd %{_builddir}/gower

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671728149

%install
export SOURCE_DATE_EPOCH=1671728149
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gower/DESCRIPTION
/usr/lib64/R/library/gower/INDEX
/usr/lib64/R/library/gower/Meta/Rd.rds
/usr/lib64/R/library/gower/Meta/features.rds
/usr/lib64/R/library/gower/Meta/hsearch.rds
/usr/lib64/R/library/gower/Meta/links.rds
/usr/lib64/R/library/gower/Meta/nsInfo.rds
/usr/lib64/R/library/gower/Meta/package.rds
/usr/lib64/R/library/gower/Meta/vignette.rds
/usr/lib64/R/library/gower/NAMESPACE
/usr/lib64/R/library/gower/NEWS
/usr/lib64/R/library/gower/R/gower
/usr/lib64/R/library/gower/R/gower.rdb
/usr/lib64/R/library/gower/R/gower.rdx
/usr/lib64/R/library/gower/doc/index.html
/usr/lib64/R/library/gower/doc/intro.R
/usr/lib64/R/library/gower/doc/intro.Rnw
/usr/lib64/R/library/gower/doc/intro.pdf
/usr/lib64/R/library/gower/help/AnIndex
/usr/lib64/R/library/gower/help/aliases.rds
/usr/lib64/R/library/gower/help/gower.rdb
/usr/lib64/R/library/gower/help/gower.rdx
/usr/lib64/R/library/gower/help/paths.rds
/usr/lib64/R/library/gower/html/00Index.html
/usr/lib64/R/library/gower/html/R.css
/usr/lib64/R/library/gower/tests/tinytest.R
/usr/lib64/R/library/gower/tinytest/test_gh_issue_18.R
/usr/lib64/R/library/gower/tinytest/test_gh_issue_8.R
/usr/lib64/R/library/gower/tinytest/test_gower.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gower/libs/gower.so
/usr/lib64/R/library/gower/libs/gower.so.avx2
/usr/lib64/R/library/gower/libs/gower.so.avx512
