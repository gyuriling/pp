gugudan = list()

for dan in range(2,10):
    gugudan.append('===={0}단===='.format(dan))
    for su in range(1,10):
        sentence = '{0} * {1} = {2}'.format(dan,su,dan*su)
        gugudan.append(sentence)


for su in gugudan:
    #if su[0] == '3' or su[0] == '6':
        #continue
    
    if su[len(su)-1] == '3' or su[len(su)-1] == '6':
        continue

    
    
    #if len(su)==9 and (su[8:]==('3') or su[8:]==('6')):
        #continue
    #if su[9:]==('3') or su[9:]==('6'):
        #continue
        
    print(su)
