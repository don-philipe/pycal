
# VARIABLES
ifeq "$(shell lsb_release -i | grep -o n/a)" "n/a"
echo "No LSB-Releaseinformation available! Please set them manually or reinstall lsb-relesase."
else
ifeq "$(shell lsb_release -i | grep -o arch)" "arch"
PYTHON = "python2"
else
PYTHON = "python"
endif
endif

PLATFORM := $(shell $(PYTHON) -B pfinfo.py)

PYMODS = $(subst ./,,$(shell cd src; find . -name \*.py; cd ..))
PYBINS = $(foreach pymod,$(PYMODS),bin/$(pymod)c)

.PHONY : pycal bin clean totalclean

pycal: bin

bin: $(PYBINS)

bin/%.pyc: src/%.py
	mkdir -p "$(dir $@)"
	$(PYTHON) pyc.py "$^" "$@"

clean:
	-rm -r bin

totalclean:
	-rm -r bin
	-rm -r doc/src

epydoc:
	mkdir -p doc
	epydoc --html src -o doc/src --config epydoc.conf --parse-only -v
