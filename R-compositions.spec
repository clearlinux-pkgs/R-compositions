#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-compositions
Version  : 2.0.2
Release  : 43
URL      : https://cran.r-project.org/src/contrib/compositions_2.0-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/compositions_2.0-2.tar.gz
Summary  : Compositional Data Analysis
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-compositions-lib = %{version}-%{release}
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

%description lib
lib components for the R-compositions package.


%prep
%setup -q -c -n compositions
cd %{_builddir}/compositions

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1626364828

%install
export SOURCE_DATE_EPOCH=1626364828
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library compositions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library compositions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library compositions
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc compositions || :


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
/usr/lib64/R/library/compositions/tests/CheckGeometry.Rout
/usr/lib64/R/library/compositions/tests/LAKE.txt
/usr/lib64/R/library/compositions/tests/RobustTest.R
/usr/lib64/R/library/compositions/tests/RobustTest.Rout
/usr/lib64/R/library/compositions/tests/Rplots.pdf
/usr/lib64/R/library/compositions/tests/TRUE.DAT
/usr/lib64/R/library/compositions/tests/TestMissing.R
/usr/lib64/R/library/compositions/tests/TestMissing.Rout
/usr/lib64/R/library/compositions/tests/TestSimp.R
/usr/lib64/R/library/compositions/tests/TestSimp.Rout
/usr/lib64/R/library/compositions/tests/acheck.R
/usr/lib64/R/library/compositions/tests/geostat.R
/usr/lib64/R/library/compositions/tests/juraset.dat
/usr/lib64/R/library/compositions/tests/missings.R
/usr/lib64/R/library/compositions/tests/missings.Rout
/usr/lib64/R/library/compositions/tests/quickcheck.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/compositions/libs/compositions.so
/usr/lib64/R/library/compositions/libs/compositions.so.avx2
/usr/lib64/R/library/compositions/libs/compositions.so.avx512
