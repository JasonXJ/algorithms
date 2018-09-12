use std::rc::Rc;
use std::cell::RefCell;

type Link = Option<Rc<RefCell<Node>>>;

struct Node {
    value: i32,
    next: Link,
}


impl Node {
    fn new(value: i32) -> Node {
        Node { value, next: None }
    }

    fn new_link(value: i32) -> Link {
        Some(Rc::new(RefCell::new(Node::new(value))))
    }
}

pub struct LinkList {
    head: Link,
}

impl LinkList {
    pub fn new() -> LinkList {
        LinkList { head: None }
    }

    pub fn insert_back(&mut self, value: i32) {
        let mut previous: Link = None;
        let mut current: Link = self.head.clone();

        while let Some(rc_node) = current {
            current = rc_node.borrow().next.clone();
            previous = Some(rc_node);
        }

        match previous {
            Some(ref rc_node) => {
                rc_node.borrow_mut().next = Node::new_link(value);
            },
            None => {
                self.head = Node::new_link(value);
            }
        }
    }

    pub fn print(&self) {
        let mut current: Link = self.head.clone();
        while let Some(rc_node) = current {
            println!("{}", rc_node.borrow().value);
            current = rc_node.borrow().next.clone();
        }
    }
}
