#include <iostream>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <unordered_map>
#include <vector>
#include <cstdio>

using namespace std;

struct NumAndPos {
    int num;
    size_t pos;
};

class RandomizedCollection {
    // Map a val to a list of indices of the `random_pool`
    unordered_map<int,vector<size_t>> hash_table;
    vector<NumAndPos> random_pool;

public:
    /** Initialize your data structure here. */
    RandomizedCollection() {
        srand(time(0));
    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        auto &random_pool_indices = hash_table[val];
        size_t position = random_pool_indices.size();
        random_pool_indices.push_back(random_pool.size());
        random_pool.push_back(NumAndPos{val, position});

        return position == 0;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        auto hash_table_it = hash_table.find(val);
        if (hash_table_it == hash_table.end())
            return false;

        // Remove the item in random_pool
        {
            size_t random_pool_index = hash_table_it->second.back();
            if (random_pool_index != random_pool.size() - 1) {
                // Need to move the item at the end to fill the empty

                NumAndPos to_fill = random_pool[random_pool.size() - 1];
                random_pool[random_pool_index] = to_fill;

                // Update the entry corresponding to `to_fill` in the hash table 
                hash_table.at(to_fill.num)[to_fill.pos] = random_pool_index;
            }
            random_pool.pop_back();
        }

        // Remove it from `hash_table`
        {
            hash_table_it->second.pop_back();
            if (hash_table_it->second.empty())
                hash_table.erase(hash_table_it);
        }

        return true;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        assert(random_pool.size() > 0);
        return random_pool[rand() % random_pool.size()].num;
    }
};

int main(int argc, char *argv[])
{
    (void) argc;
    (void) argv;

    RandomizedCollection rc;
    rc.insert(1);
    rc.insert(2);
    rc.insert(1);
    rc.insert(2);
    rc.insert(3);
    rc.insert(3);
    rc.insert(2);
    rc.insert(2);
    rc.insert(3);
    rc.insert(3);

    rc.remove(3);
    rc.remove(1);
    rc.remove(2);
    rc.remove(2);

    float count[] = {0.,0.,0.};
    for (int i = 0; i < 10000; ++i) {
        ++count[rc.getRandom() - 1];
    }
    count[1] /= count[0];
    count[2] /= count[0];
    count[0] = 1;
    printf("%.3f %.3f %.3f", count[0], count[1], count[2]);

    return 0;
}
