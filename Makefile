install:
	cp -r regex_replace regex_replace.gedit-plugin /Users/brandizzi/.gnome2/gedit/plugins

pack: clean
	tar zvcf versions/gedit2-research-$(shell date +%Y%m%d).tar.gz regex_replace/ regex_replace.gedit-plugin install.sh

tag:
	hg tag $(shell date +%Y%m%d)v2

clean:
	find . -name '*~' -exec rm {} \;
	
