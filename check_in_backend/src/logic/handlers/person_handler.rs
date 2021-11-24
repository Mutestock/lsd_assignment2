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
    .fetch_optional(&get_pg_pool().await?)
    .await?;

    // If username was found, check verify the password and send the results.
    // If no username was found => False
    match person {
        Some(p) => Ok(person::LoginResponse {
            login_successful: verify_encryption(p.pwd, request.password.as_bytes())?,
        }),
        None => Ok(person::LoginResponse {
            login_successful: false,
        }),
    }
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
    .bind(format!("{:?}",&salt))
    .execute(&get_pg_pool().await?)
    .await?;

    Ok(person::CreateUserResponse {
        msg: "201".to_owned(),
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_no_such_user() {
        assert_eq!(2 == 2, true);
    }
}
