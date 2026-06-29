class Node { 
public: 
    int key;
    int val;
    Node* next;
    Node* prev;



    Node(int key, int val) {
        this->key = key;
        this->val = val;
        this->next = nullptr;
        this->prev = nullptr;
    }
};


class LRUCache {
public:
    int capacity;
    Node* left;
    Node* right;
    unordered_map<int, Node*> mp;

    LRUCache(int capacity) {
        this->capacity = capacity;
        
        left = new Node(0,0); // we need heap allocation so when it goes out of scope it doesn't die
        // we also pass references in the functions so it's cheaper.
        right = new Node(0,0);

        left->next = right;
        right->prev = left;
    }


    
    int get(int key) {
        // if it doesn't exist in the map, remove it.
        // if this exists in the map, we sohuld remove it and reinsert it

        // remember, no refs to iterators
        auto node_it = mp.find(key);

        if (node_it == mp.end()) {
            // if that returns an invalid pointer
            return -1; 
        }

        Node* node = node_it->second; // remember we need to extract the actual node ptr from the find

        // and then if it does, we should remove it and return the value
        remove(node);
        insert(node);
        return node->val;
    }
    
    void put(int key, int value) {

        // now we have to define the put function;
        // if it already exists in the map, we shold just remove it

        if (mp.count(key) > 0) {
            // it's a old value, remove that node.
            Node* old = mp[key];
            remove(old);
            mp.erase(key);
            delete old;

        }

        // then we can construct a new node and insert it
        Node* node = new Node(key, value);
        mp[key] = node;
        insert(node);

        // then we should check the size of the map

        if (mp.size() > capacity) {
            // we need to evict the LRU
            Node* lru = left->next;
            int key = lru->key;

            // then we need to remove this from the LL

            remove(lru);

            // then we need to delete this map entry

            mp.erase(key);
            delete lru; // we have to clean up the pointer
        }
    }

    void insert(Node* node) {
        // it insert the node, we just put it at the right hand side

        Node* mru = right->prev;

        // and then we want to insert that after

        mru->next = node;
        node->prev = mru;

        node->next = right;
        right->prev = node;
    }

    void remove(Node* node) {

        Node* next = node->next;
        Node* prev = node->prev;

        next->prev = prev;
        prev->next = next;
    }

    // we should use a doubly linked list node class 

    // we can add nodes to the right - the left / front will have the LRU item
    // for the get and put we can use that to update the keys in the maps -> key -> iterator to node
    // we can add a remove node and insert node function into the map :) 
    

    // define the node class
};
