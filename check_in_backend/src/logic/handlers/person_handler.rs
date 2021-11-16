#![allow(dead_code, unused_variables, unused_imports)]

use sqlx::Executor;
use std::str;

use crate::connection::pg_connection::get_pg_pool;
use crate::entities::person;
use crate::logic::cryptography::*;

pub async fn login(
    request: person::LoginRequest,
) -> Result<person::LoginResponse, Box<dyn std::error::Error>> {
    let person = sqlx::query_as::<_, person::FullPerson>(
        r#"
        SELECT * FROM people WHERE username = $1
        "#,
    )
    .bind(request.username)
    .fetch_one(
        &get_pg_pool()
            .await
            .expect("Could not create a pool for login"),
    )
    .await
    .expect("Could not execute login query");

    Ok(person::LoginResponse {
        login_successful: verify_encryption(person.pwd, request.password.as_bytes())
            .expect("Could not verify password for login"),
    })
}

pub async fn create_user(
    request: person::CreateUserRequest,
) -> Result<person::CreateUserResponse, Box<dyn std::error::Error>> {
    let salt = generate_salt();
    let salty_pwd = hash_and_salt(request.password, &salt)?;

    sqlx::query(
        r#"
        INSERT INTO people(is_teacher, username, pwd, salt)
        VALUES($1, $2, $3, $4)
        "#,
    )
    .bind(request.is_teacher)
    .bind(request.username)
    .bind(salty_pwd)
    .bind(str::from_utf8(&salt).expect("Could not cast salt to string"))
    .execute(
        &get_pg_pool()
            .await
            .expect("Could not create a pool for create_user"),
    )
    .await
    .expect("Could not execute create user query");

    Ok(person::CreateUserResponse {
        msg: "201".to_owned(),
    })
}
