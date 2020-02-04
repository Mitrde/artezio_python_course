import xml.etree.ElementTree as Et


def xml_parser(xml_string):
    """func takes xml document and returns dictionary with hierarchy and depth of nested elements"""
    def rec_parse(elements):
        """recursively add nodes to the dictionary"""
        node = {"name": elements.tag, "children": []}
        for elem in elements:
            node["children"].append(rec_parse(elem))
        if len(elements) > 0:
            rec_parse.max_depth += 1
        return node

    root = Et.fromstring(xml_string)
    rec_parse.max_depth = 0
    xml_dict = rec_parse(root)
    print(xml_dict, ", ", rec_parse.max_depth)

    return xml_dict, rec_parse.max_depth
