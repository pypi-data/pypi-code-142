import os
import re
import sys
import inspect
import importlib_metadata
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to sources')
    args = parser.parse_args()

    buildtin_modules = set(sys.builtin_module_names)

    lib_path = os.path.dirname(inspect.getfile(re))

    python_dist_modules = {os.path.splitext(name)[0] for name in os.listdir(lib_path)}

    local_modules = set()
    for root, dirs, files in os.walk(args.path):
        for name in files:
            name_ext = os.path.splitext(name)
            if name_ext[1] != '.py':
                continue
            if name == '__init__.py':
                local_modules.add(os.path.basename(root))
                continue
            local_modules.add(name_ext[0])

    dep_modules = set()

    def test_import(name):
        if name == '':
            return
        if name not in local_modules and name not in buildtin_modules and name not in python_dist_modules:
            dep_modules.add(name)

    for root, dirs, files in os.walk(args.path):
        for file_name in files:
            if os.path.splitext(file_name)[1] != '.py':
                continue
            path = os.path.join(root, file_name)
            with open(path, encoding='utf-8') as f:
                lines = [line for line in f if re.search('\\bimport\\b', line)]
            for line in lines:
                match = re.match('^\\s*from\\s+(.*)\\s+import', line)
                if match:
                    name = match.group(1).strip().split('.')[0]
                    test_import(name)
                    continue
                match = re.match('^\\s*import\\s+(.*)', line)
                if match:
                    items = [item.strip() for item in  match.group(1).strip().split(',')]
                    for item in items:
                        item = item.strip()
                        match_ = re.match('(.*)\\s+as\\s+', item)
                        if match_:
                            name = match_.group(1).strip().split('.')[0]
                            test_import(name)
                            continue
                        name = item.split('.')[0]
                        test_import(name)
                    continue

    dep_packages = set()
    for mod_name, pak_names in importlib_metadata.packages_distributions().items():
        if mod_name in dep_modules:
            for name in pak_names:
                dep_packages.add(name)

    dep_packages = list(dep_packages)
    dep_packages.sort()

    for name in dep_packages:
        print(name)

if __name__ == "__main__":
    main()
