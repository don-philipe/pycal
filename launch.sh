#!/bin/sh

if [ -n "$(lsb_release -i | grep arch)" ]; then
	python2 bin/main.pyc
else
	python bin/main.pyc
fi
