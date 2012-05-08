install:
	cp -r regex_replace regex_replace.plugin /Users/brandizzi/.local/share/gedit/plugins/

pack:
	tar zvcf versions/gedit3-research-$(shell date +%Y%m%d).tar.gz regex_replace/ regex_replace.plugin install.sh

tag:
	hg tag $(shell date +%Y%m%d)
