import io
from setuptools import setup


setup(
    name='cognito-iam-provider',
    version='0.0.1',
    description='Assumes an IAM role in boto3 using Cognito credentials',
    author='Mathew Moon',
    author_email='mmoon@quinovas.com',
    url='https://github.com/QuiNovas/cognito-iam-provider',
    license='Apache 2.0',
    long_description=io.open('README.rst', encoding='utf-8').read(),
    long_description_content_type='text/x-rst',
    packages=['CognitoIamProvider'],
    package_dir={'CognitoIamProvider': 'src/CognitoIamProvider'},
    install_requires=["boto3", "botocore"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],
)
