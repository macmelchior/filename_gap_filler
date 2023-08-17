#! python3
# renames files so that gaps in filename numeration are filled

import os
import re
import shutil


def gap_filler(names):
    for i, name in enumerate(names[:-1]):
        digits_1 = re.findall(r'\d+', name)
        digits_2 = re.findall(r'\d+', names[i + 1])
        try:
            digits_len = len(str(digits_2[0]))
            digits_1 = int(digits_1[0])
            digits_2 = int(digits_2[0])
            if digits_2 - digits_1 != 1:
                digits_2 = digits_1 + 1
                digits_2 = str(digits_2).zfill(digits_len)
                prefix = re.search(r'^(.+)\d{3}', names[i + 1]).group(1)
                suffix = re.search(r'\.(\D|\S{3})$', names[i + 1]).group(0)
                new_filename = f'{prefix}{digits_2}{suffix}'
                shutil.move(names[i + 1], new_filename)
        except IndexError:
            pass


if __name__ == "__main__":
    namelist = (os.listdir('./'))
    gap_filler(namelist)
