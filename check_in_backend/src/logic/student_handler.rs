#![allow(dead_code, unused_variables, unused_imports)]

use crate::connection::pg_connection::get_pg_pool;
use crate::entities::student;

pub async fn code_check_in(
    request: student::CodeCheckInRequest,
) -> Result<student::CodeCheckInResponse, Box<dyn std::error::Error>> {
    todo!();
}

pub async fn get_stats(
    request: student::GetStatsRequest,
) -> Result<student::GetStatsResponse, Box<dyn std::error::Error>> {
    todo!();
}

pub async fn get_all_students(
    request: student::GetAllStudentsRequest,
) -> Result<student::GetAllStudentsResponse, Box<dyn std::error::Error>> {
    todo!();
}
