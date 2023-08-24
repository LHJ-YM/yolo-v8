import os
import yaml
desired_caps = {
                'train': 'paper_data/train.txt',
                'val': 'paper_data/val.txt',
                'nc': 2,
                'names': ['wire','spot']
                }

curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath, "./wire.yaml")

# 写入到yaml文件
with open(yamlpath, "w", encoding="utf-8") as f:
    yaml.dump(desired_caps, f)