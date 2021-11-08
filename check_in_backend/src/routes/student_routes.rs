use crate::{entities::student, logic::student_handler};
use student::student_server::Student;
use tonic::{Request, Response, Status};

#[derive(Default)]
pub struct StudentCon {}

#[tonic::async_trait]
impl Student for StudentCon {
    async fn code_check_in(
        &self,
        request: Request<student::CodeCheckInRequest>,
    ) -> Result<Response<student::CodeCheckInResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            student_handler::code_check_in(request.into_inner())
                .await
                .expect("Person Update failed"),
        ))
    }
    async fn get_stats(
        &self,
        request: Request<student::GetStatsRequest>,
    ) -> Result<Response<student::GetStatsResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            student_handler::get_stats(request.into_inner())
                .await
                .expect("Person Update failed"),
        ))
    }
    async fn get_all_students(
        &self,
        request: Request<student::GetAllStudentsRequest>,
    ) -> Result<Response<student::GetAllStudentsResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            student_handler::get_all_students(request.into_inner())
                .await
                .expect("Person Update failed"),
        ))
    }
}
