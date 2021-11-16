#![allow(dead_code, unused_variables, unused_imports)]

use sqlx::Executor;

use crate::connection::pg_connection::get_pg_pool;
use crate::entities::check_in::CheckIn;
use crate::entities::person;
use crate::utils::time::time_expired;

use crate::logic::cryptography::verify_encryption;

pub async fn code_check_in(
    request: person::CodeCheckInRequest,
) -> Result<person::CodeCheckInResponse, Box<dyn std::error::Error>> {
    let code = sqlx::query_as::<_, CheckIn>(
        r#"
        SELECT * FROM check_ins
        WHERE code = $1
        "#,
    )
    .bind(request.code)
    .fetch_optional(&get_pg_pool().await?)
    .await?;

    // Did the code exist?
    match code {
        Some(v) => {
            // Is the ip valid? Is it not too late?
            if (verify_encryption(request.ip, v.ip_salt.as_bytes())?) && !time_expired(v.check_end)
            {
                println!("TODO insert entry into code with successful login.")
            } else {
                Ok(person::CodeCheckInResponse { checked_in: false })
            }
        }
        None => Ok(person::CodeCheckInResponse { checked_in: false }),
    }
}

pub async fn get_stats(
    request: person::GetStatsRequest,
) -> Result<person::GetStatsResponse, Box<dyn std::error::Error>> {
    todo!();
}

pub async fn get_all_students(
    request: person::GetAllStudentsRequest,
) -> Result<person::GetAllStudentsResponse, Box<dyn std::error::Error>> {
    let studs = sqlx::query_as::<_, person::FullPerson>(
        r#"
        SELECT * FROM students
        "#,
    )
    .fetch_all(&get_pg_pool().await?)
    .await?;

    Ok(person::GetAllStudentsResponse {
        studs: person::FullPerson::to_studs(studs),
    })
}
