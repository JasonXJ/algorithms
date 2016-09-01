#include <cstdlib>
#include <cstdio>
#include <map>
#include <set>

using namespace std;

struct Node {
    int data;
    Node *child1, *child2;
};

Node *DeepCopyNodeChainRecursion(const Node *node, map<const Node*, Node*> *node_map) {
    if (node == NULL)
        return NULL;

    map<const Node*, Node*>::iterator new_node_iterator = node_map->find(node);
    if (new_node_iterator != node_map->end())
        return new_node_iterator->second;

    Node *new_node = new Node;
    new_node->data = node->data;
    (*node_map)[node] = new_node;
    new_node->child1 = DeepCopyNodeChainRecursion(node->child1, node_map);
    new_node->child2 = DeepCopyNodeChainRecursion(node->child2, node_map);

    return new_node;
}

Node *DeepCopyNodeChain(const Node *node) {
    map<const Node*, Node*> node_map;
    return DeepCopyNodeChainRecursion(node, &node_map);
}

void PrintChild(const Node *child) {
    if (child == NULL)
        printf("Child NULL; ");
    else
        printf("Child %d (%p); ", child->data, child);
}

void DeepFirstPrint(const Node *node, set<const Node*> *visited_nodes) {
    if (node == NULL or visited_nodes->count(node) != 0)
        return;
    visited_nodes->insert(node);

    printf("Node %d (%p): ", node->data, node);
    PrintChild(node->child1);
    PrintChild(node->child2);
    printf("\n");
    
    DeepFirstPrint(node->child1, visited_nodes);
    DeepFirstPrint(node->child2, visited_nodes);
}

void DeepFirstPrint(const Node *node) {
    set<const Node*> visited_nodes;
    DeepFirstPrint(node, &visited_nodes);
}

int main(int argc, char *argv[])
{
    Node node1 = {1, NULL, NULL},
         node2 = {2, NULL, NULL},
         node3 = {3, NULL, NULL},
         node4 = {4, NULL, NULL},
         node5 = {5, NULL, NULL},
         node6 = {6, NULL, NULL},
         node7 = {7, NULL, NULL};

    node1.child1 = &node2;
    node1.child2 = &node3;
    node2.child1 = &node4;
    node2.child2 = &node5;
    node3.child1 = &node5;
    node3.child2 = &node6;
    node5.child1 = &node5;
    node5.child2 = &node5;
    node6.child1 = &node7;
    node6.child2 = &node1;
    node7.child1 = &node2;
    node7.child2 = &node6;

    DeepFirstPrint(&node1);

    Node *nodex = DeepCopyNodeChain(&node1);
    printf("---------------------------------------------\n");
    DeepFirstPrint(nodex);
    
    return 0;
}
