import json
import re

# Load the config file
with open('config.json') as configFile:
    config = json.load(configFile)
    print('config file loaded')

print('reading template markdown file from', config['templateFile'])
# Get the template
with open(config['templateFile'], 'r') as file:
    filedata = file.read()
print('file successfully read')

# replace function for links
def linkReplFn(arg):
    linkVar = arg.group(0).split('$')[1]
    return config['variables'][linkVar]

# this function is used to replace images
def imageReplFn(arg):
    # remove @ symbol, and split over . to get the index
    configVars = arg.group(0).split('@')[1].split('.')

    # replace the variable with the appropriate item from the collection 
    return config['collections'][configVars[0]][int(configVars[1])]

print('searching for variables to substitute')
# Anything with $ sign beforehand is for this script to replace with a variable defined in config.json 
filedata = re.sub(r'\$\w+', linkReplFn, filedata)
print('variable substitution completed')

print('searching for collections to substitute')
# we'll be using @ symbol to denote collections
# Search the text for all words beginning with '@' and replace them with appropriate item from the collection
filedata = re.sub(r'\@\w+.\d+', imageReplFn, filedata)
print('collection substitution completed')

print('writing modified buffer to the file with the name:', config['outputFile'])
# Write to the output file
with open(config['outputFile'], 'w') as file:
    file.write(filedata)
    print('file successfully written')

print('exiting, goodbye!')