import pandas as pd
import json

def main():
	df = pd.read_csv('sorted.csv')
	data = []
	for i in range(df.shape[0]):
		point = {}
		row = df.iloc[i]
		fields = ['created_at', 'description', 'html_url', 'name', 'type'] 
		for field in fields:
			point[field] = row[field]
		point['type'] = int(point['type'])
		point['index'] = i
		data.append(point)
	with open("output.json", "w") as f:
		f.write(json.dumps(data))



if __name__ == "__main__":
	main()