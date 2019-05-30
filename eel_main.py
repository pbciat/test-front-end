import eel
import time
eel.init('web')




rt = []

@eel.expose
def my_python_function():
    global rt
    rt.append(1)
    print(rt)
    return rt

eel.document.onkeydown()(lambda n: print('Got this from Javascript:', n))
    



# Start app
web_app_options = {
    'mode': "chrome", #or "chrome-app"  "chrome"
    'port': 8000,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}
eel.start('index.html', options=web_app_options)