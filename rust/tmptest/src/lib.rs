use std::rc::Rc;
use std::cell::RefCell;


struct Node {
    value: i32,
    next: Option<Rc<RefCell<Node>>>,
}


impl Node {
    fn new(value: i32) -> Node {
        Node { value, next: None }
    }
}

struct LinkList {
    head: Option<Rc<RefCell<Node>>>,
}

impl LinkList {
    fn new() -> LinkList {
        LinkList { head: None }
    }

    fn insert_back(&mut self, value: i32) {
        let mut current: Option<Rc<RefCell<Node>>> = self.head.clone();
        loop {
            match current {
                Some(ref rc_node) => {
                    current = rc_node.borrow().next.clone();
                },
                None => { break; }
            }
        };
    }
}
