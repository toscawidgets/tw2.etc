from setuptools import setup, find_packages

setup(
    name='tw2.etc',
    version='2.0a3',
    description='Random extra widgets for ToscaWidgets 2.',
    long_description = open('README.rst').read().split('.. split here', 1)[1],
    author='Ralph Bean',
    author_email='ralph.bean@gmail.com',
    url='http://toscawidgets.org/docs/tw2.core/',
    install_requires=[
        "tw2.core>=2.0b4",
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        tw2.etc = tw2.etc
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
