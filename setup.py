from setuptools import setup


setup(
    name='displayer',
    version='0.3',
    description='Batch display library for images in a directory using a web browser',
    url='https://github.com/enomotokenji/image-displayer',
    author='Kenji Enomoto',
    author_email='kenji.enomoto.abc.123@gmail.com',
    license='MIT',
    packages=[
        "displayer",
    ],
    package_data={
        'displayer': ['lazysizes.min.js', 'dummy.gif']
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': ['displayer=displayer.displayer:displayer']}
)