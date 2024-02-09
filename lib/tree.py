class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]

    while nodes_to_visit:
      current = nodes_to_visit.pop()
      if current['id'] == id:
        return current
      else:
        nodes_to_visit = nodes_to_visit + current['children']
    return None      
    ### EXAMPLES
  # def breadth_firs_traversal(node):
  #   result = []
  #   nodes_to_visit = [node]

  #   while len(nodes_to_visit) > 0:
  #     node = nodes_to_visit.pop(0)
  #     result.append(node['value'])
  #     nodes_to_visit = nodes_to_visit + nodes['children']

  #   return result

  # def depth_first_traversal(node):
  #   result = []
  #   nodes_to_visit = [node]

  #   while len(nodes_to_visit) > 0:
  #     node = nodes_to_visit.pop(0)
  #     result.append(node['value'])
  #     nodes_to_visit = node['children'] + nodes_to_visit
  #   return result  

    #ALTERNATIVE  recursive SOLUTION: 
  #def depth_first_traversal(node, result = []):
  # visit each node (add it to the list of results)
  # result.append(node['value'])
  # for child in node['children']:
  #   # visit each child node
  #   depth_first_traversal(child, result)

  # return result  