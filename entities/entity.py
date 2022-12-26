import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Fx_Image Compressor Alphav1.1')
        panel = wx.Panel(self)
        #panel.SetSizer(wx.DefaultSize)
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
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
