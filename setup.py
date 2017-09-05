"""setup.py for visage."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyvisage',
    packages=['visage'],
    version='0.15.2',
    description='Add virtual makeup to an image of a face.',
    author='Hriddhi Dey',
    author_email='hriddhidey@gmail.com',
    url='https://github.com/hriddhidey/visage.git',
    download_url='https://github.com/hriddhidey/visage/archive/0.15.2.tar.gz',
    install_requires=[
        'opencv-python',
        'scikit-image',
        'dlib'
    ],
    include_package_data=True,
    keywords='image processing virtual makeup face detection opencv',
    classifiers=[],
)
