class Node {
public: 
    int key;
    int val;
    Node* prev;
    Node* next;

    // constructor
    Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
};


class LRUCache {
public:
    LRUCache(int capacity) {
        cap = capacity;
        cache.clear(); // sets this to empty

        left = new Node(0,0);
        right = new Node(0,0);

        left->next = right;
        right->prev = left;
    }
    
    int get(int key) {
        // if it's not in the map, throw negative one

        // if it exists in the map and it's not out of bounds / null
        if (cache.find(key) != cache.end()) {
            Node* node = cache[key];

            remove(node);
            insert(node);
            return node->val;
        }
        return -1;
    }
    
    void put(int key, int value) {
        // we can put the node into the map
        // if it already exists in the map, then we can remove it.


        if (cache.find(key) != cache.end()) {
            // remove takes in a pointer
            remove(cache[key]);
        }

        // we want to create a new node to insert
        // use new to alloc memory

        Node* node = new Node(key, value);

        // add to cache
        cache[key] = node;

        // insert to LL
        insert(node);

        if (cache.size() > cap) {
            // evict the lru
            Node* lru = left->next;
            remove(lru);

            // then we need evict from the map
            cache.erase(lru->key); // we need to remove the key itself
            delete lru; // need to free the memory

        }
    }

    // you need to use a doubly linked list with node class
    // need also a delete method 
    // need a insert method

private:
    int cap;
    unordered_map<int, Node*> cache;
    Node* left; // left is lru, right is end that we can append recently get nodes to.
    Node* right; 

    // remove and insert adjust pointers.
    // get and put adjust mappings these methods should just take in nodes

    void insert(Node* node) {
        // we insert a pointer at the right
        // this particular node goes to the right end 

        Node* mru = right->prev;

        // we extend mru to point to new node
        mru->next = node;
        right->prev = node;

        node->next = right;
        node->prev = mru;
    }

    void remove(Node* node) {
        // we want to delete the node at a given spot
        Node* prev = node->prev;
        Node* next = node->next;

        prev->next = next;
        next->prev = prev;
    }


};
