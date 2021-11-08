#![allow(dead_code, unused_variables, unused_imports)]

use crate::connection::mongo_connection::get_db_handle;
use crate::entities::group;

pub async fn create(
    request: group::CreateGroupRequest,
) -> Result<group::CreateGroupResponse, Box<dyn std::error::Error>> {
    todo!();
}

pub async fn delete(
    request: group::DeleteGroupRequest,
) -> Result<group::DeleteGroupResponse, Box<dyn std::error::Error>> {
    todo!();
}

pub async fn remove_student_from_group(
    request: group::RemoveStudentFromGroupRequest,
) -> Result<group::RemoveStudentFromGroupResponse, Box<dyn std::error::Error>> {
    todo!();
}

pub async fn add_student_to_group(
    request: group::AddStudentToGroupRequest,
) -> Result<group::AddStudentToGroupResponse, Box<dyn std::error::Error>> {
    todo!();
}
