install:
	cp -r regex_replace regex_replace.gedit-plugin /Users/brandizzi/.gnome2/gedit/plugins

pack:
	tar zvcf versions/gedit-reserch-$(shell date +%Y%m%d).tar.gz regex_replace/ regex_replace.gedit-plugin install.sh
