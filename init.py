#!/usr/bin/env python3
import tomllib

# Open config file
with open("config.toml", "rb") as f:
    config = tomllib.load(f)

# Read the tex template file
with open('main.template', 'r') as file:
  template = file.read()

def replace(key, value):
    global template
    template = template.replace(f'<@{key}@>', value)


## ----------------- Replace the template values ----------------- ##

replace('title', config['title'])
replace('author', config['author'])
replace('academic_year', config['academic_year'])
replace('language', config['language'])

if config['appendix']:
    replace('appendix', '\\input{chapters/Appendix}')
else:
    replace('appendix', '')

## --------------------------------------------------------------- ##


# Write the created main.tex out again
with open('main.tex', 'w') as file:
  file.write(template)