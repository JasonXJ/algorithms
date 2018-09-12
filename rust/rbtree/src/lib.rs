use std::rc::Rc;
use std::rc::Weak;
use std::cell::RefCell;

enum Color {
    Red,
    Black,
}

type Child<K, T> = Option<Rc<RefCell<Node<K, T>>>>;
type Parent<K, T> = Option<Weak<RefCell<Node<K, T>>>>;

struct Node<K: Ord, T> {
    key: K,
    value: T,
    color: Color,
    parent: Parent<K, T>,
    left: Child<K, T>,
    right: Child<K, T>,
}

impl<K: Ord, T> Node<K, T> {
    fn new(key: K, value: T, color: Color) -> Node<K, T> {
        Node {
            key,
            value,
            color,
            parent: None,
            left: None,
            right: None,
        }
    }

    fn new_child(key: K, value: T, color: Color) -> Child<K, T> {
        Some(Rc::new(RefCell::new(Node::new(key, value, color))))
    }
}

pub struct RBTree<K: Ord, T> {
    root: Child<K, T>,
}

impl<K: Ord, T> RBTree<K, T> {
    pub fn new() -> RBTree<K, T> {
        RBTree { root: None }
    }

    pub fn insert(&mut self, key: K, value: T) {
        let mut parent = None;
        let mut current = self.root.clone();

        while let Some(rc_node) = current {
            {
                let node = rc_node.borrow();
                current = if key < node.key {
                    node.left.clone()
                } else {
                    node.right.clone()
                }
            }
            parent = Some(rc_node);
        }
        match parent {
            Some(rc_node) => {
                let mut node = rc_node.borrow_mut();
                let node_to_fix = if key < node.key {
                    debug_assert!(node.left.is_none());
                    node.left = Node::new_child(key, value, Color::Red);
                    node.left.as_ref().unwrap().clone()
                } else {
                    debug_assert!(node.right.is_none());
                    node.right = Node::new_child(key, value, Color::Red);
                    node.right.as_ref().unwrap().clone()
                };
                self.insert_fixup(node_to_fix);
            },
            None => {
                self.root = Node::new_child(key, value, Color::Black);
            },
        }
        
    }

    fn insert_fixup(&mut self, _node: Rc<RefCell<Node<K, T>>>) {

    }
}
