def doc_to_plist(doc, excel=False):
    if not excel:
        with open(doc) as d:
            courses=[]
            for entry in d:
                courses+=[[e for e in entry]]

