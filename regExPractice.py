# !python3

import re


oldTitle = 'Black Sails S01E01 HDTV.xvid-AFG.avi';

regex = re.compile(r'(\sHDTV\.xvid\-AFG)')

mo = regex.search(oldTitle)
mo.group()
no = regex.findall(oldTitle)

newTitle = oldTitle.replace(mo.group(), '')

print(mo.group())
print(mo.group(0))
print(no)
