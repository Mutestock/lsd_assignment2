use argon2::{self, Config};
use rand::Rng;

lazy_static! {
    static ref CONFIG: Config<'static> = Config::default();
}

pub fn generate_salt() -> [u8; 8] {
    rand::thread_rng().gen::<[u8; 8]>()
}

pub fn hash_and_salt_password(password: String, salt: [u8; 8]) -> Result<String, argon2::Error> {
    let password = password.as_bytes();
    argon2::hash_encoded(password, &salt, &CONFIG.to_owned())
}

pub fn verify_password(hash: String, password_bytes: [u8; 8]) -> Result<bool, argon2::Error> {
    argon2::verify_encoded(&hash, &password_bytes)
}
