/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:



    Node* cloneGraph(Node* node) {
        // we create a mapping of the nodes
        // then we can go through and create a copy of the new node
        // then we can go through and then iterate through those neighbors

        // we can use a dfs for this

        // we use an ordered map...

        map<Node*, Node*> oldToNew;
        return dfs(node, oldToNew);


    }

    Node* dfs(Node* node, map<Node*, Node*>& oldToNew) {
        if (node == nullptr) {
            return nullptr;
        }

        if (oldToNew.count(node)) {
            // if it's already in the map , return it
            return oldToNew[node];
        }

        Node* copy = new Node(node->val);
        oldToNew[node] = copy;

        for (Node* nei : node->neighbors) {
            copy->neighbors.push_back(dfs(nei, oldToNew));
        }
        return copy; 
    }
};
