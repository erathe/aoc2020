use regex::Regex;
use std::str::FromStr;

#[macro_use]
extern crate lazy_static;

lazy_static! {
    static ref RE: Regex = Regex::new(r#"^(\d+)-(\d+) (.): (.+)$"#).unwrap();
}

fn main() {
    let input = include_str!("../input.txt");
    println!("{}", part1(input));
    println!("{}", part2(input));
}

fn part1(input: &str) -> usize {
    input
        .lines()
        .map(|line| line.parse::<Policy>().unwrap())
        .filter(Policy::is_valid_sled)
        .count()
}

fn part2(input: &str) -> usize {
    input
        .lines()
        .map(|line| line.parse::<Policy>().unwrap())
        .filter(Policy::is_valid_toboggan)
        .count()
}

struct Policy {
    min: usize,
    max: usize,
    ch: char,
    st: String,
}

impl Policy {
    fn is_valid_sled(Self { min, max, ch, st }: &Self) -> bool {
        let len = st.matches(*ch).count();
        len >= *min && len <= *max
    }

    fn is_valid_toboggan(Self { min, max, ch, st }: &Self) -> bool {
        let b_str = st.as_bytes();
        [min - 1, max - 1]
            .into_iter()
            .filter(|v| b_str[*v] == *ch as u8)
            .count()
            == 1
    }
}

impl FromStr for Policy {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let m = RE.captures(s).unwrap();
        Ok(Policy {
            min: m[1].parse().unwrap(),
            max: m[2].parse().unwrap(),
            ch: m[3].parse().unwrap(),
            st: m[4].parse().unwrap(),
        })
    }
}
