#![allow(dead_code, unused_variables, unused_imports)]

use crate::entities::teacher;

pub async fn generate_code(
    request: teacher::GenerateCodeRequest,
) -> Result<teacher::GenerateCodeResponse, Box<dyn std::error::Error>> {
    todo!();
}

pub async fn start_countdown(
    request: teacher::StartCountdownRequest,
) -> Result<teacher::StartCountdownResponse, Box<dyn std::error::Error>> {
    todo!()
}

pub async fn extend_countdown(
    request: teacher::ExtendCountdownRequest,
) -> Result<teacher::ExtendCountdownResponse, Box<dyn std::error::Error>> {
    todo!()
}


