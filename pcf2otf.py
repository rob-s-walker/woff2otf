from fontTools import ttLib
import os

for file in os.listdir("./"):
    if file.endswith(".woff"):
        source_file_name = file
        target_file_name = source_file_name.rsplit('.', 1)[0] + '.otf'
        font = ttLib.TTFont(source_file_name)
        font.flavor = None  # was "woff"; `None` restores the default value, for non-compressed OpenType
        font.save(target_file_name)
    if file.endswith(".woff2"):
        source_file_name = file
        target_file_name = source_file_name.rsplit('.', 1)[0] + '.otf'
        font = ttLib.TTFont(source_file_name)
        font.flavor = None  # was "woff"; `None` restores the default value, for non-compressed OpenType
        font.save(target_file_name)
