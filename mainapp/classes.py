class BreadCrumb:

    def __init__(self, name, href):
        self.name = name
        if href == '/':
            self.href = href
        else:
            self.href = '/' + str(href) + '/'
