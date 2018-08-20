import os
import time
import numpy as np


class Dataset(object):
	"""Dataset of game plays"""
	def __init__(self, dataset_path):
		self.dataset_path = dataset_path
		self.games_dir = next(os.walk(dataset_path))[1]
		self.games = self.load_games()

	def load_games(self):
		game_info = os.listdir(os.path.join(self.dataset_path, self.games_dir[0]))
		info_tag = [os.path.splitext(info)[0] for info in game_info]
		base_game_dict = {tag: [] for tag in info_tag}

		games_data = []
		games_path = [os.path.join(self.dataset_path, g) for g in self.games_dir]
		for path in games_path:
			game_name = os.path.basename(path)
			game_info = base_game_dict.copy()
			for data_name, data_value in game_info.items():
				csv_file = os.path.join(path, data_name+'.csv')
				data_value = np.genfromtxt(csv_file, delimiter=',')
				print(len(data_value))
			game_info['name'] = game_name



if __name__ == '__main__':
	dataset_path = os.path.join(os.path.dirname(__file__), 'Dataset')
	dataset = Dataset(dataset_path)




