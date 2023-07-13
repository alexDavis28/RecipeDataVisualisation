import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import random

# relations between each recipe and ingredient

ingredients_df = pd.read_csv("top100ingredients.csv")
print(ingredients_df.head())
print(ingredients_df.columns.tolist())

ingredient_names = ingredients_df["ingredient name"].tolist()
ingredient_ids = ingredients_df["ingredient id"].tolist()
ingredient_dict = {i_id: name for name, i_id in zip(ingredient_names, ingredient_ids)}
print(ingredient_dict)


connections = pd.read_csv("has_ingredients.csv")
connections = zip(connections["recipe id"].tolist(), connections["ingredient id"].tolist())
# filter to be relevant
connections = [i for i in connections if i[1] in ingredient_ids]

recipes_df = pd.read_csv("recipes.csv")
print(len(recipes_df))
recipes = zip(recipes_df["recipe id"].tolist(), recipes_df["title"].tolist())
recipes_dict = {i: name for i, name in recipes}
recipes = [i for i in recipes if i[0] in [c[0] for c in connections]]
recipes = recipes[:10]
recipe_names = [i[1] for i in recipes]

connections = [(recipes_dict[i[0]], ingredient_dict[i[1]]) for i in connections]
print(connections[:10])
print("graphing")
Graph = nx.Graph()
print("recipes")
Graph.add_nodes_from(recipe_names)
print("ingredients")
Graph.add_nodes_from(ingredient_names)
print("edges")
print(len(connections))
random.shuffle(connections)
Graph.add_edges_from(connections[:10])


nx.draw_networkx(Graph, with_labels=True)
plt.show()