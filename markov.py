import math
AnswerExpected = 0.985093

fr = 0.00001
t = 7500

Rel = (3*math.exp(-fr*t) + 3*(2*math.exp(-fr*t)*(1-math.exp(-fr*t))))
Rel2 = 3*math.exp(-fr*t) + 3*(2*math.exp(-fr*t)*(1-math.exp(-fr*t)))
print("REL = ", Rel)
print("REL2 = ", Rel2)