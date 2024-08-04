class FileSystem:
    def __init__(self):
        self.root = {'val': '*'}

    def split_path(self, path):
        return path[1:].split("/")

    def get_node(self, path):
        names = self.split_path(path)
        cur = self.root
        for name in names[:-1]:
            if name in cur.keys():
                cur = cur[name]
            else:
                raise Exception("invalid parent")

        return cur, names

    def create(self, path, value):
        cur, names = self.get_node(path)

        cur[names[-1]] = {"_val": value}

    def get(self, path):
        cur, names = self.get_node(path)

        if names[-1] in cur:
            return cur[names[-1]]['_val']
        else:
            raise Exception("invalid path")

    def set(self, path, value):
        cur, names = self.get_node(path)

        if names[-1] in cur:
            cur[names[-1]]['_val'] = value
        else:
            raise Exception("invalid path")

    def delete(self, path):
        cur, names = self.get_node(path)

        # delete names[-1] if it exists and no other change
        if names[-1] in cur and set(cur[names[-1]].keys()) == '_val':
            del cur[names[-1]]
        else:
            raise Exception("invalid path")

def main():
    fs = FileSystem()

    fs.create("/abc", "val1")
    assert fs.get("/abc") == 'val1', 'fails'

    fs.create("/abc/bcd", "val2")
    assert fs.get("/abc/bcd") == "val2", 'fails'
    # fs.delete("/abc")

    # fs.delete("/bcd")
    fs.set("/abc", "val3")
    assert fs.get("/abc") == "val3"

    # fs.delete("/")
    # fs.delete('/abc/bcd/def')
    # fs.create("/acd/bcd", "val4")
    # fs.get("/aaa")


if __name__ == "__main__":
    main()