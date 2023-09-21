# .NET Environment Setup Guide
This repo contains assets and template for .NET Environment Setup Guide and a small python scripts to managing links to website and images a little less painful

## The Python Script
This script reads a markdown file, scans for variables and collections, replaces it with whatever it matches in config.json, and writes to a specified file name.


### Required:
- Python 3
- a markdown file to be used as a template
- config.json file with the following required properties:
  - "templateFile": path to the template markdown file
  - "outputFile": path to the output file. Will overwrite if it already exists

### To Run
Execute `python script.py`

### Variables
variables begins with $ symbol and looks for the 1-1 match in the "variables" object in config.json
  
  EX:
  template.md
  ```
    $foo
  ```

  config.json
  ```json
    {
      "templateFile": "template.md",
      "outputFile": "output.md",
      "variables": {
        "foo": "bar"
      }
    }
  ```

  output.md
  ```
    bar
  ```

### Collection
collections begin with @ symbol, and must be followed by . (dot) and an integer value. It is used to contain many related links that does not all necessarily need unique names.

  template.md
  ```
    @fruits.0
    @fruits.1
  ```

  config.json
  ```json
    {
      "templateFile": "template.md",
      "outputFile": "output.md",
      "collections": {
        "fruits": ["apple", "banana"]
      }
    }
  ```

  output.md
  ```
    apple
    banana
  ```