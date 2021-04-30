from setuptools import _install_setup_requires, setup

setup(
    name="twitoff_app", 
    packages=['twitoff_app'],
    include_package_data=True,
    install_requires=[
        'flask',
        ],    
)