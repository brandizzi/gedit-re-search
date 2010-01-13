import gtk

class SearchDialog(gtk.Dialog):

    def __init__(self):
        gtk.Dialog.__init__(self, title=_("Replace"))

        self.table = gtk.Table(homogeneous=False)
     
        # Entries
        self.search_label = self._get_label(_("_Search for: "))
        self.table.attach(self.search_label, 
                0, 1, 0, 1,
                xoptions=gtk.FILL, yoptions=gtk.FILL,
                xpadding=6, ypadding=6)
        self.search_entry = gtk.Entry()
        self.table.attach(self.search_entry, 
                1, 2, 0, 1,
                xoptions=gtk.EXPAND|gtk.FILL, yoptions=gtk.FILL,
                xpadding=6, ypadding=6)
        self.search_label.set_mnemonic_widget(self.search_entry)
        
        self.replace_label = self._get_label(_("Replace _with: "))
        self.table.attach(self.replace_label,
                0, 1, 1, 2,
                xoptions=gtk.FILL, yoptions=gtk.FILL,
                xpadding=6, ypadding=6)
        self.replace_entry = gtk.Entry()
        self.table.attach(self.replace_entry, 
                1, 2, 1, 2,
                xoptions=gtk.EXPAND|gtk.FILL, yoptions=gtk.FILL,
                xpadding=6, ypadding=6)
        self.replace_label.set_mnemonic_widget(self.replace_entry)
        
        # Options
        # TODO: regex disabling
        #self.regex_search_checkbutton = gtk.CheckButton(
        #        _("Regular expression search"))
        #self.table.attach(self.regex_search_checkbutton, 1, 2, 0, 1)
        self.case_sensitive_checkbutton = gtk.CheckButton(
                _("_Match case"))
        self.table.attach(self.case_sensitive_checkbutton, 
                0, 2, 2, 3,
                xpadding=6, ypadding=6)
        
        self.wrap_around_checkbutton = gtk.CheckButton(
                _("_Wrap around"))
        self.table.attach(self.wrap_around_checkbutton, 
                0, 2, 3, 4, 
                xoptions=gtk.EXPAND|gtk.FILL, yoptions=gtk.FILL,
                xpadding=6, ypadding=6)
        
        self.backreferences_checkbutton = gtk.CheckButton(
                _("Use _backreferences"))
        self.table.attach(self.backreferences_checkbutton, 
                0, 2, 4, 5,
                xoptions=gtk.EXPAND|gtk.FILL, yoptions=gtk.FILL,
                xpadding=6, ypadding=6)

        self.close_button = self.add_button(gtk.STOCK_CLOSE, 
                gtk.RESPONSE_ACCEPT)
        self.replace_all_button = self.add_button(_("Replace All"), 
                gtk.RESPONSE_ACCEPT)

        # Creating a button just like the one from the default Replace dialog
        self.replace_button = gtk.Button()
        self.replace_button.add(gtk.HBox())
        self.replace_button.get_child().set_spacing(2)
        self.replace_button.get_child().pack_start(
                gtk.image_new_from_stock(
                        gtk.STOCK_FIND_AND_REPLACE, 
                        gtk.ICON_SIZE_BUTTON))
        self.replace_button.get_child().pack_end(self._get_label(_("_Replace")))
        self.replace_button.show_all()
        self.action_area.pack_end(self.replace_button)

        self.find_button = self.add_button(gtk.STOCK_FIND, 
                gtk.RESPONSE_ACCEPT)

        self.set_resizable(False)
        
        self.vbox.pack_start(self.table)

        
    def _get_label(self, text):
        label = gtk.Label(text)
        label.set_alignment(0, 0.5)
        label.set_use_underline(True)
        return label

