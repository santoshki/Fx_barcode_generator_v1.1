import wx
from entities import keybindings


class BarcodeGeneratorUI(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Fx_Barcode_generator Alpha_v1.1')
        panel = wx.Panel(self)
        self.title_label = wx.StaticText(panel, id=1, label="Old Label.", pos=(150, 50),
                                         size=wx.DefaultSize, style=0, name="statictext")
        self.title_label.SetLabel("Barcode Generator")
        self.society_name_values = ["PSP Norwood", "Other"]
        self.book_category_values = ["Kids", "Philosophy", "Religion", "Social Sciences", "Language", "Science",
                                     "Technology",
                                     "Arts", "Literature", "History, Geography"]
        self.society_name_label = wx.StaticText(panel, id=1, label="Old Label.", pos=(25, 100),
                                                size=wx.DefaultSize, style=0, name="statictext")
        self.society_name_label.SetLabel("Society Name")
        self.society_names_dropdown = wx.ComboBox(panel, value=self.society_name_values[0],
                                                  choices=self.society_name_values,
                                                  pos=(120, 100))
        self.book_category_label = wx.StaticText(panel, id=1, label="Old Label.", pos=(25, 150),
                                                 size=wx.DefaultSize, style=0, name="statictext")
        self.book_category_label.SetLabel("Book Category")
        self.book_category_dropdown = wx.ComboBox(panel, value=self.book_category_values[0],
                                                  choices=self.book_category_values,
                                                  pos=(120, 150))
        self.barcode_count_label = wx.StaticText(panel, id=1, label="Old Label.", pos=(25, 200),
                                                 size=wx.DefaultSize, style=0, name="statictext")
        self.barcode_count_label.SetLabel("No. of barcodes\nto be created")
        self.barcode_count = wx.SpinCtrl(panel, -1, '', (120, 200), (60, -1))
        self.barcode_count.SetRange(0, 100)
        self.barcode_count.SetValue(1)
        self.barcode_generate_button = wx.Button(panel, label="Generate", pos=(25, 250))
        self.barcode_app_exit_button = wx.Button(panel, label="Exit", pos=(250, 400))
        self.barcode_app_about_button = wx.Button(panel, label="About", pos=(25, 400))
        self.barcode_generate_button.Bind(wx.EVT_BUTTON, self.on_click_barcode_generate_button)
        self.barcode_app_exit_button.Bind(wx.EVT_BUTTON, self.on_click_exit_button)
        self.barcode_app_about_button.Bind(wx.EVT_BUTTON, self.on_click_about_button)
        self.Show()

    def on_click_barcode_generate_button(self, event):
        keybindings.barcode_generation(self.society_names_dropdown.GetValue(), self.book_category_dropdown.GetValue(),
                                       self.barcode_count.GetValue())

    def on_click_about_button(self, event):
        keybindings.about_app_action(self)

    def on_click_exit_button(self, event):
        keybindings.exit_app_action(self)


class ActionComplete(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Fx_Barcode_generator Alphav1.1")
        panel = wx.Panel(self)
        txt = wx.StaticText(panel, label="Barcodes generated Successfully!")
        self.okay_button = wx.Button(panel, label="Okay", pos=(25, 25))
        self.okay_button.Bind(wx.EVT_BUTTON, self.on_click_okay_button)

    def on_click_okay_button(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    frame = BarcodeGeneratorUI()
    app.MainLoop()
