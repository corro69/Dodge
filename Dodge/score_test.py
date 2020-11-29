import pickle
import os

x = 0

score_save = int(x)
pickle_out = open("data/score.dat","wb")
pickle.dump(score_save, pickle_out)
pickle_out.close()

#score_save.remove()

#pickle_in = open("score.dat", "rb")
#score_save = pickle.load(pickle_in)

print(score_save)
#print(score_save[1])
