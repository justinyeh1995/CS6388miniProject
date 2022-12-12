"""
This is where the implementation of the plugin code goes.
The PetriNetClassificationPython-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase
import collections

# Setup a logger
logger = logging.getLogger('PetriNetClassificationPython')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class PetriNetClassificationPython(PluginBase):
    def main(self):
        core = self.core
        root_node = self.root_node
        active_node = self.active_node

        name = core.get_attribute(active_node, 'name')

        logger.info('ActiveNode at "{0}" has name {1}'.format(core.get_path(active_node), name))

        core.set_attribute(active_node, 'name', 'newName')

        commit_info = self.util.save(root_node, self.commit_hash, 'master', 'Python plugin updated the model')
        logger.info('committed :{0}'.format(commit_info))

        nodes = core.load_sub_tree(active_node) 
        self.namespace = None
        META = self.META
        
        places = []
        transitions = []
        arcs = []
        path2node = {}
        inplaceSet = collections.defaultdict(list)
        for node in nodes:
            path2node[core.get_path(node)] = node
            if core.is_type_of(node, META['Place']):
                places.append(node)
            elif core.is_type_of(node, META['T2PArc']):
                arcs.append(node)
            elif core.is_type_of(node, META['P2TArc']):
                arcs.append(node)
                t = core.get_pointer_path(arc, 'dst')
                p = core.get_pointer_path(arc, 'src')
                inplaceSet[t].append(p)
            elif core.is_type_of(node, META['Transition']):
                transitions.append(node)

        def free_choice(self):
            prev = set()
            for inplace in inplaceSet.values():
                if not prev & inplace:
                  return False
                prev = inplace
            return True

        def state_machine(self):
            balance = 0
            for tran in transition:
              path = core.get_path(tran)
              for arc in arcs:
                if path == core.get_pointer_path(arc, 'dst'):
                  balance += 1
                elif path == core.get_pointer_path(arc, 'src'):
                  balance -= 1
            res = balance <= 1 and balance >= -1
            return res

        def marked_graph(self):
            for tran in transitions:
              path = core.get_path(tran)
              inplace = 0
              for arc in arcs:
                if path == core.get_pointer_path(arc, 'dst'):
                  inplace += 1
                if inplace != 1:
                  return False

            for place in places:
              path = core.get_path(place)
              outplace = 0
              for arc in arcs:
                if path == core.get_pointer_path(arc, 'src'):
                  outplace += 1
                if outplace != 1:
                  return False
            return True

        def workflow(self):
            return True

        if self.free_choice():
            self.send_notification("This is a Free Choice PetriNet")
        if self.state_machine():
            self.send_notification("This is a StateMachine")
        if self.marked_graph():
            self.send_notification("This is a Marked Graph!")
        if self.workflow():
            self.send_notification("This is a Workflow PetriNet")

