def weight_on_planets():
	weight = int(input("What do you weigh on earth? "))
	mars_wt = weight * 0.38
	jupiter_wt = weight * 2.34
	print()
	(print("On Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(mars_wt, jupiter_wt)))
   
if __name__ == '__main__':
   weight_on_planets()
