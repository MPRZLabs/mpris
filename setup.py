from distutils.core import setup
setup(name='michi-mpris',
      version='1.0.4',
      author='Michał Sidor',
      author_email='michcioperz@gmail.com',
      description='wrapper over MPRIS2 APIs',
      url='http://github.com/michcioperz/mpris',
      py_modules=['michimpris'],
      scripts=['michispotify.py','michitomahawk.py'],
      )
