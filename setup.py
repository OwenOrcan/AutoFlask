from setuptools import setup, find_packages

setup(
    name='AutoFlask',
    version='1.0',
    packages=find_packages(),
    author='Owen Orcan',
    author_email='owenorcan@gmail.com',
    url='https://github.com/OwenOrcan/Yirabot-Crawler',
    license='MIT License',
    description="AutoFlask simplifies Flask project setup, automating the creation of essential files and directories with just one command.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    entry_points={
        'console_scripts': [
            'autoflask = AutoFlask.AutoFlask:main',
        ],
    },
)
