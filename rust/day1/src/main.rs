use regex::Regex;
use std::fs;

fn decodeLine(line: &str) {
    let re = Regex::new(r"(\d){1}").unwrap();
    let digits = re.captures(line).map(String::from);

    println!("{digits}")
}
fn main() {
    let file_path = "assets/puzzle.txt";
    // --snip--
    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");

    for line in contents.split("\n") {
        println!("{line}")
    }
}
