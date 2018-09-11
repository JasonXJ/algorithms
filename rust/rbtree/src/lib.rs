use std::rc::Rc;
use std::rc::Weak;
use std::cell::RefCell;

enum Color {
    Red,
    Black,
}

struct Node<K: Ord, T> {
    key: K,
    value: T,
    color: Color,
    parent: Option<Weak<RefCell<Node<K, T>>>>,
    left: Option<Rc<RefCell<Node<K, T>>>>,
    right: Option<Rc<RefCell<Node<K, T>>>>,
}

impl<K: Ord, T> Node<K, T> {
    fn new(key: K, value: T, color: Color) -> Node<K, T>
    {
        Node {
            key,
            value,
            color,
            parent: None,
            left: None,
            right: None,
        }
    }
}

pub struct RBTree<K: Ord, T> {
    root: Option<Rc<RefCell<Node<K, T>>>>,
}

impl<K: Ord, T> RBTree<K, T> {
    pub fn new() -> RBTree<K, T> {
        RBTree { root: None }
    }

    pub fn insert(&mut self, key: K, value: T) {
        let &mut current = self.root;
        let &mut parent = None;
        
        loop {
            match current {
                // TODO: use `ref`?
                Some(rc_node) => {
                    let node = rc_node.borrow();
                    parent = current.clone();
                    current = if key < node.key {
                        node.left.clone()
                    } else {
                        node.right.clone()
                    };
                },
                None => break,
            }
        }
    }

    fn insert_fixup(node: Rc<RefCell<Node<K, T>>>) {

    }
}
