from setuptools import setup, find_packages

setup(
    name='my_math',
    version='0.1',
    packages=find_packages(),
    author='Md. Rezaul Karim',
    author_email='rezaul.cse.pust17@gmail.com',
    license='MIT',
    description='A simple python package for math',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rkpust/my_math",
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.0',
    keywords='math, calculations'
)
