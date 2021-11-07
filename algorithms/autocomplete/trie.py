import json
import yaml

class Trie:
    def __init__(self):
        self.root_path = autocomplete_config()['root_path']
        f = open(self.root_path, encoding="utf-8")
        self.root = json.load(f)

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['is_word'] = 0
    
    def has_word(self, word):
        node = self.root
        words = self.get_prefixes(node, word, 0)
        for word in words:
            node = self.root
            for char in word:
                if char not in node:
                    return False
                node = node[char]
            if 'is_word' not in node:
                return False
            else:
                return word

    def match_prefix(self, prefix, k=10):
        if not prefix.isspace() and prefix:
            node = self.root
            prefixes = self.get_prefixes(node, prefix, 0)
            matches = []
            for pref in prefixes:
                node = self.root
                for char in pref:
                    node = node[char]
                matches.extend(self.search_prefix(node, pref))
            matches.sort(key=lambda x : x[1], reverse=True)
            res = [matches[i][0] for i in range(len(matches))]
            if k > len(matches):
                return res
            return res[:k]
        return []
    
    def search_prefix(self, node, prefix):
        res = []
        for char in node.keys():
            if char == 'is_word':
                res.append([prefix, node['is_word']])
            else:
                res.extend(self.search_prefix(node[char], prefix + char))
        return res
    
    def get_prefixes(self, node, prefix, i):
        res = []
        if i == len(prefix):
            return [prefix]
        suffix = ""
        if i + 1 < len(prefix):
            suffix = prefix[i + 1 : ]
        for char in node:
            if char == prefix[i].lower():
                    new_prefix = prefix[: i] + prefix[i].lower() + suffix
                    res.extend(self.get_prefixes(node[char], new_prefix, i + 1))
            if char == prefix[i].upper() and prefix[i].lower() != prefix[i].upper():
                new_prefix = prefix[: i] + prefix[i].upper() + suffix
                res.extend(self.get_prefixes(node[char], new_prefix, i + 1))
        return res

    def update_root(self, word):
        node = self.root
        for char in word:
            node = node[char]
        node['is_word'] += 1
        with open(self.root_path, 'w') as fp:
            json.dump(self.root, fp)
        return node['is_word']


def autocomplete_config():
    with open('algorithms/algorithms_config.yaml') as f:
        config = yaml.safe_load(f)
    return config['auto_complete']