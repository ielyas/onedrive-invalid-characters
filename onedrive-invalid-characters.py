import os

# DON'T FORGET TO CHANGE THE PATH OF YOUR ONEDRIVE FOLDER
path = "/Users/elyas/Library/CloudStorage/OneDrive-Personal"
forbidden = ['\\ ', '/', '|', ':', '*', '?', '"', '<', '>', '�']
counter = 0

for root, dirs, files, in os.walk(path, topdown=False):
	for name in files:
		name.strip()
		if any(map(name.__contains__, forbidden)):
			
			counter += 1

			old_name = os.path.join(root, name)

			for i in name:
				if any(map(i.__contains__, forbidden)):

					new_name = name.replace(i, "-")
					new_path = os.path.join(root, new_name)

			os.rename(old_name, new_path)
			print("changed file name from: ", old_name)
			print("to: ", new_path)

if counter < 1:
	print("No files with forbidden characters found.")
else:
	print("Found ", counter, " files with forbidden characters.")
