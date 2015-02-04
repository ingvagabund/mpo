#!/bin/sh

# check input

if [ "$(echo $MPO_Y_STREAM)" == "" ]; then
	echo "MPO_Y_STREAM env not defined"
	exit 1
fi

if [ "$1" == "" ]; then
	echo "component not defined"
	exit 1
fi

if [ "$(basename $(pwd))" != "man-pages-overrides" ]; then
	echo "not in man-pages-overrides directory"
	exit 1
fi

# variables
dir_name="man-pages-overrides-$MPO_Y_STREAM"
component=$1
tarball="$dir_name".tar.gz

# remove component from tarball
rm -rf $dir_name
tar -xf $tarball
pushd $dir_name
rm -rf $component
popd
tar -czf $tarball $dir_name

