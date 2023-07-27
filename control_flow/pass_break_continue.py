# pass, break, continue keywords are used to control or disrupt loops

# when pass is placed under a condition, nothing gets executed
# break keyword terminates a loop after a certain condition is met
# continue keyword skips over an iteration and goes onto the next one when the condition is met

names = ['Amanda', 'Mercedes', 'Rachel', 'Elisabeth', 'Tay', 'Xavier', 'Joaquin', 'Sam']

for name in names:
    if 'm' in name.lower():
        continue
    elif 'r' in name.lower():
        pass
    elif 'j' in name.lower():
         break
    else:
        print(name)
        