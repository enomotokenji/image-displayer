from setuptools import setup
from displayer import displayer


setup(
    name='displayer',
    version='0.4.2',
    description='Batch display library for images in a directory',
    url='https://github.com/enomotokenji/image-displayer',
    author='Kenji Enomoto',
    author_email='kenji.enomoto.abc.123@gmail.com',
    license='MIT',
    packages=[
        "displayer",
    ],
    package_data={
        'displayer': displayer.misc_files
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': ['displayer=displayer.displayer:displayer_commandline']}
)