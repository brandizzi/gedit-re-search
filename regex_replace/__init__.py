from gi.repository import GObject, Gedit
from .regexsearchinstance import RegexSearchInstance

class RegexSearch(GObject.Object, Gedit.WindowActivatable):
    DATA_TAG = "RegexSearchInstance"
    __gtype_name__ = "GeditRESearch"
    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        regexsearch_instance = RegexSearchInstance(self.window)
        setattr(self.window, self.DATA_TAG, regexsearch_instance)
				
	
    def do_deactivate(self):
        regexsearch_instance = getattr(self.window, self.DATA_TAG)
        # regexsearch_instance destroy!?
        delattr(self.window, self.DATA_TAG)
		
    def do_update_ui(self):
        regexsearch_instance = getattr(self.window, self.DATA_TAG)
        regexsearch_instance.update_ui()
