fh = file('/dev/input/mice')
while True:                 
    fh.read(3)
    print 'Mouse moved!'
