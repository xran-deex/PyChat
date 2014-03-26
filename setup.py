# A very simple setup script to create 2 executables.
#
# hello.py is a simple "hello, world" type program, which alse allows
# to explore the environment in which the script runs.
#
# test_wx.py is a simple wxPython program, it will be converted into a
# console-less program.
#
# If you don't have wxPython installed, you should comment out the
#   windows = ["test_wx.py"]
# line below.
#
#
# Run the build process by entering 'setup.py py2exe' or
# 'python setup.py py2exe' in a console prompt.
#
# If everything works well, you should find a subdirectory named 'dist'
# containing some files, among them hello.exe and test_wx.exe.


from distutils.core import setup
import py2exe

setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "0.1.0",
    description = "PyChat",
    name = "PyChat",

    # targets to build
    windows = ["PyChatClient.py"],
    data_files = [('imageformats', [r'E:\Portable Python 2.7.5.1\App\Lib\site-packages\PyQt4\plugins\imageformats\qsvg4.dll', r'E:\Portable Python 2.7.5.1\App\Lib\site-packages\PyQt4\plugins\imageformats\qtga4.dll', r'E:\Portable Python 2.7.5.1\App\Lib\site-packages\PyQt4\plugins\imageformats\qjpeg4.dll'])],
    options={

# And now, configure py2exe by passing more options;

          'py2exe': {

# Py2exe will not figure out that you need these on its own.
# You may need one, the other, or both.

              'includes': [
                  'sip',
                  ],
             'dll_excludes': [
                 'qsvg4.dll',
              ],
# Optional: make one big exe with everything in it, or
# a folder with many things in it. Your choice
            'bundle_files': 3,
            'dist_dir': r'E:\PyChat',
          }
    }
    )
