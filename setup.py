from setuptools import setup, find_packages

setup(
    name='AutoFL',
    version='1.2',
    packages=find_packages(),
    author='Owen Orcan',
    author_email='owenorcan@gmail.com',
    url='https://github.com/OwenOrcan/AutoFlask',
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
