use argon2::{self, Config};
use rand::{distributions::Alphanumeric, thread_rng, Rng};

pub fn generate_salt() -> [u8; 8] {
    rand::thread_rng().gen::<[u8; 8]>()
}

pub fn hash_and_salt(item: String, salt: &[u8; 8]) -> Result<String, argon2::Error> {
    argon2::hash_encoded(item.as_bytes(), salt, &Config::default())
}

pub fn verify_encryption(hash: String, item_bytes: &[u8]) -> Result<bool, argon2::Error> {
    println!("{} - {:?}", hash, item_bytes);
    //let bytes_specific: [u8;8] = item_bytes.try_into().unwrap();
    argon2::verify_encoded(&hash, item_bytes)
}

pub fn generate_code() -> String {
    thread_rng()
        .sample_iter(&Alphanumeric)
        .take(6)
        .map(char::from)
        .collect()
}

pub fn parse_string_salt_to_byte_vector(byte_vec_string: String) -> Vec<u8> {
    let modified = byte_vec_string
        .replace("[", "")
        .replace("]", "");
    
    println!("{}", modified);

    let split_modified = modified.split(", ")
        .into_iter()
        .map(|x|x.parse::<u8>().unwrap())
        .collect();
    
    println!("SPLIT MODIFIED - {:?}",split_modified);
    
    split_modified
}
