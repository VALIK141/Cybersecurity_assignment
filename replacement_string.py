#!/usr/bin/python


string = "Master Ik is the tutor, the students are Valentine, Helena AND Esther. We are Zealous learners."
encripted_string = string.translate(str.maketrans('eAbBoisFpZ', '3468015792'))
print(encripted_string)

