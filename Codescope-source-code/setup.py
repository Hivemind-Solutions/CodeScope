from setuptools import setup

APP = ['codescope.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']

)
