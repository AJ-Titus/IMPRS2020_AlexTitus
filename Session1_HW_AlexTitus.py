# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:51:06 2020

@author: Gebruiker
"""

pip install Faker

from faker import Faker
import numpy as np

fake = Faker()
students = []

for i in range(100):
    students.append({
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'address': fake.address(),
            'maths': np.clip(normal(3, .5), 0, 4),
            'linguistics': np.clip(normal(3, .5), 0, 4),
            'psychology': np.clip(normal(3, .5), 0, 4)
            })

first_names = []
last_names = []
addresses = []
maths_grades = []
linguistics_grades = []
psychology_grades = []   

for i in range(len(students)):
    first_names.append()