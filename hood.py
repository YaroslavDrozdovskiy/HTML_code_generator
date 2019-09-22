
class HTML:
    def __init__(self, output=None):
        self.output = output
        self.children = []

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        if self.output is None:
            children = [str(i) for i in self.children]
            into_tag = "\n".join(children)
            print("<html>\n{into_tag}\n</html>".format(into_tag=into_tag))
        else:
            fp = open(self.output, 'w')
            children = [str(i) for i in self.children]
            into_tag = "\n".join(children)
            print("<html>\n{into_tag}\n</html>".format(into_tag=into_tag), file=fp)
            fp.close()


# добавляем теги BODY и HEAD
class TopLevelTag:
    def __init__(self, tag):
        self.tag = tag
        self.children = []

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __enter__(self):
        return self

    def __str__(self):
        if self.children:
            children = [str(i) for i in self.children]
            into_tag = "\n".join(children)
            return "<{tag}>\n{into_tag}\n</{tag}>".format(tag=self.tag, into_tag=into_tag)
        else:
            return "<{tag}\n</{tag}>".format(tag=self.tag)

    def __exit__(self, *args, **kwargs): pass


class Tag:
    def __init__(self, tag, class_=None, is_single=False, **kwargs):
        self.tag = tag
        self.text = ""
        self.attributes = {}
        self.children = []
        self.is_single = is_single
        if class_ is not None:
            self.attributes["class"] = " ".join(class_)
        for attr, value in kwargs.items():
            if "_" in attr:
                attr = attr.replace("_", "-")
            self.attributes[attr] = value

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __enter__(self):
        return self

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)
        if self.children:
            children = [str(i) for i in self.children]
            into_tag = "\n".join(children)
            return "<{tag}>{text}\n{into_tag}\n</{tag}>".format(tag=self.tag, text=self.text, into_tag=into_tag)
        elif self.is_single:
            return "<{tag} {attrs}/>".format(tag=self.tag, attrs=attrs)
        else:
            return "<{tag} {attrs}>{text}</{tag}>".format(tag=self.tag, attrs=attrs, text=self.text)

    def __exit__(self, *args, **kwargs): pass
