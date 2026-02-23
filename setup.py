from setuptools import setup, find_packages

setup(
    name='your_package_name', # Replace with your package name
    version='0.1.0',
    author='Your Name', # Replace with your name
    author_email='your_email@example.com', # Replace with your email
    description='A brief description of your package',
    long_description=open('README.md').read(), # Make sure you have a README file
    long_description_content_type='text/markdown',
    url='https://github.com/Anas999-lgtm/AnasAl',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)