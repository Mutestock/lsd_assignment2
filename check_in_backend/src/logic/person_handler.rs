#![allow(dead_code, unused_variables, unused_imports)]

use crate::connection::pg_connection::get_pg_pool;
use crate::entities::person;
use crate::logic::cryptography::*;

pub async fn login(
    request: person::LoginRequest,
) -> Result<person::LoginResponse, Box<dyn std::error::Error>> {
    todo!()
}

pub async fn create_user(
    request: person::CreateUserRequest,
) -> Result<person::CreateUserResponse, Box<dyn std::error::Error>> {
    let salt = generate_salt().to_string();
    let salty_pwd = hash_and_salt_password(request.password, salt)?;

    sqlx::query(
        r#"
        INSERT INTO people(is_teacher, username, pwd, salt)
        VALUES($1, $2, $3, $4, $5)
        "#
    )
    .bind(request.is_teacher)
    .bind(request.username)
    .bind(salty_pwd)
    .bind(salt.to_string())
}
