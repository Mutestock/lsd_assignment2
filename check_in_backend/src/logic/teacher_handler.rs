#![allow(dead_code, unused_variables, unused_imports)]

use crate::connection::pg_connection::get_pg_pool;
use crate::entities::person;

pub async fn generate_code(
    request: person::GenerateCodeRequest,
) -> Result<person::GenerateCodeResponse, Box<dyn std::error::Error>> {
    todo!();
}

pub async fn start_countdown(
    request: person::StartCountdownRequest,
) -> Result<person::StartCountdownResponse, Box<dyn std::error::Error>> {
    todo!()
}

pub async fn extend_countdown(
    request: person::ExtendCountdownRequest,
) -> Result<person::ExtendCountdownResponse, Box<dyn std::error::Error>> {
    todo!()
}
