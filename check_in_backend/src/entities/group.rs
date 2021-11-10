use sqlx::FromRow;

tonic::include_proto!("group");

#[derive(sqlx::FromRow)]
pub struct FullGroup{
    id: i32,
    name: String,
}

