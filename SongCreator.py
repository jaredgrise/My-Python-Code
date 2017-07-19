print 'Jared Grise'
print 'Assingment 2 -- Song Creator'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print ' ' 

print 'Enter the first verse: ',
firstverse = raw_input()
print 'Enter the second verse: ',
secondverse = raw_input()
print 'Enter the third verse: ',
thirdverse = raw_input()
print 'Enter the forth verse: ',
forthverse = raw_input()

print 'Enter the chorus: ',
chorus = raw_input()
chorus = chorus + " "
print 'Enter the chorus repeat number: ',
repeatchorus = raw_input()

print " "
song = [" " + firstverse + " " + chorus*int(repeatchorus) + " " + secondverse + " " + chorus*int(repeatchorus) + " " + thirdverse + " " + chorus*int(repeatchorus) + " " + forthverse + " " + chorus*int(repeatchorus) + " " + chorus*int(repeatchorus) + chorus]
print song 

print ''
print "%s" % firstverse
print "%s" % chorus*int(repeatchorus)
print "%s" % secondverse
print "%s" % chorus*int(repeatchorus)
print "%s" % thirdverse
print "%s" % chorus*int(repeatchorus)
print "%s" % forthverse
print "%s" % chorus*int(repeatchorus), chorus

print ''
print "One More time!!!"
print "%s" % firstverse
print "%s" % chorus*int(repeatchorus)
print "%s" % secondverse
print "%s" % chorus*int(repeatchorus)
print "%s" % thirdverse
print "%s" % chorus*int(repeatchorus)
print "%s" % forthverse
print "%s" % chorus*int(repeatchorus), chorus





