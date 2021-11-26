tonic::include_proto!("group");


#[derive(sqlx::FromRow)]
pub struct FullGroup{
    pub id: i32,
    pub name: String
}