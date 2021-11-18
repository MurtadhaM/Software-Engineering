import bcrypt
saltp = bcrypt.gensalt(14)                       # b'$2b$14$7QmgF.1F4dTKeb8o8dprEu'
hashp = bcrypt.hashpw('p@ssW0rd'.encode(), saltp)  # b'$2b$14$7QmgF.1F4dTKeb8o8dprEuo2T2Y908hdZan9fb.LDWDuibPl/SLpm'
bcrypt.checkpw('p@ssW0rd'.encode(), hashp)         # True

print(hashp)
print(saltp)
print(bcrypt.checkpw('p@ssW0rd'.encode(), hashp)  )