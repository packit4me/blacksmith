PACKAGE := $(shell basename *.spec .spec)
ARCH = noarch
PYTHON_SITELIB := $(shell python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
RPMBUILD = rpmbuild --define "_topdir %(pwd)/rpm-build" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %(pwd)/rpms" \
	--define "_srcrpmdir %{_rpmdir}" \
	--define "_sourcedir  %{_topdir}"


all: rpms

clean:
	rm -rf dist/ build/ rpm-build/ rpms/
	rm -rf blacksmith/*.pyc MANIFEST *.pyc *~

build: clean
	python setup.py build -f

install: build
	python setup.py install -f

reinstall: uninstall install

uninstall: clean
	rm -f /usr/bin/${PACKAGE}
	rm -rf ${PYTHON_SITELIB}/${PACKAGE}

uninstall_rpms: clean
	rpm -e ${PACKAGE}

sdist:
	python setup.py sdist

prep_rpmbuild: build sdist
	mkdir -p rpm-build
	mkdir -p rpms
	cp dist/*.gz rpm-build/

rpms: prep_rpmbuild
	${RPMBUILD} -ba ${PACKAGE}.spec

srpm: prep_rpmbuild
	${RPMBUILD} -bs ${PACKAGE}.spec
