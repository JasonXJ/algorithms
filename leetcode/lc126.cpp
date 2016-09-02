#include <vector>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_set>
#include <unordered_map>

using namespace std;

class Solution {
public:
    class TrieFuzzySearcher;

    class Trie {
        friend class TrieFuzzySearcher;

        struct Node {
            Node *children[26] = {nullptr};
        };

        Node *root;
        Node *search_middle_node = nullptr;

        void delete_node(Node *n) {
            for (size_t i = 0; i < sizeof(n->children)/sizeof(n->children[0]); ++i) {
                Node *nn = n->children[i];
                if (nn != nullptr)
                    delete_node(nn);
            }
        }
        
    public:
        Trie() {root = new Node;}

        void insert(const string &word) {
            Node *cursor = root;
            for (size_t i = 0; i < word.size(); ++i) {
                size_t code = word[i] - 'a';
                if (cursor->children[code] == nullptr)
                    cursor->children[code] = new Node;
                cursor = cursor->children[code];
            }
        }

        // Return all words which has only one character different
        // from `word`
        void fuzzy_find(const string &word, vector<string> &rv) {
            Node *mismatch_node = root;

            for (size_t mismatch_char_index = 0;
                    mismatch_char_index < word.size();
                    ++mismatch_char_index) {
                /* Note that this implementation make use of the
                 * property that all word has the same length */

                int current_char = word[mismatch_char_index];

                for (int i = 0; i < 26; ++i) {
                    if (mismatch_node->children[i] != nullptr &&
                            i != current_char - 'a') {
                        /* Now, the mismatch letter is used, we need
                         * to match the rest of the word */
                        Node *cursor = mismatch_node->children[i];
                        bool successful = true;
                        for (size_t j = mismatch_char_index + 1; j < word.length(); ++j) {
                            if (cursor->children[word[j] - 'a'] == nullptr) {
                                successful = false;
                                break;
                            }
                            cursor = cursor->children[word[j] - 'a'];
                        }
                        if (successful) {
                            string new_result(word);
                            new_result[mismatch_char_index] = 'a' + i;
                            rv.push_back(new_result);
                        }
                    }
                }

                mismatch_node = mismatch_node->children[current_char - 'a'];
                if (mismatch_node == nullptr) {
                    break;
                }
            }
        }

        // For debug;
        vector<string> get_all() {
            vector<string> rv;
            string current;
            _get_all(rv, current, root);
            return rv;
        }

        // For debug;
        void _get_all(vector<string> &buf, string &current, Node *current_node) {
            bool find_children = false;
            for (int i = 0; i < 26; ++i) {
                if (current_node->children[i] != nullptr) {
                    find_children = true;
                    current.push_back('a' + i);
                    _get_all(buf, current, current_node->children[i]);
                    current.pop_back();
                }
            }
            if (!find_children)  // Leaf node.
                buf.push_back(current);
        }

        ~Trie() {
            delete_node(root);
        }
    };


    struct GraphNode {
        string s;
        vector<GraphNode *> out;

        GraphNode(const string &s_): s(s_) {}
    };

    vector<vector<string>> findLadders(string beginWord, string
            endWord, unordered_set<string> &wordList) {
        assert(beginWord.length() == endWord.length() and beginWord.length() >= 1);
        Trie trie;
        for (auto it = wordList.begin(); it != wordList.end(); ++it) {
            trie.insert(*it);
        }
        trie.insert(endWord);
        auto begin_node = new GraphNode{beginWord};
        auto end_node = new GraphNode{endWord};
        unordered_set<string> visited{beginWord};
        unordered_map<string, GraphNode*> visiting;
        vector<GraphNode *> pioneers{begin_node};
        vector<string> next_strings;
        vector<GraphNode *> all_nodes{begin_node, end_node};
        
        bool target_reached = false;
        // BFS. Each iteration process one level.
        while (!target_reached && !pioneers.empty()) {
            for (auto pioneers_it = pioneers.cbegin();
                    pioneers_it != pioneers.end();
                    ++pioneers_it) {
                next_strings.clear();
                trie.fuzzy_find((*pioneers_it)->s, next_strings);
                auto end_string_it = find(next_strings.cbegin(),
                        next_strings.cend(), endWord);
                if (end_string_it != next_strings.end()) {
                    target_reached = true;
                    (*pioneers_it)->out.push_back(end_node);
                }
                if (target_reached)
                    continue;
                for (auto next_strings_it = next_strings.cbegin();
                        next_strings_it != next_strings.cend();
                        ++next_strings_it) {
                    if (!visited.count(*next_strings_it)) {
                        auto visiting_it = visiting.find(*next_strings_it);
                        if (visiting_it != visiting.end()) {
                            // A visiting node found, share the node.
                            (*pioneers_it)->out.push_back(visiting_it->second);
                        } else {
                            // This is a brand new node.
                            GraphNode *p_new_node = new GraphNode(*next_strings_it);
                            all_nodes.push_back(p_new_node);
                            (*pioneers_it)->out.push_back(p_new_node);
                            visiting[*next_strings_it] = p_new_node;
                        }
                    }
                }
            }

            // Finished one level.
            pioneers.clear();
            for (auto visiting_it = visiting.begin();
                    visiting_it != visiting.end();
                    ++visiting_it) {
                visited.insert(visiting_it->first);
                pioneers.push_back(visiting_it->second);
            }
            visiting.clear();
        }


        // Construct the results from the graph
        vector<vector<string>> rv;
        vector<string> temp;
        flatten_graph(begin_node, end_node, rv, temp);

        // Delete all seen nodes.
        for (auto seen_nodes_it = all_nodes.begin();
                seen_nodes_it != all_nodes.end();
                ++seen_nodes_it)
            delete *seen_nodes_it;

        return rv;
    }

    void flatten_graph(GraphNode *const begin_node,
            GraphNode *const end_node,
            vector<vector<string>> &container,
            vector<string> &prefix) {
        prefix.push_back(begin_node->s);
        if (begin_node == end_node) {
            container.push_back(prefix);
        } else
            for (auto next_node_it = begin_node->out.cbegin();
                    next_node_it != begin_node->out.cend();
                    ++next_node_it) {
                flatten_graph(*next_node_it, end_node, container, prefix);
            }
        prefix.pop_back();
    }
};

int main(void)
{
    //unordered_set<string> word_list = {"hat", "hbt", "ait", "bit", "hia", "hib", "aat", "abt", "hab", "abc"};
    //auto trie = Solution::Trie(word_list);
    //for (auto s: trie.get_all()) {
        //cout << s << endl;
    //}
    //cout << endl;
    //for (auto s: trie.fuzzy_find("hit")) {
        //cout << s << endl;
    //}

    string begin_word = "hit", end_word = "cog";
    unordered_set<string> word_list = {"hot","dot","dog","lot","log"};
    Solution s;
    /* Expected result:
     *    ["hit","hot","dot","dog","cog"],
     *    ["hit","hot","lot","log","cog"]
     */
    for (auto &vec: s.findLadders(begin_word, end_word, word_list)) {
        for (auto &str: vec) {
            cout << str << " ";
        }
        cout << endl;
    }

    return 0;
}
