from setuptools import setup, find_packages

setup(
    name="filesystem-usage-viewer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "matplotlib"
    ],
    entry_points={
        'console_scripts': [
            'fsviewer=fsviewer.gui:start_gui'
        ],
    },
    python_requires='>=3.6',
)
