import requests
import lxml.html
import re
from io import StringIO

def qualify(query, recipeName):
  # Write code to tighten or relax which recipes to use
  return re.search(query, recipeName, flags=re.IGNORECASE)

def convert(ingredient, toUnit):
  # Write code to convert between units (e.g. mg => g)
  return {
    "name": ingredient.name,
    "unit": toUnit,
    "amount": ingredient.amount
  }

def parseNumber(text):
  # Write code to convert text into numbers (e.g. "1/2" => 0.5)
  return 0.5

# Strategy for parsing ingredients from smittenkitchen
def smittenRecipes(query):
  def retrieveArticles():
    payload={"s": query}
    r = requests.get("https://smittenkitchen.com/", params=payload)
    tree = lxml.html.parse(StringIO(r.text))
    articles = tree.getroot().find_class('post')

    return articles

  def isArticleRecipe(article):
    label = article.find_class('smittenkitchen-primary-category')[0]
    return label.text_content() == 'Recipes'

  def retrieveLinks(articles):
    links = []
    for article in articles:
      recipeName = article.find_class('entry-title')[0].text_content()
      if (isArticleRecipe(article) and qualify(query, recipeName)):
        links.append(article.find_class('entry-header')[0][0].get('href'))
    return links

  def getIngredients(link):
    print("Gathering ingredients from: " + link)
    def parseIngredientText(text):
      # Write code to parse ingredients here ("1/2 cup butter" => {name: butter, unit: "cup", amount: 0.5})
      return {
        "name": text.split(" ", 2)[2],
        "unit": text.split(" ", 2)[1],
        "amount": text.split(" ", 1)[0]
      }

    r = requests.get(link)
    tree = lxml.html.parse(StringIO(r.text))
    ingredient_elements = tree.getroot().find_class('jetpack-recipe-ingredient')
    ingredients = []

    for ingredient_element in ingredient_elements:
      ingredients.append(parseIngredientText(ingredient_element.text_content()))

    return ingredients

  articles = retrieveArticles()
  links = []
  recipeIngredients = []
  if articles is not None:
    # links = retrieveLinks(articles)
    links = ["https://smittenkitchen.com/2018/02/chocolate-peanut-butter-cup-cookies/"]
    for link in links:
      recipeIngredients.append(getIngredients(link))

  return recipeIngredients

# main
print(smittenRecipes('cookies'))

# r = requests.get("https://smittenkitchen.com/recipes/")
# tree = lxml.html.parse(StringIO(r.text))

# print(html.findall(".//h2"))
# print(etree.tostring(html, pretty_print=True, method="html"))

# allElements = tree.getroot().find_class('section')

# Find all elements and split on the first occurrence of a space
# if allElements is not None:
#   for element in allElements:
#     text = element.text
#     if text is not None:
#       print(text.split(" ", 1))

# Find all elements and show each elements attributes
# for element in allElements:
#   print(element.keys())