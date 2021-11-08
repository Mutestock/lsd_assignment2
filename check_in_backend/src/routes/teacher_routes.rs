use crate::{entities::teacher, logic::teacher_handler};
use teacher::teacher_server::Teacher;
use tonic::{Request, Response, Status};

#[derive(Default)]
pub struct TeacherCon {}

#[tonic::async_trait]
impl Teacher for TeacherCon {
    async fn generate_code(
        &self,
        request: Request<teacher::GenerateCodeRequest>,
    ) -> Result<Response<teacher::GenerateCodeResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            teacher_handler::generate_code(request.into_inner())
                .await
                .expect("Person Update failed"),
        ))
    }
    async fn start_countdown(
        &self,
        request: Request<teacher::StartCountdownRequest>,
    ) -> Result<Response<teacher::StartCountdownResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            teacher_handler::start_countdown(request.into_inner())
                .await
                .expect("Person Update failed"),
        ))
    }
    async fn extend_countdown(
        &self,
        request: Request<teacher::ExtendCountdownRequest>,
    ) -> Result<Response<teacher::ExtendCountdownResponse>, Status> {
        println!("Got a request from {:?}", request.remote_addr());

        Ok(Response::new(
            teacher_handler::extend_countdown(request.into_inner())
                .await
                .expect("Person Update failed"),
        ))
    }
}
