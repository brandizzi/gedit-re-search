#!/bin/sh

GEDIT_PLUGINS_DIRECTORY=$HOME/.gnome2/gedit/plugins

mkdir -p $GEDIT_PLUGINS_DIRECTORY/regex_replace

cp regex_replace/* $GEDIT_PLUGINS_DIRECTORY/regex_replace
cp regex_replace.gedit-plugin $GEDIT_PLUGINS_DIRECTORY
