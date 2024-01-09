#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: ab27b0e
#
Name     : R-compositions
Version  : 2.0.7
Release  : 63
URL      : https://cran.r-project.org/src/contrib/compositions_2.0-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/compositions_2.0-7.tar.gz
Summary  : Compositional Data Analysis
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-compositions-lib = %{version}-%{release}
Requires: R-compositions-license = %{version}-%{release}
Requires: R-bayesm
Requires: R-robustbase
Requires: R-tensorA
BuildRequires : R-bayesm
BuildRequires : R-robustbase
BuildRequires : R-tensorA
BuildRequires : buildreq-R

%description
data (e.g. portions of substances) and positive numbers (e.g. concentrations) 
  in the way proposed by J. Aitchison and V. Pawlowsky-Glahn.

%package lib
Summary: lib components for the R-compositions package.
Group: Libraries
Requires: R-compositions-license = %{version}-%{release}

%description lib
lib components for the R-compositions package.


%package license
Summary: license components for the R-compositions package.
Group: Default

%description license
license components for the R-compositions package.


%prep
%setup -q -n compositions
pushd ..
cp -a compositions buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1704821108

%install
export SOURCE_DATE_EPOCH=1704821108
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-compositions
cp %{_builddir}/compositions/COPYING %{buildroot}/usr/share/package-licenses/R-compositions/075d599585584bb0e4b526f5c40cb6b17e0da35a || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/compositions/DESCRIPTION
/usr/lib64/R/library/compositions/INDEX
/usr/lib64/R/library/compositions/Meta/Rd.rds
/usr/lib64/R/library/compositions/Meta/data.rds
/usr/lib64/R/library/compositions/Meta/demo.rds
/usr/lib64/R/library/compositions/Meta/features.rds
/usr/lib64/R/library/compositions/Meta/hsearch.rds
/usr/lib64/R/library/compositions/Meta/links.rds
/usr/lib64/R/library/compositions/Meta/nsInfo.rds
/usr/lib64/R/library/compositions/Meta/package.rds
/usr/lib64/R/library/compositions/Meta/vignette.rds
/usr/lib64/R/library/compositions/NAMESPACE
/usr/lib64/R/library/compositions/R/compositions
/usr/lib64/R/library/compositions/R/compositions.rdb
/usr/lib64/R/library/compositions/R/compositions.rdx
/usr/lib64/R/library/compositions/data/Aar.rda
/usr/lib64/R/library/compositions/data/Activity10.rda
/usr/lib64/R/library/compositions/data/Activity31.rda
/usr/lib64/R/library/compositions/data/AnimalVegetation.rda
/usr/lib64/R/library/compositions/data/ArcticLake.rda
/usr/lib64/R/library/compositions/data/Bayesite.rda
/usr/lib64/R/library/compositions/data/Blood23.rda
/usr/lib64/R/library/compositions/data/Boxite.rda
/usr/lib64/R/library/compositions/data/ClamEast.rda
/usr/lib64/R/library/compositions/data/ClamWest.rda
/usr/lib64/R/library/compositions/data/Coxite.rda
/usr/lib64/R/library/compositions/data/DiagnosticProb.rda
/usr/lib64/R/library/compositions/data/Firework.rda
/usr/lib64/R/library/compositions/data/Glacial.rda
/usr/lib64/R/library/compositions/data/Hongite.rda
/usr/lib64/R/library/compositions/data/HouseholdExp.rda
/usr/lib64/R/library/compositions/data/Hydrochem.txt
/usr/lib64/R/library/compositions/data/Kongite.rda
/usr/lib64/R/library/compositions/data/Metabolites.rda
/usr/lib64/R/library/compositions/data/PogoJump.rda
/usr/lib64/R/library/compositions/data/Sediments.rda
/usr/lib64/R/library/compositions/data/SerumProtein.rda
/usr/lib64/R/library/compositions/data/ShiftOperators.rda
/usr/lib64/R/library/compositions/data/SimulatedAmounts.RData
/usr/lib64/R/library/compositions/data/Skulls.rda
/usr/lib64/R/library/compositions/data/SkyeAFM.rda
/usr/lib64/R/library/compositions/data/Supervisor.rda
/usr/lib64/R/library/compositions/data/WhiteCells.rda
/usr/lib64/R/library/compositions/data/Yatquat.rda
/usr/lib64/R/library/compositions/data/jura259.rda
/usr/lib64/R/library/compositions/data/juraset.rda
/usr/lib64/R/library/compositions/demo/compplots.R
/usr/lib64/R/library/compositions/doc/UsingCompositions.pdf
/usr/lib64/R/library/compositions/doc/UsingCompositions.rnw
/usr/lib64/R/library/compositions/doc/compositions_v2.R
/usr/lib64/R/library/compositions/doc/compositions_v2.Rmd
/usr/lib64/R/library/compositions/doc/compositions_v2.html
/usr/lib64/R/library/compositions/doc/index.html
/usr/lib64/R/library/compositions/help/AnIndex
/usr/lib64/R/library/compositions/help/aliases.rds
/usr/lib64/R/library/compositions/help/compositions.rdb
/usr/lib64/R/library/compositions/help/compositions.rdx
/usr/lib64/R/library/compositions/help/paths.rds
/usr/lib64/R/library/compositions/html/00Index.html
/usr/lib64/R/library/compositions/html/R.css
/usr/lib64/R/library/compositions/tests/AitchisonTest.R
/usr/lib64/R/library/compositions/tests/CheckGeometry.R
/usr/lib64/R/library/compositions/tests/CheckGeometry.Rout.save
/usr/lib64/R/library/compositions/tests/LAKE.txt
/usr/lib64/R/library/compositions/tests/RobustTest.R
/usr/lib64/R/library/compositions/tests/RobustTest.Rout.save
/usr/lib64/R/library/compositions/tests/Rplots.pdf
/usr/lib64/R/library/compositions/tests/TRUE.DAT
/usr/lib64/R/library/compositions/tests/TestMissing.R
/usr/lib64/R/library/compositions/tests/TestMissing.Rout.save
/usr/lib64/R/library/compositions/tests/TestSimp.R
/usr/lib64/R/library/compositions/tests/TestSimp.Rout.save
/usr/lib64/R/library/compositions/tests/acheck.R
/usr/lib64/R/library/compositions/tests/geostat.R
/usr/lib64/R/library/compositions/tests/juraset.dat
/usr/lib64/R/library/compositions/tests/missings.R
/usr/lib64/R/library/compositions/tests/missings.Rout.save
/usr/lib64/R/library/compositions/tests/quickcheck.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/compositions/libs/compositions.so
/usr/lib64/R/library/compositions/libs/compositions.so.avx2
/usr/lib64/R/library/compositions/libs/compositions.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-compositions/075d599585584bb0e4b526f5c40cb6b17e0da35a
