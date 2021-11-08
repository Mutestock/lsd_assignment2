#![allow(dead_code, unused_variables, unused_imports)]

use crate::connection::pg_connection::get_pg_pool;
use crate::entities::user;

pub async fn login(
    request: user::LoginRequest,
) -> Result<user::LoginResponse, Box<dyn std::error::Error>> {
    todo!();
}

pub async fn create_user(
    request: user::CreateUserRequest,
) -> Result<user::CreateUserResponse, Box<dyn std::error::Error>> {
    todo!()
}
