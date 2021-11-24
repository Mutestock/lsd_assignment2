use argon2::{self, Config};
use rand::{Rng, distributions::Alphanumeric, thread_rng};

lazy_static! {
    static ref CONFIG: Config<'static> = Config::default();
}

pub fn generate_salt() -> [u8; 8] {
    rand::thread_rng().gen::<[u8; 8]>()
}

pub fn hash_and_salt(item: String, salt: &[u8; 8]) -> Result<String, argon2::Error> {
    argon2::hash_encoded(item.as_bytes(), salt, &Config::default())
}

pub fn verify_encryption(hash: String, item_bytes: &[u8]) -> Result<bool, argon2::Error> {
    argon2::verify_encoded(&hash, item_bytes)
}

pub fn generate_code() -> String {
    thread_rng()
        .sample_iter(&Alphanumeric)
        .take(6)
        .map(char::from)
        .collect()
}
