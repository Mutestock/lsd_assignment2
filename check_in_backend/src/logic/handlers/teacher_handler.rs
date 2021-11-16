#![allow(dead_code, unused_variables, unused_imports)]

use sqlx::Executor;
use std::str;

use crate::connection::pg_connection::get_pg_pool;
use crate::entities::person;
use crate::logic::cryptography::{generate_code, generate_salt, hash_and_salt};
use crate::utils::time::get_current_time_and_add_request_millis;

pub async fn generate_code_and_start(
    request: person::GenerateCodeAndStartRequest,
) -> Result<person::GenerateCodeAndStartResponse, Box<dyn std::error::Error>> {
    let code = generate_code();
    let salt = generate_salt();

    sqlx::query(
        r#"
        INSERT INTO check_ins(check_end, allowed_ip, ip_salt, code)
        VALUES($1, $2, $3)
    "#,
    )
    .bind(get_current_time_and_add_request_millis(&request))
    .bind(hash_and_salt(request.ip_encrypted, &salt).expect("Could not hash and salt argon2 pwd"))
    .bind(match str::from_utf8(&salt) {
        Ok(v) => v,
        Err(e) => panic!("Invalid UTF-8 sequence: {}", e),
    })
    .bind(&code)
    .execute(
        &get_pg_pool()
            .await
            .expect("Could not create pg pool for generate code and start"),
    )
    .await
    .expect("could not execute generate code and start query");

    Ok(person::GenerateCodeAndStartResponse { code: code })
}

pub async fn edit_countdown(
    request: person::EditCountdownRequest,
) -> Result<person::EditCountdownResponse, Box<dyn std::error::Error>> {
    sqlx::query(
        r#"
        UPDATE check_ins SET check_end = $1
        WHERE code = $2
        "#,
    )
    .bind(request.date_time)
    .bind(request.code)
    .execute(
        &get_pg_pool()
            .await
            .expect("Could not get pool for countdown edit"),
    )
    .await
    .expect("Could not execute edit countdown query");

    Ok(person::EditCountdownResponse {
        msg: "Ok".to_owned(),
    })
}

pub async fn delete_code(
    request: person::DeleteCodeRequest,
) -> Result<person::DeleteCodeResponse, Box<dyn std::error::Error>> {
    sqlx::query(
        r#"
        DELETE FROM check_ins where code = $1
        "#,
    )
    .bind(request.code)
    .execute(
        &get_pg_pool()
            .await
            .expect("Could not create pool for delete code query"),
    )
    .await
    .expect("Could not execute delete code query");

    Ok(person::DeleteCodeResponse {
        msg: "Ok".to_owned(),
    })
}
