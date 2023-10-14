from distutils.core import setup
import setuptools

def requirements():
    with open('requirements.txt', 'r') as f:
        requirements = [line.strip() for line in f]
        return requirements

setup(
    name='seq_bank',
    version='1.0',
    author='Xiaohong Yuan',
    author_email='xyuan04@nyit.edu',
    description='Seq Bank',
    packages = ['seq_bank'],
    package_data = {'seq_bank': ['resources/*.csv']},
    entry_points={
        'console_scripts': [
            'seq_bank = seq_bank.__main__:main'
        ]
    },
    install_requires = requirements(),
    python_requires=">=3.5",
)
