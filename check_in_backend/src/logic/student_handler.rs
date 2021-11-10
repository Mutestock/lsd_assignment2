#![allow(dead_code, unused_variables, unused_imports)]

use crate::connection::pg_connection::get_pg_pool;
use crate::entities::person;

pub async fn code_check_in(
    request: person::CodeCheckInRequest,
) -> Result<person::CodeCheckInResponse, Box<dyn std::error::Error>> {
    todo!();
}

pub async fn get_stats(
    request: person::GetStatsRequest,
) -> Result<person::GetStatsResponse, Box<dyn std::error::Error>> {
    todo!();
}

pub async fn get_all_students(
    request: person::GetAllStudentsRequest,
) -> Result<person::GetAllStudentsResponse, Box<dyn std::error::Error>> {
    todo!();
}
