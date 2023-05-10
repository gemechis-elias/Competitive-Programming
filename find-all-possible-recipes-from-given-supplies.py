class Solution:
	def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

		g = defaultdict(list)
		in_degree = defaultdict(int)
		for r, ingred in zip(recipes, ingredients):
			for i in ingred:
				g[i].append(r)
				in_degree[r]+=1

		#print(g)
		queue = supplies[::]
		res = []
		while queue:
			#print("queue", queue, "res", res)
			ingred = queue.pop(0)
			#print(ingred)
			if ingred in recipes:
				res.append(ingred)
				
			for node in g[ingred]:
				in_degree[node]-=1
				if in_degree[node]==0:
					queue.append(node)

		return res