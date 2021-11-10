use sqlx::FromRow;

tonic::include_proto!("user");
tonic::include_proto!("teacher");
tonic::include_proto!("student");

#[derive(sqlx::FromRow)]
pub struct NewPerson {
    is_teacher: bool,
    username: String,
    pwd: String,
    salt: String,
}

#[derive(sqlx::FromRow)]
pub struct FullPerson {
    id: i32,
    is_teacher: bool,
    username: String,
    pub pwd: String,
    salt: String,
}

impl FullPerson {
    pub fn to_studs(people: Vec<FullPerson>) -> Vec<get_all_students_response::Stud> {
        people
            .into_iter()
            .map(|x| get_all_students_response::Stud {
                id: x.id,
                is_teacher: x.is_teacher,
                username: x.username,
                password: x.pwd,
                salt: x.salt,
            })
            .collect()
    }
}
