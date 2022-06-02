from fontTools import ttLib
font = ttLib.TTFont("D:\\Downloads\\woff2ttf\\Reformation_v0.1-Regular.woff2")
font.flavor = None  # was "woff"; `None` restores the default value, for non-compressed OpenType
font.save("D:\\Downloads\\woff2ttf\\Reformation_v0.1-Regular.otf")