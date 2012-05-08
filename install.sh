#!/bin/sh

GEDIT_PLUGINS_DIRECTORY=$HOME/.local/share/gedit/plugins/

mkdir -p $GEDIT_PLUGINS_DIRECTORY/regex_replace

cp regex_replace/* $GEDIT_PLUGINS_DIRECTORY/regex_replace
cp regex_replace.plugin $GEDIT_PLUGINS_DIRECTORY
