with open('initial_source.csv') as f:
    source = [x.strip().split(',')[0] for x in f.readlines()[1:]]

print(source[:3])
