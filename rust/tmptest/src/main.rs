extern crate tmptest;

fn main() {
    let mut ll = tmptest::LinkList::new();
    ll.insert_back(12);
    ll.insert_back(20);
    ll.insert_back(50);
    ll.print();

    println!("Hello, world!");
}
