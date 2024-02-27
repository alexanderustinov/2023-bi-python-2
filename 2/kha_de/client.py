import socket
import pickle
from common import AAA

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(AAA)
inf = pickle.loads(s.recv(500))
print(f"Penguin's species - {inf.species}. "
      f"Their average height is {inf.height} and weight is from {inf.weight[0]} to {inf.weight[1]}. "
      f"Besides, they can reach the age of {inf.age}.")