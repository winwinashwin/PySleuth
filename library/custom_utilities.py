# to compress folder into zip file

from shutil import make_archive


class Compress:
	def __init__(self, out_file_name, dirname):
		make_archive(out_file_name, "zip", dirname)
