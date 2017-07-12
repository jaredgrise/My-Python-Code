print 'Jared Grise'
print 'Assingment 1 -- Recipe Converter'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print ' ' 

print '---Original Recipe---'
print 'Enter the amount of Flour (Cups): ',
flourcups = raw_input()
print 'Enter the amount of Water (Cups): ',
watercups = raw_input()
print 'Enter the amount of salt (teaspoons): ',
saltteas = raw_input()
print 'Enter the amount of Yeast (teaspoons): ',
yeastteas = raw_input()
print 'Enter the load adjustment factor (e.g. 2.0 double the size): ',
factor = raw_input()

print ' '
print 'Thanks!'
print '---Modified Recipe---'
print 'Flour: %.2f cups. ' % (int(flourcups)*float(factor))
print 'Water: %.2f cups. ' % (int(watercups)*float(factor))
print 'Salt: %.2f teaspoons. ' % (int(saltteas)*float(factor))
print 'Yeast: %.2f teaspoons. ' % (int(yeastteas)*float(factor))
print ' '
print 'We multplied the reciple by a factor of: ', factor

