#!/usr/bin/python

import note
from time import strptime

name = "Minke Zhang"
email = "mzhang@blogzhang.com"
task = "go home to gheoaiwphgwoepahgoewahgo weahgoewhao ewioa hgeowa hgoiwea hgioewap hgiowea hgiopewa hgoiewagoi haewoipghewaioh gpowae hgoewa hgoipewah gpweoa"
time = strptime("Apr 05 2011 23:33", "%b %d %Y %H:%M")

print note.note(name, email, task, time, 1)
