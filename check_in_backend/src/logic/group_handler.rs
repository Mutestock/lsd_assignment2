#![allow(dead_code, unused_variables, unused_imports)]

use sqlx::Executor;

use crate::connection::pg_connection::get_pg_pool;
use crate::entities::group;

pub async fn create(
    request: group::CreateGroupRequest,
) -> Result<group::CreateGroupResponse, Box<dyn std::error::Error>> {
    sqlx::query(
        r#"
        INSERT INTO groups(name)
        VALUES($1)
        "#,
    )
    .bind(request.name)
    .execute(
        &get_pg_pool()
            .await
            .expect("Could not create pool in create group"),
    )
    .await
    .expect("Could not create group");

    Ok(group::CreateGroupResponse {
        msg: "201".to_owned(),
    })
}

pub async fn delete(
    request: group::DeleteGroupRequest,
) -> Result<group::DeleteGroupResponse, Box<dyn std::error::Error>> {
    sqlx::query(
        r#"
        DELETE FROM groups WHERE id = $1
        "#,
    )
    .bind(request.group_id)
    .execute(
        &get_pg_pool()
            .await
            .expect("Could not delete pool in delete group"),
    )
    .await
    .expect("Could not delete group");

    Ok(group::DeleteGroupResponse {
        msg: "204".to_owned(),
    })
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
