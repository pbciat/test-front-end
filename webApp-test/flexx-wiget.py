from flexx import flx

class Example(flx.Widget):
    def init(self):
        with flx.HSplit():
            with flx.GridLayout(ncolumns=3):
                flx.Button(text='A')
                flx.Button(text='B')
                flx.Button(text='C')
                flx.Button(text='D')
                flx.Button(text='E')
                flx.Button(text='F')

            with flx.GridLayout(ncolumns=2):
                flx.Button(text='A', flex=(1, 1))  # Set flex for 1st row and col
                flx.Button(text='B', flex=(2, 1))  # Set flex for 2nd col
                flx.Button(text='C', flex=(1, 1))  # Set flex for 2nd row
                flx.Button(text='D')
                flx.Button(text='E', flex=(1, 2))  # Set flex for 3d row
                flx.Button(text='F')

app = flx.App(Example)

# Export to separate files (link=2, link separate css)
app.serve('')
assets = app.dump('index.html', link=2)


#app.export('example.html', link=2)  

print(assets)

# launch in browser
app.launch('browser')  # show it now in a browser
flx.run()  # enter the mainloop