#![allow(dead_code, unused_variables, unused_imports)]

use sqlx::Executor;

use crate::connection::pg_connection::get_pg_pool;
use crate::entities::{check_in::CheckIn, person};
use crate::logic::cryptography::verify_encryption;
use crate::utils::time::time_expired;

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

    let person = sqlx::query_as::<_, person::FullPerson>(
        r#"
        SELECT * FROM people
        WHERE username = $1
        "#,
    )
    .bind(request.username)
    .fetch_one(&get_pg_pool().await?)
    .await?;

    // Did the code exist?
    match code {
        Some(v) => {
            // Is the ip valid? Is it not too late?
            if (verify_encryption(request.ip, v.ip_salt.as_bytes())?) && !time_expired(v.check_end)
            {
                sqlx::query(
                    r#"
                    INSERT INTO people_m2m_check_ins(people_name, check_in_id)
                    VALUES($1, $2)
                "#,
                )
                .bind(person.username)
                .bind(v.id)
                .execute(&get_pg_pool().await?)
                .await?;
                Ok(person::CodeCheckInResponse { checked_in: true })
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
    // Get all codes for each group for that student.
    // Get relations in people <-> check_in. Missing IDS in relations vs all codes for each group for that student = Didn't submit
    // To return: Start date, End Date, Checked in, student usernaem, is_teacher

    // Getting student with id
    let stud = sqlx::query_as::<_, person::FullPerson>(
        r#"
        SELECT * FROM people
        WHERE username = $1
        "#,
    )
    .bind(&request.username)
    .fetch_one(&get_pg_pool().await?)
    .await?;

    // Getting all check-ins of groups that the student is part of.
    let all_check_ins_in_group: Vec<CheckIn> = sqlx::query_as::<_, CheckIn>(
        r#"
        SELECT * FROM check_ins ci
        INNER JOIN groups_m2m_check_ins gmci ON ci.id = gmci.check_in_id
        INNER JOIN people p ON gmci.people_name = p.username
        WHERE p.username = $1
        "#,
    )
    .bind(&request.username)
    .fetch_all(&get_pg_pool().await?)
    .await?;

    let all_successful_check_ins: Vec<CheckIn> = sqlx::query_as::<_, CheckIn>(
        r#"
        SELECT * FROM check_ins ci
        INNER JOIN people_m2m_check_ins pmci ON ci.id = pmci.check_in_id
        INNER JOIN people p ON p.username = pmci.people_name
        WHERE p.username=$1
        "#,
    )
    .bind(request.username)
    .fetch_all(&get_pg_pool().await?)
    .await?;

    // Concatenate stat profile. Iterate through check_ins for checked_in_on_time attribute
    let stud_stats: Vec<person::get_stats_response::Stats> = all_check_ins_in_group
        .into_iter()
        .map(|x| person::get_stats_response::Stats {
            checked_in_on_time: all_successful_check_ins.iter().any(|z| x.id == z.id),
            start_date_time: x.check_start.to_string(),
            end_date_time: x.check_end.to_string(),
            username: stud.username.clone(),
            is_teacher: stud.is_teacher,
        })
        .collect();

    Ok(person::GetStatsResponse {
        all_stats: stud_stats,
    })
}

pub async fn get_all_students(
    request: person::GetAllStudentsRequest,
) -> Result<person::GetAllStudentsResponse, Box<dyn std::error::Error>> {
    let studs = sqlx::query_as::<_, person::FullPerson>(
        r#"
        SELECT * FROM people where is_teacher = false
        "#,
    )
    .fetch_all(&get_pg_pool().await?)
    .await?;

    Ok(person::GetAllStudentsResponse {
        studs: person::FullPerson::to_studs(studs),
    })
}
