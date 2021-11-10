tonic::include_proto!("user");
tonic::include_proto!("teacher");
tonic::include_proto!("student");


#[derive(sqlx::FromRow)]
pub struct NewPerson{
    is_teacher: bool,
    username: String,
    pwd: String,
    email: Option<String>,
    phone_number: Option<String>,
    salt: String,    
}

pub struct PersonLogin{
    username: String,
    pwd: String,
}