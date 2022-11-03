from setuptools import setup, find_packages
import os


setup(
    url = 'https://gitlab.com/optimization-tasks-in-machine-learning/tz9_merging_library',
    version = '0.1.0',
    name = 'tz9_merging_library',
    description = 'ТЗ9 Объединенная библиотека',
    author = 'Группа ПМ19-1',
    author_email = 'leonidalekseevv@mail.ru',
    license = 'MIT',
    python_requires = '>=3.7',
    package_data = {
        '': ['*.pyc'],
    },
    package_dir = {
        '': os.path.dirname(os.path.realpath(__file__)),
    },
    packages = [
        'tz8_stochastic_optimization',
        'tz7_cutting_optimisation',
        'tz6_classification',
        'tz5_constrained_optimization',
        'tz4_regression',
        'tz3_multidimensional_optimization',
        'tz2_numerical_optimization',
        'tz1_find_extremums',
    ],
)
