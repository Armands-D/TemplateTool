from setuptools import setup

setup(
    name='temp_tool',
    version='0.1.0',
    py_modules=['temp_tool'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'temp_tool = temp_tool:cli',
        ],
    },
)
