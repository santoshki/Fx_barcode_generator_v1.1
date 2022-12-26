import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Fx_Image Compressor Alphav1.1')
        panel = wx.Panel(self)
        self.title_label = wx.StaticText(panel, id=1, label="Old Label.", pos=(150, 50),
                                         size=wx.DefaultSize, style=0, name="statictext")
        self.title_label.SetLabel("Barcode Generator")
        self.society_name_label = wx.StaticText(panel, id=1, label="Old Label.", pos=(25, 100),
                                         size=wx.DefaultSize, style=0, name="statictext")
        self.society_name_label.SetLabel("Society Name")
        self.society_name_values = ["PSP Norwood", "Other"]

        cb = wx.ComboBox(panel, value=self.society_name_values[0], choices=self.society_name_values, pos=(120, 100))


        self.book_category_label = wx.StaticText(panel, id=1, label="Old Label.", pos=(25, 150),
                                         size=wx.DefaultSize, style=0, name="statictext")
        self.book_category_label.SetLabel("Book Category")


        self.barcode_count_label = wx.StaticText(panel, id=1, label="Old Label.", pos=(25, 200),
                                                 size=wx.DefaultSize, style=0, name="statictext")
        self.barcode_count_label.SetLabel("Number of barcodes\nto be created")

        self.barcode_generate_button = wx.Button(panel, label='Generate', pos=(50, 300))
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()