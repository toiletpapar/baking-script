# baking-script
A short python script to demonstrate the language

# Requirements
This document describes the functionalities of a script that ingests data pulled from the Internet into a useful information in the context of baking. The goal of the script is to contain little maintenance and simple interface. It will provide the average number of ingredients in a specified recipe across multiple data sources.

## Analysis
Things to keep in mind

### Measurements
There are four kinds of ways to describe an ingredient:
* By weight (mg, g, oz, pound)
* By volume (tsp, tbsp, cup, pint)
* By words (dozen, some, a, couple)
* By non-standard unit (e.g. 3 eggs)

## Functional Requirements 
* It should support multiple data sources including:
  * TBD
* The data sources to use should be read from a user provided file called `sources.json`
* It should take one argument called `query` which describes the recipes to search for
* It should should write a CSV file called `ingredients.csv` that contains:
  * The name of the ingredient
  * The average number of that ingredient to use in:
    * By weight: g
    * By volume: ml
    * All words should be converted to numbers (e.g. dozen => 12) and treated as non-standard units
    * All non-standard units should be written without a unit
  * The number of times that ingredient was found in a recipe (to remove outliers)
* It should support the following standard units:
  * By weight: milligrams, mg, grams, g, ounce(s), oz, pound(s), lb
  * By volume: tsp, teaspoon(s), tbsp, tablespoon(s), cup(s), millilitres, ml, litres, L
  * By words: dozen (12), a (1)
* It should stop after scanning **200** recipes from each data source
  
## Technical Requirements (and technical guidelines)
A skeleton to make the codebase understandable and maintainable. Should make development easier.

### Managing Different Data Sources (strategies)
Each data source will have a different way of obtaining it's information, yet the information we want to extract is standard. By utilizing a strategy we can opt-in to different data sources that we support and drop data sources we no longer want to support without affecting other parts of the code.

Write a function for each data source (called a strategy) with the following interface:
```
interface Ingredient {
  name: string,
  unit: <all supported units> or None for non-standard,
  amount: number
}
type Recipe = Ingredient[]

strategy(query: string) => Recipe[]
```

### Qualification
There are a variety of ways to tweak how we qualify recipes. This can change based on the needs of the user and our data sources. If we find that our data sources have to little information with respect to some recipes, then the user might want to tweak the qualifier such that it is more lenient. If we find that we're picking up too many recipes that are not relevant, than we may choose to tweak it to consider more variables. For simplicity, we choose to use one qualifier for all data sources rather than a one-to-one pairing of qualifiers to data sources.

Write a function that qualifies a recipe with the following interface:
```
qualify(recipeName: string, query: string): boolean
```
Only qualified recipes should be counted towards the ingredient average

### Managing Measurements
A helper to make life easier.

Write a function that can convert `x` standard units into `y` of the unit specified in the report (i.e. g, ml, numbers). 
* Example: mg => g, dozen => 12, g => g

### Making Web Requests to Data Sources
I suggest using the requests library

### Parsing the HTML Document
I suggest using an XML parser like `ElementTree`.

See https://stackoverflow.com/questions/33747603/how-to-parse-html-using-elementtree-to-find-a-particular-regex

## Pitfalls
* Sometimes there are multiple words that refer to the same ingredient
* Strategies will become outdated as the data sources get updated
* The amount of the food produced is not quantifiable (3 cookies? What if they're really big cookies? What's the quantifiable definition of a serving anyway?)
* The quality of the recipe is not factored (yet)

# Setup
1. Clone this skeleton repository `git clone https://github.com/toiletpapar/baking-script.git`
2. Install python at https://www.python.org/downloads/
3. Setup your working directory for python `python3 -m venv baking-script`
4. Navigate to your working directory `cd baking-script`
5. Activate your working directory (in Windows) `bin/activate`
6. Install the required dependencies for this script `pip install -r requirements.txt`
7. Start hacking in `script.py`
