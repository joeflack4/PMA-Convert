# PMA-Convert
A GUI tool for converting PMA2020 Specification XlsForms .

# Development
# Building a standalone .app file for OSX.
* `py2applet --make-setup PMA-Convert.py --iconfile favicon.icns`
* `python setup.py py2app`
<!--## Building to a standalone app-->
<!--See: https://ar.al/1675/-->

## Possible Errors
### Py2App
If you run into errors such as `AttributeError: 'ModuleGraph' object has no attribute 'scan_code'` or `AttributeError: 'ModuleGraph' object has no attribute 'load_module'`, consult the following solution: http://www.marinamele.com/from-a-python-script-to-a-portable-mac-application-with-py2app

### Running standalone app file
If you run into the the error `A Python runtime not could be located.  You may need to install a framework build of Python, or edit the PyRuntimeLocations array in this application's Info.plist file.`, consult: http://stackoverflow.com/questions/1346297/py2app-cant-find-standard-modules

# Running
Navigate to PMA-Convert.py. If double clicking does not load the app, try right clicking and opening with Python.
