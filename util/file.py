import yaml

def open_world(file_path):
    try:       
        file = open(file_path, 'r+')
        world = yaml.load(file)
        file.close()
        print 'World loaded from %s' % file_path
    except:
        print "Can't open file"
    return world
