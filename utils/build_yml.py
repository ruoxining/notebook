"""Script to build outline."""
import os

import yaml


def main():
    """Main function to build the outline."""
    # define path
    path_yml = 'outline'

    # read and concat ymls
    # main file
    with open(f'{path_yml}/main.yml', encoding='utf-8') as stream:
        try:
            yml_main = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    # rest files
    yml_idc = ['1-cs', '2-ling', '3-ml', '4-math', '5-misc', '6-life']
    for yml_idx in yml_idc:
        with open(f'{path_yml}/{yml_idx}.yml', encoding='utf-8') as stream:
            try:
                yml_sec = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        yml_main['nav'].append(yml_sec)

    with open('mkdocs.yml', 'w', encoding='utf-8') as outfile:
        yaml.dump(yml_main, outfile, allow_unicode=True, default_flow_style=False, sort_keys=False)


if __name__ == '__main__':
    main()
